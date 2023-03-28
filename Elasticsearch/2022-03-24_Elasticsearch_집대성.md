## Elasticsearch 기본 조작

#### index CRUD

```
#settings, mappings로 index 만들기
PUT my_index
{
	"settings" : {
		"index" : {
			"number_of_shards" : 3,
			"number_of_replicas" : 1
		}
	},
	"mappings" : {
		"properties" : {
			"name" : {
				"type" : "keyword"
			}
		}
	}
}

#index 삭제
DELETE my_index

#index 조회
GET my_index/_search 내용 조회
GET my_index/_settings 세팅 조회
GET my_index/_mappings 매핑 조회

#index 수정
POST my_index/_update/1
{
	"doc" : {
		"name" : "kim"
	}
}
```



#### mapping

```
#index의 field type을 mapping으로 미리 설정할 수 있다.
PUT my_index
{
	"mappings" : {
		"properties" : {
			"name" : {
				"type" : "keyword"
			},
			"age" : {
				"type" : "integer"
			}
		}
	}
}

#날짜 타입을 mapping할때는 format을 지정해 줄 수 있다
PUT my_index
{
	"mappings" : {
		"properties" : {
			"name" : {
				"type" : "keyword"
			},
			"date" : {
				"type" : "date",
				"format" : "yyyy-MM-dd" HH:mm:ss
			}
		}
	}
}

#필드 아래 필드를 둬서 계층적으로 mapping할 수 있다.
PUT my_index
{
	"mappings" : {
		"properties" : {
			"region" : {
				"type" : "keyword"
			},
			"manager" : {
				"properties" : {
					"age" : {
						"type" : "ingeger"
					},
					"name" : {
						"properties" : {
							"first" : {"type" : "keyword"},
							"last" : {"type" : "keyword"},
							"full" : {"type" : "text"}
						}
					}
				}
			}
		}
	}
}
=> 위와 같은 경우 full 필드를 기준으로 검색하고 싶을 때 필드 명을 manager.name.full 로 잡고 쿼리를 작성하면 된다.
```



#### Document indexing

```
#document id를 통해 색인
PUT my_index/_doc/1
{
	"name" : "an",
	"age" : 14
}

#document id 없이 색인 -> 자체적으로 id를 생성한다.
POST my_index/_doc
{
	"name" : "kim",
	"age" : 35
}
```



#### BULK API

```
#여러 개의 index를 CRUD할 때 사용된다.
POST _bulk
{"index" : {"_index" : "my_index","_id" : "1"}}
{"name" : "na"}
{"index" : {"_index" : "my_index","_id" : "2"}}
{"name" : "kim"}
{"index" : {"_index" : "my_index","_id" : "3"}}
{"name" : "lee"}
```



#### Search

##### Requqst Body Search

```
GET bank/_search
{
	"from" : 0,"size" : 10,
	"query" : {
		"match" : {
			"field" : "value"
		}
	}
}

# pagination
#검색 결과의 0번지 부터 2개의 결과를 보여준다.
GET bank/_search
{
	"from" : 0, "size" : 2,
	"query" : {
		"match" : {
			"address" : "Fleet"
		}
	}
}

#정렬 
GET bank/_search
{
	"sort" : {
		"age" : "desc"
	}
}

#원하는 필드만 출력
GET bank/_search
{
	"_source" : ["age"],
	"sort" : "asc"
}

#검색결과 강조 효과
GET bank/_search
{
	"query" : {
		"match" : {
			"name" : {
				"query" : "an"
			}
		}
	},
	"highlight" : {
		"fields" : {
			"name": {}
		}
	}
}
이런 결과가 반환된다
 "_index" : "my_index1",
        "_type" : "_doc",
        "_id" : "7",
        "_score" : 0.44183272,
        "_source" : {
          "name" : "an",
          "age" : 17
        },
        "highlight" : {
          "name" : [
            "<em>an</em>"
          ]
        }
      },
      
```



##### query context - 유사도 스코어를 검사해서 가장 유사한 결과를 보여준다. 이때 검색하고자 하는 필드는 text 타입으로 매핑 되어 있어야 한다.

```
# match query
GET my_index/_saerch
{
	"query" : {
		"match" : {
			"name" : "a"
		}
	}
}

# match query에서 operator 사용
GET my_index/_search
{
	"query" : {
		"match" : {
			"name" : "mary bailey",
			"operator" : "and"
		}
	}
}
=> mary와 bailey 모두 포함된 필드를 검색한다.
=> or로 설정했다면 mary 또는 bailey가 포함된 필드를 검색한다.

# match phrase query
GET my_index/_search
{
	"query" : {
		"match_phrase" : {
			"address" : "123 street W"
		}
	}
}

# multi match query
GET my_index/_search
{
	"query" : {
		"multi_match" : {
			"query" : "value",
			"fields" : ["field1","field2"]
		}
	}
}
=> value 값을 rield1,firld2에서 모두 검색한다.

```

##### filter context - 유사도 스코어와 관계 없이 검색어와 일치하는 항목이 있을 때 결과를 보여준다. 정확히 일치해야 하기 때문에 대소문자를 구분해줘야 한다.

