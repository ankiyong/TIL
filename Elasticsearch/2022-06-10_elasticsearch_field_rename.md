# elasticsearch field rename

```
PUT _ingest/pipeline/my_rename_pipeline
{
  "description" : "describe pipeline",
  "processors" : [
    {
      "rename": {
        "field": "차sam계정",
        "target_field": "1차sam계정"
      }
    }
  ]
}
GET test12345/_search
POST _reindex
{
  "source": {
    "index": "test1234"
  },
  "dest": {
    "index": "test12345",
    "pipeline": "my_rename_pipeline"
  }
} 
```

