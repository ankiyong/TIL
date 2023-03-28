## logstash filter split

```json
filter {
	split { }

	mutate {
		split => { "message" => "|" }
		add_field => {
			"first" => "%{[message][0]}"
			"second" => "%{[message][1]}"
			"third" => "%{[message][2]}"
		}
	}
}
```

