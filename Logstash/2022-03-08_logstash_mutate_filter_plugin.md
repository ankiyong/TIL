### 1.logstash mutate filter plugin

#### 1. split 

지정한 문자열을 기준으로 문장을 나눠준다.

```bash
input {...}

filter {
  mutate {
    split {"field1" => ","}
  }

}

output {...}
```

#### 2. strip

지정한 필드의 좌우 공백을 제거한다.

```bash
input {...}

filter {
  mutate {
    sptrip ["field1"]
  }

}

output {...}
```

#### 3. covert 

해당 필드를 형변환한다.

```bash
input {...}

filter {
  mutate {
    convert => {
    "field1" => "integer"
    "field2" => "float"
  }
 }
}

output {...}
```

#### 4. copy

필드의 값을 복사한다.

```bash
input {...}

filter {
  mutate {
    copy => {
    "field" => "field1_copied"
    }
   }
}

output {...}
```

#### 5. gsub

정규식으로 일치하는 항목을 다른 문자열로 대체한다.

```bash
input {...}

filter {
  mutate {
    gsub => [
      "field1", "/","_"
    ]
   }
}

output {...}
```

#### 6.join

배열을 하나의 문자로 합친다.



#### 7.lowercase,uppercase

필드 내 문자열을 대/소 변환 한다.

```
input {...}

filter {
   mutate {
     lowercase =>["field1","field2"]
     uppercase => ["field3"]
   }
}

output {...}
```

#### 8. capitalize

첫 글자를 대문자화 하고 나머지는 소문자화 한다.

```
input {...}

filter {
   mutate {
     caplitalize => ['field1']
   }
}

output {...}
```

#### 9. merge

해당 필드 값을 다른 필드에 포함시킨다.

```bash
input {...}

filter {
   mutate {
     merge => {"field1"=>"field2"}
   }
}

output {...}
```

이해가 잘 안돼서 message => path로 실행시켜봤는데 

path를 message에 추가하고 이걸 배열로 반환하는 플러그인 같음

![merge](C:\Users\pop24\Documents\카카오톡 받은 파일\merge.png)

#### 10. coerce

필드 값이 null인 경우에 기본값을 넣어준다.

```
input {...}

filter {
   mutate {
     coerce => {"field2" => "empty"}
   }
}

output {...}
```

#### 11. rename 

해당 필드의 이름을 변경한다

```
input {...}

filter {
   mutate {
     rename => { "field1" => "field2"}
   }
}

output {...}
```

## 2. dissect plugin

mutate 플러그인의 split은 하나의 구분자만을 이용해 데이터를 다눠야하는 단점이 있다.

dissect 플러그인은 패턴을 이용해 문자열을 분석하고 주요 정보를 필드로 추출한다. 

```bash
ex) [2020-01-02 14:17] [ID1] 192.10.2.6 9500 [INFO] - connected.
input {...}

filter {
	dissect {
	mapping => {"field1" => "[%{time}] [%{ID}] %{IP} %{port} [%{lovel}] - %{message}."}
	}
}

output {...}


```

모든 필드의 문장 형태가 동일하다면 위의 설정처럼 하면 된다.

하지만 공백의 수가 다른 경우는 다음처럼 하면 된다. 

```bash
filter {
	dissect {
	mapping => {"field1" => "[%{time}]%{?->}[%{ID}] %{IP} %{port} [%{lovel}] - %{message}."}
	}
}
```

필드마다 공백이 서로 다른 지점에 %{?->}를 삽입하여 모든 공백이 몇칸이라도 하나의 공백으로 보고 문장 분리를 실행하게 된다.

## 3. grok plugin

grok플러그인은 정규 표현식을 통해 문자열을 파싱한다. 

자주 사용되는 패턴들은 정리되어있어 가져다 사용하면 된다. 

```bash
filter {
  grok {
    match => { "message" => "\[%{TIMESTAMP_ISO8601:timestamp}\] [ ]*\[%{DATA:id}\] %{IP:ip} %{NUMBER:port:int} \[%{LOGLEVEL:level}\] \- %{DATA:msg}\."}
  }
}
```

TIMESTAMP - ISO8601 표준 시간 표기법에 대한 패턴

DATA - 모든 데이터를 인식

IP - IPv4 형태의 데이터(192.192.192.192)를 인식

NUMBER - 숫자를 인식하는데 변수 뒤에 :int를 추가하면 정수 타입으로 지정된다.

LOGLEVEL - syslog 레벨을 인식한다 (warn,error 등)

[  ]* 은 dissect의 %{?->}과 같은 기능을 한다.

[  ,  ]  , - . 과 같은 기호를 사용할 떄는 \을 앞에 붙여줘야한다. 

TIMESTAMP같은 경우 기본 yyyy-mm-dd의 형식만 인식한다. 그래서 yyyy-mm-dd 같은 형식의 날짜는 인식하지 못하게 된다. 그럴떄는 pattern_definitions를 통해 패턴을 변경시켜준다. 
