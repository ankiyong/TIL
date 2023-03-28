# synonym filter test

synonym filter의 여러 사용에 대해 test한 내용이다.

```json
#기본 index 형태
PUT /test_index
{
  "settings": {
    "index": {
      "analysis": {
        "analyzer": {
          "synonym_analyzer": {
            "tokenizer": "whitespace",
            "filter": ["lowercase", "my_synonyms"]
          }
        },
        "filter": {
          "my_synonyms": {
            "type": "synonym",
            "synonyms": ["Eins, Uno, One", "Cosmos => Universe"]
          }
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "text" : {
        "type": "text",
        "analyzer": "synonym_analyzer"        
      }
    }
  }
}

#색인 내용
PUT test_index/_doc/1
{
  "text" : "uno"
}
```

```json
#case1. 검색,색인 두 경우 모두 synonym 사용
GET test_index2/_search
{
  "query": {
    "match": {
      "text": {
        "query": "one"
      }
    }
  }
}

#결과
   "hits" : [
      {
        "_index" : "test_index2",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 0.5274172,
        "_source" : {
          "text" : "uno"
        }
      }
    ]
```

```json
#case2. 검색 시에만 synonym 사용
GET test_index/_search
{
  "query": {
    "match": {
      "text": {
        "query": "one",
        "analyzer": "synonym_analyzer"
      }
    }
  }
}

#결과
    "hits" : [
      {
        "_index" : "test_index",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 0.2876821,
        "_source" : {
          "text" : "uno"
        }
      }
    ]
```

```json
#case3. 색인 시에만 synonym 사용
GET test_index1/_search
{
  "query": {
    "match": {
      "text": {
        "query": "one"
      }
    }
  }
}

#결과
    "hits" : [
      {
        "_index" : "test_index1",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 0.5274172,
        "_source" : {
          "text" : "uno"
        }
      }
    ]
```

news index에 설정하여 비교해본 내용

##### 결과

검색시에 search analyzer에만 synonym을 설정해 두는것이 좋다. 검색 결과 수는 같지만 다른 score를 보이게 된다. 모든 document가 일정한 비율로 score 하락이 오는것이 아니고, 아예 새로운 score가 계산되어 부여된다. 

1. 색인시에 사용하면 index의 크기가 계속 커진다.
2. update에 불편함이 따른다.
3. highlight가 생각과는 조금 다르게 표시된다.

```json
#synonym 설정 내용
"filter": {
    "my_synonyms": {
      "type": "synonym",
      "synonyms": ["문대통령, 문재인, 대통령", "국민의 힘,국힘,국민의힘 => 국민의힘"]
}

#query DSL
GET news_sy1/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "id": "29739"
          }
        }
      ],
      "must": [
        {
          "match": {
            "title": {
              "query": "문재인",
              "analyzer": "nori_analyzer1"
            }
          }
        }
      ]
    }
  },
  "highlight": {
    "fields": {
      "title" : {}
    }
  },
  "explain": true
}
```

