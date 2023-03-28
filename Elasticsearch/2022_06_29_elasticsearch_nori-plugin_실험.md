# elasticsearch nori-plugin 실험



### 1. 문제

사용자 사전 구성시 복합어가 많았음. 사용자 사전에 명시된 단어들은 우선순위가 높아서 해당 단어가 token으로 추출되기 때문에 어떻게 구성하냐에 따라 token이 상이할 것으로 예상됨.

```
1. nori에서 복합어의 tokenize 단위를 결정하기 위한 decompound_mode 옵션을 조정
2. 사용자 사전에서 복합어와 단순명사의 포함을 조절
```

### 2. 시도

###### 조건 1. nori_pos 에 stop tag를 사용하여 명사만 tokenize 하도록 설정

#### 1. 복합어를 포함하고 decompound_mode 조정

```bash
#사전 list
강남역
삼성전자
부서장
보물찾기
대학수학능력시험
세종문화회관
서울대학교
북핵실험
한미동맹
공백문자
```

```
PUT test_nori
{
    "settings": {
    "index": { "max_ngram_diff": 4 },
    "analysis": {
      "analyzer": {
        "nori_analyzer": {
          "tokenizer": "nori_to",
          "filter": ["pos"]
        }
      },
      "tokenizer": {
        "nori_to": {
          "type": "nori_tokenizer",
          "decompound_mode": "{{mode_name}}",
          "user_dictionary": "news/dict_kor_2.txt"
        }
      },
      "filter": {
        "pos": {
          "type": "nori_part_of_speech",
          "stoptags":  ["E","IC","J","MAG","MAJ",
                      "MM","NA","NP","SC","SE",
                      "SF","SP","SSC","SSO","SY",
                      "UNA","UNKNOWN","VA","VCN",
                      "VCP","VSV","VV","VX","XPN",
                      "XR","XSA","XSN","XSV"]
        }
      }
    }
  }
}
```



##### 1. decompound_mode : none

```json
#query
GET test_nori/_analyze
{
  "analyzer": "nori_analyzer",
  "text" : "대학수학능력시험이 대학의 수학을 능력 시험 회사원 회사건물"
}

#result
{
  "tokens" : [
    {
      "token" : "대학수학능력시험",
		...
    },
    {
      "token" : "대학",
		...
    },
    {
      "token" : "수학",
		...
    },
    {
      "token" : "능력",
		...
    },
    {
      "token" : "시험",
		...
    },
    {
      "token" : "회사원",
		...
    },
    {
      "token" : "회사",
		...
    }, 
    {
      "token" : "건물",
	    ...
    }
  ]
}
#기존의 nori가 기본적인 단어들은 알아서 tokenize 해주기 때문에 none으로 설정했을 때 복합어만 사용해도 크게 무리가 없어보임
#사전에 없는 복합명사(명사+명사)를 검색할 경우 가장 작은 단어 단위로 tokenize 되기 때문에 검색에 유의해야함
```

##### 2. decompound_mode : discard

```json
#query
GET test_nori/_analyze
{
  "analyzer": "nori_analyzer",
  "text" : "대학수학능력시험이 대학의 수학을 능력 시험 회사원 회사건물"
}

#result
{
  "tokens" : [
    {
      "token" : "대학수학능력시험",
		...
    },
    {
      "token" : "대학",
		...
    },
    {
      "token" : "수학",
		...
    },
    {
      "token" : "능력",
		...
    },
    {
      "token" : "시험",
		...
    },
    {
      "token" : "회사",
		...
    },
    {
      "token" : "원",
		...
    },
    {
      "token" : "회사",
		...
    }, 
    {
      "token" : "건물",
	    ...
    }
  ]
}
#사용자 사전에 복합명사를 동일하게 저장했기 때문에 동일한 결과가 나온다.
#mode가 달라지면서 하나 다르게 나오는 부분은, "회사원"을 ["회사","원"]으로 tokenize 한다는 것이다.
=> none은 합성어를 분리하지 않는 반면, discard는 합성어를 분리한다.
```

##### 3. decompound_mode : mixed

```json
#query
GET test_nori/_analyze
{
  "analyzer": "nori_analyzer",
  "text" : "대학수학능력시험이 대학의 수학을 능력 시험 회사원 회사건물"
}

#result
{
  "tokens" : [
    {
      "token" : "대학수학능력시험",
		...
    },
    {
      "token" : "대학",
		...
    },
    {
      "token" : "수학",
		 ...
    },
    {
      "token" : "능력",
		 ...
    },
    {
      "token" : "시험",
		...
    },
    {
      "token" : "회사원",
		...
    },
    {
      "token" : "회사",
		...
    },
    {
      "token" : "원",
		...
    },
    {
      "token" : "회사",
		...
    },
    {
      "token" : "건물",
		...
    },
    {
      "token" : "조별",
		...
    },
    {
      "token" : "과제",
		...
    },
    {
      "token" : "세계",
		...
    },
    {
      "token" : "여행",
		...
    }
  ]
}
#사전에 있는 복합 명사(명사+명사)는 사전에 명시된 단어 그대로 tokenize 된다. 
#사전에 없는 복합 명사(명사+명사)는 각각의 명사만 tokenize하는 반면, 합성어는 단어를 분리하여 각각의 어근과 전체 단어까지 tokenize한다.
=> ["회사원"] => ["회사원","회사","원"], ["세계여행"] => ["세계","여행"]
=>
```

