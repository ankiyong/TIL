# Function score query

특정 필드에 가중치를 주는 Function score query 옵션 테스트

=> 필드의 값(숫자)에 직접 가중치를 줘서 스코어를 조정할 수 있다.

##### test 환경

- elasticsearch 8.3.2 version
- kibana 8.3.2 version

##### Case 1 : document에 9개의 직급을 random하게 지정해주고 그에 따른 가중치를 price field에 지정해준다.

## Case 1

##### 진행순서

1. index 생성
2. function score query 테스트
3. 테스트 결과 확인
4. 기존에 진행했던 news 프로젝트에 적용
5. 결과 확인

### 1.index 생성

```python
#9개의 직급과 그에 따른 가중치를 각각 rank,price field에 색인
es = Elasticsearch("localhost:9200")
docs = []
rank = ["사장","전무","상무","부장","차장","과장","대리","사원","인턴"]
for i in range(1000):
    r = random.choice(rank)
    if r == "사장": n = 10
    elif r == "전무": n = 9
    elif r == "상무": n = 8
    elif r == "부장": n = 7
    elif r == "차장": n = 6
    elif r == "과장": n = 5
    elif r == "대리": n = 4
    elif r == "사원": n = 3
    elif r == "인턴": n = 2
    docs.append(
        {"_index" : "com_rank",
        "_source" : {
            "rank" : r,
            "price" : n
            }
        }
    )
helpers.bulk(es,docs)
```

```json
{
  ...
  "hits" : {
    "total" : {
      "value" : 1000,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "com_rank",
        "_type" : "_doc",
        "_id" : "jp1YH4IBj7VPJNSvzCQr",
        "_score" : 1.0,
        "_source" : {
          "rank" : "전무",
          "price" : 9
        }
		...
      {
        "_index" : "com_rank",
        "_type" : "_doc",
        "_id" : "l51YH4IBj7VPJNSvzCQr",
        "_score" : 1.0,
        "_source" : {
          "rank" : "차장",
          "price" : 6
        }
      }
    ]
  }
}

```

### 2.function_score

```json
#price 값에 대해 factor 값 만큼 modifier에 명시된 연산을 진행하여 socre에 반영해준다.
#이때 price field가 존재하지 않는 document에 대해서는 missing값 만큼 연산하여 score에 반영해준다.
GET com_rank/_search
{
  "query": {
    "function_score": {
      "field_value_factor": {
        "field": "price",
        "factor": 1.2,
        "modifier": "sqrt",
        "missing": 1
      }
    }
  }
}
```

### 3.결과 확인

```json
{
	...
    "max_score" : 3.4641018,
    "hits" : [
      {
        "_index" : "com_rank",
        "_type" : "_doc",
        "_id" : "j51YH4IBj7VPJNSvzCQr",
        "_score" : 3.4641018,
        "_source" : {
          "rank" : "사장",
          "price" : 10
        }
      },
      ...
      {
        "_index" : "com_rank",
        "_type" : "_doc",
        "_id" : "151YH4IBj7VPJNSvzCQr",
        "_score" : 3.4641018,
        "_source" : {
          "rank" : "사장",
          "price" : 10
        }
      }
    ]
  }
}

```

###### price field에 저장된 숫자가 클수록 높은 출력 우선순위가 생기게 되어 상단에 노출된다.

### 4.news index에 적용

match 검색의 결과에 대해 score를 재조정하여 출력 우선순위를 조조정 

```json
GET news/_search
{
  "query": {			···> #1
    "function_score": {
      "query": {
        "match": {
          "title": "삼성"
      }
    },
      "field_value_factor": {
        "field": "id",	···> #2
        "factor": 1.3,	···> #3
        "modifier": "sqrt", ···> #4
        "missing": 1
      }
    }
  }
}
# 1 - 검색하고싶은 query를 작성한다.
# 2 - 가중치를 주고싶은 field를 지정한다.
# 3 - 부여하고 싶은 가중치를 설정한다.
# 4 - 가중치 계산 방법을 설정한다.

```

### 5.결과

id값이 높은 document의 score가 높아진다.

