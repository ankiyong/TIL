# Elasticsearch constant_score

score를 1로 고정하는 constant_score 옵션 테스트

##### test 환경

- elasticsearch 7.10.2 version
- kibana 7.10.2 version

## 1.일반적인 검색

elasticsearch에서 검색 requert를 하게 되면 score를 계산하여 보여주게 된다.

```json
#검색 query
GET my_index1/_search
{
  "query": {
    "term": {
      "name": {
        "value": "an"
      }
    }
  }
}
#결과
{
 "_index" : "my_index1",
 "_type" : "_doc",
 "_id" : "4",
 "_score" : 1.4552872,
 "_source" : {
  "name" : "an",
  "age" : 11,
  "gender" : "male",
  "title" : "Harry Potter and the Goblet of Fire"
        }
}
```

## 2.constant_score 설정

구조화된 데이터에서는 score를 굳이 산출하여 자원을 낭비할 필요가 없다. 

##### constant_score 옵션을 통해 score계산을 하지 않고 1로 고정시킬 수 있다.

```json
#검색 query
GET my_index1/_search
{
  "query": {
    "constant_score": {
      "filter": {
        "match": {
          "name": "an"
        }
      },
      "boost": 1.2
    }
  }
}
#결과
      {
        "_index" : "my_index1",
        "_type" : "_doc",
        "_id" : "4",
        "_score" : 1.2,
        "_source" : {
          "name" : "an",
          "age" : 11,
          "gender" : "male",
          "title" : "Harry Potter and the Goblet of Fire"
     }
}
=> score는 기본적으로 1이 되고 boost로 지정한 1.2가 가중치로 계산되어 1.2의 score를 출력하고 있다.
```

### 결론

1. bool query 안에서 filter를 사용하는 것과 동일한 효과
2. 단독으로 사용되기 보다는 bool query 안에서 다른 query와 결합되었을 때 활용도가 좋을 것으로 보임