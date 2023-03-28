agg할때

index 생성시에 text type field에 대해 fielddata : true 옵션을 주면 agg가 가능ㄹ하다. 하지만, new york을 agg할 때 new/york를 각각 집계하게 된다. 그래서 keyword 사용하여 전체 단어를 집계 대상으로 삼아야 할 경우가 있을 수 있다. 



GET /agg_analysis/_search
{
    "size" : 0,
    "aggs" : {
        "states" : {
            "terms" : {
                "field" : "state"
            }
        }
    }
}



PUT agg_analysis
{
  "mappings": {
    "properties": {
      "state" : {
        "type" : "text",
        "fielddata": true
      }
    }
  }
}