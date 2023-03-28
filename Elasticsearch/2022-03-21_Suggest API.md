## 1.Suggest API

엘라스틱 서치는 도큐먼트 내에 존재하는 단어를 대상으로 비슷한 키어드를 변경해서 제시하는 교정 기능을 제공한다. suggest API를 이용하면 텀과 정ㄹ확히 일치하지 않는 단어도 자동으로 인식해서 처리할 수 있다.

```
Term suggest API : 추천 단어 제안
Completion suggest API : 자동완성 제안
Phrase suggest API : 추천 문장 제안
Context suggest API : 추천 문맥 제안
```

### 1.1 Term Suggest API

term suggest API는 편집 거리(edit distance)를 사용해 비슷한 단어를 제안한다.

*편집 거리 - 두 문자열 사이의 편집거리는 하나의 문자열을 다른 문자열로 바꾸는 데 필요한 편집 횟수를 말한다.*

먼저, 각각 동일한 필드에 다른 값을 가지는 도큐먼트를 여러개 생성한다.

```bash
PUT movie_term_suggest/_doc/1
{
  "movieNm" : "lover"
}
PUT movie_term_suggest/_doc/2
{
  "movieNm" : "Fall love"
}
PUT movie_term_suggest/_doc/3
{
  "movieNm" : "lovely"
}
PUT movie_term_suggest/_doc/4
{
  "movieNm" : "lovestory"
}
```

이후 suggest API를 사용해서 다른 단어를 검색해 보면 최대한 유사한 값을 검색해준다.

```bash
POST movie_term_suggest/_search
{
	"suggest" : {
		"spell-stggestion" : {
			"text" : "lave",
			"term" : {
				"field" : "movieNm"
			}
		}
	}
}
```

### 1.2 Completion Suggest API

자동완성 기능을 사용하기 위해서는 데이터 타입을 completion으로 설정해서 인덱스를 생성해야 한다. 

```bash
PUT movie_term_completion
{
	"mappings" : {
		"properties" : {
			"movieNm" : {
				"type" : "completion"
			}
		}
	}
}
```

생성된 인덱스에 문서를 추가한다.

```bash
PUT movie_term_completion/_doc/1
{
  "movieNmEnComple" : "After Love"
}
PUT movie_term_completion/_doc/2
{
  "movieNmEnComple" : "Lover"
}
PUT movie_term_completion/_doc/3
{
  "movieNmEnComple" : "Love for a mother"
}
PUT movie_term_completion/_doc/4
{
  "movieNmEnComple" : "Fall love"
}
PUT movie_term_completion/_doc/5
{
  "movieNmEnComple" : "My lovely wife"
}
```

suggest 옵션을 사용해서 검색해본다.

```bash
POST movie_term_completion/_search
{
	"suggest" : {
		"movie_completion" : {
			"prefix" : "l",
			"completion" : {
				"field" : "movieNm",
				"size" : 5				
			}
		}
	}
}
```

prefix 값을 l로 설정했기 때문에 l로 시작하는 필드가 검색되는 것을 확인할 수 있다.

