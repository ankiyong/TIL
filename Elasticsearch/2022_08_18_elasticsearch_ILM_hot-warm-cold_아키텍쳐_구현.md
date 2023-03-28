# elasticsearch ILM hot-warm-cold 아키텍쳐 구현

## hot-warm-cold node

elasticsearch는 shard 내 data의 중요도,사용 빈도에 따라 hot,warm,cold 으로 정의된 node에 각각 할당할 수 있다. 각각의 node는 아래 그림처럼 구성될 수 있으며 최소 2개의 node만 있어도 구현 가능하다.

![hot_warm_cold](C:\Users\pop24\Desktop\source_code\Elasticsearch\image\hot_warm_cold.png)

각 node는 hot-warm-cold 순으로 중요도가 높기 때문에 서로 다른 사양으로 구성하게 된다. (일반적으로 hot node는 더 많은 CPU 리소스와 빠른 IO가 필요하고, warm,cold node는 더 많은 disk 공간이 필요하지만 CPU 리소스는 적더오 되고 IO는 더 느려도 된다.)

## ILM을 사용해 how-warm-cold 아키텍쳐 구현

아키텍쳐 구현은 다음과 같은 순서로 진행된다.

1. data roles 설정
   - elasticsearhc.yml 파일 내의 data.roles 설정으로 hot,warm,cold node를 지정해준다.
2. ILM 정책 구성
   - 조건에 부합하는 shard의 위치를 조정하기 위한 정책을 구성한다.
3. Index pattern 정의
   - index pattern을 정의하여 ILM 정책과 연결해준다.

##### 아래의 예는 hot-warm-delete 로 구성되어 있다.

### 1. data.roles 설정

```json
#node1 elasticsearch.yml
data.roles: ["data_hot","master"]

#node2 elasticsearch.yml
data.roles: ["data_warm","master"]

#node3 elasticsearch.yml
data.roles: ["data_warm","master"]
```

### 2. ILM 정책 설정

```json
PUT _ilm/policy/aky
{
  "policy": {
    "phases": {
      "hot": {               ···> #1
        "min_age": "0ms",
        "actions": {
          "rollover": {
            "max_size": "5gb",
            "max_docs": 1
          },
          "set_priority": {
            "priority": 100
          }
        }
      },
      "warm": {              ···> #2
        "min_age": "30s",
        "actions": {
          "set_priority": {
            "priority": 50
          },
          "allocate": {
            "number_of_replicas": 0
          }
        }
      },
      "cold": {             ···> #3
        "min_age": "1m",
        "actions": {
          "delete": {
            "delete_searchable_snapshot": true
          }
        }
      }
    }
  }
}

# 1 - index의 size 50GB 혹은 doc의 수가 10개를 초과 하면 자동으로 rollover가 진행되고 새로운 index가 생성된다.
# 2 - rollover 30초 이후에는 warm node에 진입한다. warm node에 진입하게 되면 shard의 replica를 0개로 설정하여 재할당 한다. 
# 3 - rollover 1분 이후 cold node에 진입하게 된다.

```

### 3. Index template 설정

```json
PUT /_template/my-log-template
{
  "index_patterns": [
    "news-*"
  ],
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 2,
    "index": {
      "routing.allocation.include._tier_preference": "data_hot",
      "lifecycle": {
        "name": "aky",
        "rollover_alias": "news",
        "parse_origination_date": true
      }
    }
  }
}

```

### 4. Alias 설정

```json
PUT /%3Cnews-%7Bnow%2Fd%7D-000001%3E
{
  "aliases": {
    "news": { "is_write_index": true } 
  }
}

#index 설정에서 "parse_origination_date": true 설정을 해줬기 때문에 date math 형식으로 index 이름을 설정해 줘야 한다.
#false로 설정해도 되지만 now를 사용하기 위해서는 true로 설정해야 할 것 같다.
```

## 결과

### 1. news alias에 속한 index가 생성된다.

![hot_warm_cold](C:\Users\pop24\Desktop\source_code\Elasticsearch\image\1.png)

### 2. ILM 정책에 따라 1개 이상의 doc를 색인하게 되면 rollover하여 새로운 index가 생성된다. 기존의 index는 rollover 된 시점으로 부터 30초가 경과하면 warm 단계로 진입한다.

![hot_warm_cold](C:\Users\pop24\Desktop\source_code\Elasticsearch\image\3.png)

### 3. rollover 된 시점으로 부터 1분이 경과하면 기존의 index는 delete phase로 진입하여 삭제된다.

![hot_warm_cold](C:\Users\pop24\Desktop\source_code\Elasticsearch\image\4.png)