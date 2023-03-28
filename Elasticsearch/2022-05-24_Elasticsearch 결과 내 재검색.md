# Elasticsearch 결과 내 재검색

```json
GET kibana_sample_data_flights/_search
{
  "query": {
    "query_string": {
      "query": "Sunny",
      "fields": [
        "OriginWeather"
      ]
    }
  },
  "post_filter": {
    "query_string": {
      "query": "Frankfurt am Main",
      "fields": [
        "OriginCityName"
      ]
    }
  }
}
```