#### 2. 어근과 복합명사 모두를 포함하고 decompound_mode 조정

```
#사전 list
강남
역
삼성
전자
...
강남역
삼성전자
부서장
보물찾기
대학수학능력시험
세종문화회관
서울대학교
북핵실험
한미동맹
공백문자
```

사용자 사전에 어근과 복합명사,합성어가 중복되어 있다면, nori는 사전에 명시된 내용을 우선순위로 하여 tokenize 한다. 예를 들어 사용자 사전에 ["대학수학능력시험","회사원","대학","수학","능력","시험","회사","원"] 을 명시해 둔다면, 분명히 사용자 사전에 어근이 함께 있음에도 불구하고 명시된 원형 그대로 ["대학수학능력시험","회사원"] 와 같은 token을 생성하게 된다.(사용자사전에 명시해두지 않으면, ["대학","수학","능력","시험","회사","원"]의 형태로 tokenize하게 된다.) 

##### *대체적으로 어근과 합성어는 nori에서 tokenize를 잘 해주는 편이기 때문에  필요한 복합명사를 사용자 사전에 추가해 두는 것이 필요하다고 보임* 

#### 3. 어근만 포함하고 decompound_mode 조정

```
#사전 list
강남
역
삼성
전자
부서
장
보물
찾기
대학
수학
능력
시험
세종
문화
회관
서울
대학교
북핵
실험
한미
동맹
공백
문자
```

##### 1. decompound_mode : discard

```json
#query
GET test_nori9/_analyze
{
  "analyzer": "nori_analyzer",
  "text" : "대학수학능력시험이 대학의 수학을 능력 시험 회사원 회사건물 조별과제 세계여행"
}

#result
{
  "tokens" : [
    {
      "token" : "대학",
      ...
    },
    {
      "token" : "수학",
      ...
    },
    {
      "token" : "능력",
      ...
    },
    {
      "token" : "시험",
      ...
    },
    {
      "token" : "대학",
      ...
    },
    {
      "token" : "수학",
      ...
    },
    {
      "token" : "능력",
      ...
    },
    {
      "token" : "시험",
      ...
    },
    {
      "token" : "회사",
      ...
    },
    {
      "token" : "원",
      ...
    },
    {
      "token" : "회사",
      ...
    },
    {
      "token" : "건물",
      "...
    },
    {
      "token" : "조별",
      ...
    },
    {
      "token" : "과제",
      ...
    },
    {
      "token" : "세계",
      ...
    },
    {
      "token" : "여행",
      ...
    }
  ]
}

```

##### 2. decompound_mode: none

```json
#query
GET test_nori9/_analyze
{
  "analyzer": "nori_analyzer",
  "text" : "대학수학능력시험이 대학의 수학을 능력 시험 회사원 회사건물 조별과제 세계여행"
}

#result
{
  "tokens" : [
    {
      "token" : "대학",
      ...
    },
    {
      "token" : "수학",
      ...
    },
    {
      "token" : "능력",
      ...
    },
    {
      "token" : "시험",
      ...
    },
    {
      "token" : "대학",
      ...
    },
    {
      "token" : "수학",
      ...
    },
    {
      "token" : "능력",
      ...
    },
    {
      "token" : "시험",
      ...
    },
    {
      "token" : "회사원",
      ...
    },
    {
      "token" : "회사",
      ...
    },
    {
      "token" : "건물",
      "...
    },
    {
      "token" : "조별",
      ...
    },
    {
      "token" : "과제",
      ...
    },
    {
      "token" : "세계",
      ...
    },
    {
      "token" : "여행",
      ...
    }
  ]
}

```

사용자 사전에 어근만 사용했을 경우는 none과 discard의 차이 말고는 큰 차이가 없다.

### 3. 결론

- 어근의 경우 nori 자체의 사전을 기반으로 tokenize 해줌. 따라서 nori의 사전과 사용자 사전을 비교하여 중복값을 제외하고 필요한 어근만 두는것이 좋을 것 같음.

- 복합명사(명사+명사)의 경우 사용자 사전에 없는 단어라면 무조건 어근 단위로 tokenize 하게 됨. 통상적으로 붙여서 사용하나, 실제로는 두 명사 사이에 띄어쓰기가 포함되어 있기 때문. 

- 복합명사 전체가 token이 되어야 하는 경우라면 사용자 사전에 명시해 두는것이 필요. 

- 합성어( ex) "회사원" -> "회사"+"원")의 경우 복합명사와 조금 다름. 파생어는 nori의 decompound_mode를 discard로 설정했을 경우에만 분리 되므로 사용자 사전에 명시하지 않아도 될 것으로 보임.

