# elasticsearch search after

10000개 이상의 doc를 확인하거나 paging을 할 때 사용

```json
#first request
GET naver_news/_search
{
  "size" : "10000",
  "query": {
    "match_all": {}
  },
  "sort": [
    {"id" : "asc"}
  ]
}
=> 먼저 sort를 통해 sort 값을 가져온다.

#second requert
GET naver_news/_search
{
  "search_after" : [10000]
  "size" : "10000",
  "query": {
    "match_all": {}
  },
  "sort": [
    {"id" : "asc"}
  ]
}
=> sort로 나온 값을 search_after에 넣어주면 해당 번호 이후의 doc확인이 가능하다. 
```



