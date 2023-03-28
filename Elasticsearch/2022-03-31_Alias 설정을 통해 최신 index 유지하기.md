### Alias 설정을 통해 최신 index 유지하기

먼저 _reindex API를 통해 인덱스를 생성한다.

```json
POST _reindex
{
	"source" : {
		"index" : "my_index1"
        },
    "dest" : {
    	"index" : "my_info"
    }
}
```

인덱스 생성 이후 _aliases를 통해 두 인덱스의 별칭을 만들 수 있다.

```json
POST _aliases
{
	"actions" : [
		{"add" : {"index" : "my_index1",
                  "alias" : "alias_name"}},
		{"add" : {"index" : "my_info",
                  "alias" : "alias_name"}}
	]
}
```

앞서 생성한 my_index1,my_info가 alias_name 이라는 별칭을 갖게 되었다. 

이제 index를 별칭으로 검색할 수 있게 되었다.

```json
GET alias_name/_search
```



alias 설정은 index를 다시 만드는 경우에 많이 활용된다. data는 자주 변경되는 경우가 빈번하기 때문에 index를 삭제하고 다시 만드는 경우가 많아서 alias 설정을 많이 사용하게 된다.

```json
POST _aliases
{
	"actions" : [
		{"remove" : {"index" : "삭제할index",
                     "alias" : "alias_name"}},
		{"add" : {"index" : "새로운index",
                  "alias" : "alias_name"}}
		
	]
}
```

