# logstash error

```
#error명
[logstash.inputs.jdbc     ][main][a2cdc8aea9e3568be609b8294b04b99260831021fc4f4390f7aec7705833fa20] Exception when executing JDBC query {:exception=>"Java::JavaSql::SQLException: Invalid utf8mb4 character string: '1\\xEC'"}

#해결
field명으로 숫자+한글 을 사용하면 위의 에러가 발생한다.
숫자_한글 또는 숫자+영어 를 사용하면 잘 된다.
```

```
#error명
Filter Error ASCII-8BIT to UTF-8

#해결
input {
  jdbc {
    columns_charset => {
      "some_field" => "BINARY"
      "another_field" => "UTF-8"
    }
    # ...
  }
}
#설명
binary로 된 data를 인덱싱할 때 발생한 오류다.
해결방안처럼 columns_charset 설정을 추가해 주면 오류 없이 인덱싱이 가능하다.
```

