# Logstash jdbc streaming

jdbc streaming과 dashboard 사용을 위한 test 진행

###### 진행 환경

- elasticsearch 8.3.2 version
- kibana 8.3.2 version
- logstash 8.3.2 version

###### 사용 data

- 서울시 상권 정보

###### 진행 순서

1. csv db에 import
2. logstash jdbc_streaming filter를 사용해서 es에 indexing
3. kibana dashboard를 사용해서 시각화



##### 1. data import

- jdbc streaming을 이용하기 위해 상권 정보 내 위,경도 column을 분리해서 따로 테이블 생성![image-20220929103716165](C:\Users\pop24\AppData\Roaming\Typora\typora-user-images\image-20220929103716165.png)



##### 2. jdbc streaming 사용해서 es에 indexing

```json
#store.conf(logstash)
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
  jdbc_streaming {
    jdbc_driver_library => "C:/Program Files (x86)/MySQL/Connector J 8.0/mysql-connector-java-8.0.28.jar"
    jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
    jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
    jdbc_connection_string => "jdbc:mysql://localhost:3306/store"
    jdbc_user => "root"
    jdbc_password => "595855"
	statement => "SELECT longitude,latitude FROM coordinate WHERE store_num = :num"
    #input의 query와 join할 key값 store_num을 num이라는 변수에 담아줌
    parameters => {"num" => "store_num"}
	#input과 filter query의 key값을 비교
    target => "location"
	#es안에서 query로 조회된 값을 넣을 field명 설정
  }
  mutate {
    rename => {"[location][0][latitude]" => "[location][0][lat]"}
    rename => {"[location][0][longitude]" => "[location][0][lon]"}
	convert => {"[location][0][lat]" => "float"}
	convert => {"[location][0][lon]" => "float"}
	#좌표 정보 사용을 위해 데이터 가공
    }
}
```

##### 2-1. 색인 결과

```json
      {
        "_index": "store_seoul",
        "_id": "Msn9goMBdT6qk95W-wCE",
        "_score": 1,
        "_source": {
          "mtype_code": "D10",
          "sido": "서울특별시",
          "store_branch": "",
          "zip_code": "7250",
          "jibun_juso": "서울특별시 영등포구 영등포동5가 41-1",
          "portal_code": "150035",
          "ltype": "소매",
          "mtype": "건강/미용식품",
          "industry": "건강보조식품 소매업",
          "ltype_code": "D",
          "industry_code": "G47216",
          "sigungu_code": 11560,
          "road_name": "서울특별시 영등포구 영중로14길",
          "@version": "1",
          "sigungu": "영등포구",
          "road_code": "1.15604E+11",
          "store_num": 23324279,
          "sido_code": 11,
          "stype": "건강원",
          "road_juso": "서울특별시 영등포구 영중로14길 11-17",
          "stype_code": "D10A07",
          "@timestamp": "2022-09-28T07:27:03.425403300Z",
          "store_name": "제중건강원",
          "location": [
            {
              "lat": 37.520599365234375,
              "lon": 126.90699768066406
            }
          ]
        }
      },
```

##### 3. 시각화 페이지

- 상단의 filter에 조건을 넣어서 원하는 정보만 시각화 가능

![image-20220929111743411](C:\Users\pop24\AppData\Roaming\Typora\typora-user-images\image-20220929111743411.png)

- 강남구,한식/백반/한정식으로 필터를 적용했을 때 화면

![image-20220929131201068](C:\Users\pop24\AppData\Roaming\Typora\typora-user-images\image-20220929131201068.png)