

# elasticsearch alias is_write_index option

다수의 index가 연결된 alias를 대상으로 색인요청하는 경우 test

##### test 환경

- elasticsearch 8.3.2 version
- kibana 8.3.2 version

##### Case 1 : 단일 index와 연결된 alias에 색인 요청

##### Case 2 : 다수의 index와 연결된 alias에 색인 요청

## Case 1 

##### 진행순서

1. index 1개 생성
2. 생성된 index에 alias 설정
3. alias에 색인 요청
4. 결과 확인

### 1.index 생성

```json
PUT test_index
```

### 2.생성된 index에 alias 설정

```json
POST _aliases
{
	"actions" : [
        {
        	"add" : {
                "index" : "test_index",
                "alias" : "alias1"
            }   
        }        
    ]
}
```

### 3.alias에 색인 요청

```json
POST alias1/_doc
{
    "name" : "an"
}
```

### 4.결과 확인

```json
#search
GET alias1/_search
{
    "query" : {
        "match_all" : {}
    }
}

#result
...
"hits": [
  {
    "_index": "test_index_1",
    "_id": "60-Sj4IBti63olZ1HeUp",
    "_score": 1,
    "_source": {
	    "name": "an"
   	}
  }
```

## Case 2

##### 진행순서

1. index 3개 생성
2. 생성된 index에 alias 설정
3. alias에 색인 요청
4. 결과 확인

### 1.index 생성

```json
PUT test_index_2
PUT test_index_3
PUT test_index_4
```

### 2.생성된 index에 alias 설정

```json
POST _aliases
{
  "actions": [
    {"add": {"index": "test_index_2","alias": "alias2"}},
    {"add": {"index": "test_index_3","alias": "alias2"}},
    {"add": {"index": "test_index_4","alias": "alias2"}}
  ]
}
```

### 3.alias에 색인 요청

```json
POST alias2/_doc
{
  "name" : "an"
}
```

### 4.결과 확인

```json
{
  "error": {
    "root_cause": [
      {
        "type": "illegal_argument_exception",
        "reason": "no write index is defined for alias [alias2]. The write index may be explicitly disabled using is_write_index=false or the alias points to multiple indices without one being designated as a write index"
      }
    ],
    "type": "illegal_argument_exception",
    "reason": "no write index is defined for alias [alias2]. The write index may be explicitly disabled using is_write_index=false or the alias points to multiple indices without one being designated as a write index"
  },
  "status": 400
}
```

## test 결과

2개의 case를 통해 각각의 사실을 도출할 수 있었다.

1. 단일 index가 연결된 alias는 색인 요청이 정상적으로 작동한다.
2. 다수 index가 연결된 alias는 색인 요청이 작동하지 안호고 오류가 발생한다.

위의 결과와 관련하여 공식 문서에서는 다음과 같이 설명한다

- 1개의 Alias에 2개 이상의 Index가 설정되어 있을 경우 1개의 Alias 당 정확히 1개의 Index만 write 가능(index/update) Index로 설정할 수 있다.
- 2개 이상의 Index가 Alias와 연결되어 있는 경우, 어느 하나의 Index에 명시적으로 is_write_index가 설정되어 있어야 데이터 입력이 정상적으로 되며 그렇지 않을 경우 오류가 발생한다.

## 추가 test

##### alias 설정시 is_write_index 옵션 추가

### 1.alias 설정을 다시 하면서 is_write_index 옵션 추가

```json
POST _aliases
{
  "actions": [
    {
      "remove": {
        "index": "test_index_3",
        "alias": "alias2"
      }
    },
    {
      "add": {
        "index": "test_index_3",
        "alias": "alias2",
        "is_write_index" : true
      }
    }
  ]
}
```

### 2.alias에 색인 요청

```json
POST alias2/_doc
{
  "name" : "an"
}
```

### 3.결과 확인

```json
#search
GET alias1/_search
{
    "query" : {
        "match_all" : {}
    }
}

#result
...
"hits": [
  {
    "_index": "test_index_3",
    "_id": "60-7k_Ij4IBti63olZ1IOXL",
    "_score": 1,
    "_source": {
	    "name": "an"
   	}
  }
```

## 결과

1. 다수의 index와 연결된 alias에 색인 요청을 하기 위해서는 is_write_index 옵션을 true로 설정해줘야 한다. 
2. alias 내에 하나의 index만 설정할 수 있다. 
3. 설정한 후에는 설정된 index에만 색인 요청을 보내고, 색인된다.