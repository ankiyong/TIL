## logstash sql_last_value 사용법

```json
input {
  jdbc {
    jdbc_driver_library => "/home/elastic/mysql-connector-java-8.0.28/mysql-connector-java-8.0.28.jar"
    jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
    jdbc_connection_string => "jdbc:mysql://192.168.219.192:3306/article"
    jdbc_user => "root"
    jdbc_password => "MySQL2022!"
    tracking_column_type => "numeric"
    #기준으로 삼을 컬럼의 타입을 지정해준다.
    use_column_value => true
    #true로 설정해야 tracking_column을 사용할 수 있다
    tracking_column => id
    #기준으로 사용할 컬럼을 지정해준다.
    statement => "SELECT * FROM news1 WHERE id > :sql_last_value"
  }
}

#데이터 전송 기록을 남기기 위해 특정 파일에 정보가 저장되는데, 기본경로는 ~/.logstash_jdbc_last_run
이다.



```

