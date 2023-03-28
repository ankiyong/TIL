# nori_analyzer 실험

복합어가 사용자 사전에 포함되어 있을 때 decompound mode에 따라 검색이 어떻게 되는지 실험

## 1. index 생성

3개의 decompound mode를 각각 적용한 analyzer를 생성하고 field에 적용해 줬다. 사용자 사전에는 사전에 있는 단어와  사전에 없는 명사의 결합으로 이뤄진 단어를 명시했다.

```json
PUT nori_test
{
  "settings": {
    "analysis": {
      "analyzer": {
        "nori_no" : {
          "tokenizer" : "nori_none",
          "filter": ["pos"]
        },
        "nori_di" : {
          "tokenizer" : "nori_dis",
          "filter": ["pos"]
        },
        "nori_mi" : {
          "tokenizer" : "nori_mix",
          "filter": ["pos"]
        }
      },
      "tokenizer": {
        "nori_none" : {
          "type" : "nori_tokenizer",
          "decompound_mode" : "none",
          "user_dictionary_rules" : ["풋사과 풋 사과","청사과 청 사과","대학수학능력시험 대학 수학 능력 시험","반부패비서관 반 부패 비서관","정부청사 정부 청사","정부정책 정부 정책"]
        },
       "nori_dis" : {
          "type" : "nori_tokenizer",
          "decompound_mode" : "discard",
          "user_dictionary_rules" : ["풋사과 풋 사과","청사과 청 사과","대학수학능력시험 대학 수학 능력 시험","반부패비서관 반 부패 비서관","정부청사 정부 청사","정부정책 정부 정책"]
        },
        "nori_mix" : {
          "type" : "nori_tokenizer",
          "decompound_mode" : "mixed",
          "user_dictionary_rules" : ["풋사과 풋 사과","청사과 청 사과","대학수학능력시험 대학 수학 능력 시험","반부패비서관 반 부패 비서관","정부청사 정부 청사","정부정책 정부 정책"]
        }
      },
      "filter" : {
        "pos" : {
          "type" : "nori_part_of_speech",
          "stoptags": ["E","IC","J","MAG","MAJ",
                      "MM","NA","NP","SC","SE",
                      "SF","SP","SSC","SSO","SY",
                      "UNA","UNKNOWN","VA","VCN",
                      "VCP","VSV", "VV","VX","XPN",
                      "XR","XSA","XSN","XSV"]
        }
      }
    }
  }, 
  "mappings" : {
    "properties": {
      "text_no" : {
        "type" : "text",
        "analyzer" : "nori_no"
      },
      "text_di" : {
        "type" : "text",
        "analyzer" : "nori_di"
      },
      "text_mi" : {
        "type" : "text",
        "analyzer" : "nori_mi"
      }
    }
  }
}
```

## 2. 색인

각각의 필드에 동일하게 사용자 사전에 명시된 단어들을 색인해 줬다.

```json
PUT nori_test/_doc/1
{
  "text_no" : "풋사과 청사과 대학수학능력시험 반부패비서관 정부청사 정부정책",
  "text_di" : "풋사과 청사과 대학수학능력시험 반부패비서관 정부청사 정부정책",
  "text_mi" : "풋사과 청사과 대학수학능력시험 반부패비서관 정부청사 정부정책"
}
```

