# LS를 통해 DB를 ES로 sync하기

DB에 있는 data를 ES로 동기화 하기 위해서는 각 row를 식별할 수 있는 id값과 시간을 비교하기 위한 unix_timestamp column값이 필요하다.

```json
input {
  jdbc {
    jdbc_driver_library => "C:/Program Files (x86)/MySQL/Connector J 8.0/mysql-connector-java-8.0.28.jar"
    jdbc_driver_class => "com.mysql.jdbc.Driver"
    jdbc_connection_string => "jdbc:mysql://root@192.168.219.210:3306/HIWDB"
    jdbc_user => "root"
    jdbc_password => "Netand141)"
    jdbc_paging_enabled => true
    tracking_column => "unix_ts_in_secs"
    use_column_value => true
    tracking_column_type => "numeric"
    schedule => "*/2 * * * * *"
    statement => "SELECT UNIX_TIMESTAMP(B.REG_DTTM) AS unix_ts_in_secs
    				#등록시간인 REG_DTTM을 UNIX_TIMESTAMP 함수를 사용하여 형식을 변경해준다.
		, B.EQMT_NO
		, B.EQMT_NM
		...
	, (SELECT @n := 0) m
	WHERE (UNIX_TIMESTAMP(B.REG_DTTM) > :sql_last_value AND B.REG_DTTM < NOW()) 
	#where 조건을 통해 last_value 값보다 등록시간 값이 큰 row만 indexing을 진행한다.
	ORDER BY B.REG_DTTM"
  }
}


filter {
  mutate {
    copy => { "eqmt_no" => "[@metadata][_id]"}
	#식별자가 될 수 있는 eqmt_no 를 _id로 지정해준다.
    remove_field => ["id", "@version", "unix_ts_in_secs"]
  }
}
output {
		elasticsearch {
		hosts => "localhost:9200"
		document_id => "%{[@metadata][_id]}"
		index => "test123456"
	}
}

```

| option               | 설명                                                         |
| -------------------- | ------------------------------------------------------------ |
| tracking_column      | last_value값으로 사용하기 위한 추척 column명                 |
| use_column_value     | true로 설정하지 않으면 설정한 tracking_col 값이 아닌 현재 시간을 last_value로 사용한다. |
| tracking_column_type | numeric / date type을 지정할 수 있다.                        |
| schedule             | ls의 reload 주기를 설정한다. cron과 동일한 문법이다.         |

