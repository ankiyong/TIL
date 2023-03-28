# Logstash elasticsearch filter

logstash의 elasticsaerch filter 사용법 소개

###### 진행 환경

- elasticsearch 8.3.2 version
- kibana 8.3.2 version
- logstash 8.3.2 version

###### 사용 data

- 서울시 상권 정보

###### 진행 순서

1. csv db에 import

2. logstash elasticsearch filter를 사용해서 es에 indexing

   

##### 1. data import

- jdbc streaming을 이용하기 위해 상권 정보 내 위,경도 column을 분리해서 따로 테이블 생성![image-20220929103716165](C:\Users\pop24\AppData\Roaming\Typora\typora-user-images\image-20220929103716165.png)



##### 2. elasticsearch filter 사용해서 es에 indexing

```json
#logstash config file
input {
  jdbc {
    jdbc_driver_library => "C:/Program Files (x86)/MySQL/Connector J 8.0/mysql-connector-java-8.0.28.jar"
    jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
    jdbc_connection_string => "jdbc:mysql://localhost:3306/store"
    jdbc_user => "root"
    jdbc_password => "595855"
	statement => "SELECT * FROM store_info_seoul"
    }
}


filter {
	elasticsearch {
		hosts => "localhost:9200"
		index => "geo_test1"
		query_template => "C:/elk/logstash-8.4.1/config/store.json"
        #enrich할 data를 찾기 위해 json 파일에 쿼리 작성
		fields => {"latitude" => "location1"}
		#enrich할 field와 새로 생성할 field를 매칭
		
	}
}

#store.json
{
	"query" : {
		"match" : { 
			"store_num" : "%{[store_num]}"
            #input의 query에서 검색할 keyword를 변수로 받아서 처리
		}
	}
}
```

##### 2-1. 색인 결과

```json
{
     "_index": "geo_test_re",
     "_id": "td3uh4MBdT6qk95Wq0Sl",
     "_score": 1,
     "_source": {
       "mtype": "양식",
       "road_code": "1.11403E+11",
       "portal_code": "100053",
       "@version": "1",
       "store_branch": "",
       "mtype_code": "Q06",
       "stype_code": "Q06A01",
       "ltype": "음식",
       "sigungu_code": 11140,
       "road_juso": "서울특별시 중구 퇴계로 114",
       "location1": 37.56050109863281,
       "industry": "서양식 음식점업",
       "sido": "서울특별시",
       "sigungu": "중구",
       "store_name": "루치다",
       "jibun_juso": "서울특별시 중구 회현동3가 1-10",
       "road_name": "서울특별시 중구 퇴계로",
       "sido_code": 11,
       "zip_code": "4631",
       "store_num": 8599830,
       "@timestamp": "2022-09-29T06:28:26.308189600Z",
       "industry_code": "I56114",
       "stype": "정통양식/경양식",
        "ltype_code": "Q"
     }
}
#store_num을 비교해서 같은 값을 가진 document의 latitude 값을 location1 필드에 담아서 enrich 된 것을 확인할 수 있다.
```