```
#term query
GET my_index/_search
{
	"query" : {
		"term" : {
			"name" : "an"
		}
	}
}

#terms query
GEt my_index/_search
{
	"query" : {
		"terms" : {
			"day_of_week" : [
				"Monday","Sunday"		
			]
		}
	}
}
```



##### 그 밖의 쿼리

```
# range query
GET my_index/_search
{
	"query" : {
		"range" : {
			"age" : {
				"gte" : 25,
				"lte" : 30
			}
		}
	}
}
=> 범위 쿼리는 relation옵션을 통해 검색 옵션을 조정할 수 있다.
=> contains,within등이 있다.

#wildcard query
GET my_index/_search
{
	"query" : {
		"wildcard" : {
			"name.keyword" : "a*n"
		}
	}
}
=> keyword 타입의 필드에만 사용 가능하다.

#날짜/시간 data type
GET my_index/_search
{
	"query" : {
		"range" : {
			"date" : {
				"gte" : "now-1M"
			}
		}
	}
}
=> 현재 날짜로 부터 1달 전까지의 모든 데이터를 가져오는 쿼리다.
```

| 표현식            | 설명                        |
| ----------------- | --------------------------- |
| now               | 현재 시각                   |
| now+1h+30m        | 현재 시각 + 1일             |
| now+1h+30m        | 현재 시각 + 1시간 30분 10초 |
| 2021-01-21\|\|+1M | 2021-01-21 + 1달            |



##### Compound query - 다양한 쿼리를 조합할 수 있도록 4개의 타입을 지원한다.

```
GET my_index/_search
{
	"qeury" : {
		"bool" : {
			"must" : [
				{쿼리문},...
			],
            "must_not" : [
				{쿼리문},...
			],
			"should" : [
				{쿼리문},...
			],
			"filter" : [
				{쿼리문},...
			],
		}
	}
}

# must type
GET my_index/_search
{
	"query" : {
		"bool" : {
			"must" : {
				"field" : "value"
			}
		}
	}
}
=> must type은 쿼리를 실행하고 참인 도큐먼트를 검색한다.
GET my_index/_search
{
    "query" : {
        "bool" : {
            "must" : [
                {"term" : {"field1" : "keyword"} },
                {"match" : {"field2" : "text" } }
            ]
        }
    }
}
=> 복수의 쿼리를 실행하면 and의 효과를 얻을 수 있다.

# must_not type
GET my_index/_search
{
	"query" : {
		"bool" : {
			"must_not" : {
				"match" : {"field" : {"query" : "value"}}
			}
		}
	}
}
=> field에 value가 들어가지 않은 document를 매칭한다.

GET my_index/_search
{
	"query" : {
		"bool" : {
			"must_not" : {
				"match" : {"field" : "value"}}
			},
			"must" : {
				"range" : {
					"age" : {
						"gte":10,"lte":30
					}
				}
			}
		}
	}
}
=> 위의 쿼리처럼 다양한 쿼리를 조합해서 사용할 수 있다.

# should type
GET my_index/_search
{
	"query" : {
		"bool" : {
			"should" : {
				"match" : {"field" : "value"}
			}
		}
	}
}
=> should type은 단일 쿼리만 실행했을 때는 must type과 결과가 같다.

GET my_index/_search
{
	"query" : {
		"bool" : {
			"should" : [
				{"match" : {"field" : "value"}},
				{"term" : {"field" : "value"}}
			]
		}
	}
}
=> 복수의 쿼리를 실행하게 되면 must와는 반대로 두 query가 or 조건으로 묶이게 된다.
```



#### Aggregations

```
#집계의 기본 형태
GET my_index/_search
{
	"aggs" : {
		"my_aggs" : {
			"aggs_type" : {
				...
			}
		}
	}
}
# my_aggs => 사용자가 지정하는 집계 명
# aggs_type => 사용할 집계 타입
```

##### Metric aggregations

| 메트릭 집계  | 설명                                                  |
| ------------ | ----------------------------------------------------- |
| avg          | 필드의 평균값을 계산한다.                             |
| min          | 필드의 최솟값을 계산한다.                             |
| max          | 필드의 최댓값을 계산한다.                             |
| sum          | 필드의 총합을 계산한다.                               |
| percentiles  | 필드의 백분윗값을 계산한다.                           |
| stats        | 필드의 min, max, sum, avg, count를 한번에 볼 수 있다. |
| cardinaltity | 필드의 유니크한 값 개수를 보여준다.                   |
| geo-centroid | 필드 내부의 위치 정보의 중심점을 계산한다.            |

```
#평균/중간값 구하기
GET my_index/_search
{
	"aggs" : {
		"my_avg" : {
			"avg" : {
				"field" : "age"
			}
		}
	}
}
GET my_index/_search
{
	"aggs" : {
		"my_median" : {
			"percentiles" : {
				"field" : "age",
				"percents" : [
				25,
				50
				]
			}
		}
	}
}

# 필드의 유니크한 값 개수 확인하기
GET my_index/_search
{
	"aggs" : {
		"cartinality" : {
			"field" : "name",
			"precision_threshould" : 100
		}
	}
}
=> precision_threshould는 정확도를 나타낸다. 값이 높을 수록 정확도는 높아지지만 자원을 많이 소모하게 된다.
```

