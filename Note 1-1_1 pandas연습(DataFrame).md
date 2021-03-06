# 데이터 프레임

![](./dataframe.png)


- Pandas 라이브러리에서 기본적으로 데이터를 다루는 단위는 DataFrame : spreadsheet와 같은 개념

- 이러한 형태의 데이터는 Structured Data 또는 Panel Data 또는 Tabular Data라고 부름

- pandas를 공부한다는 것은 결국 dataframe의 사용법을 익히고 활용하는 방법을 배운다는 것과 같다

- pandas를 잘 활용하면 대부분의 structured data를 자유자재로 다룰 수 있게 됨


### 데이터 프레임
- 2차원 행렬 데이터에 인덱스를 붙인 것
- 행과 열로 만들어지는 2차원 배열 구조
- R의 데이터 프레임 에서 유래
- 데이프레임의 각 열은 시리즈로 구성되어 있음 - 각 열의 데이터 타입은 동일해야 한다.
- DataFrame()함수를 사용해서 생성

![](./pandas_files.png)

## 데이터 프레임 생성

#### 리스트로 데이터 프레임 만들기

- DataFrame([[list1],[list2]]) 
- 각 list는 한 행으로 구성됨
- 행의 원소 개수가 다르면 None 값으로 저장



```python
import pandas as pd
import numpy as np
```


```python
#1차원 list를 이용해서 df를 생성 - 원소가 각 행으로 매핑
df = pd.DataFrame([1,2,3]) #list의 형태에 따라 데이터프레임의 형태가 달라진다
print(df)
#2차원 list를 이용해서 df를 생성 - 하위 list가 각 행으로 매핑
df = pd.DataFrame([[1,2,3],['a','b','c']])
df
```

       0
    0  1
    1  2
    2  3
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>b</td>
      <td>c</td>
    </tr>
  </tbody>
</table>
</div>




```python
#하위 list원소의 개수가 다른 경우 - None 값을 저장
df = pd.DataFrame([['a','c','b'],['a','b','c'],['a','b']])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>c</td>
      <td>b</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>b</td>
      <td>c</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>b</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>



### dict로 데이터 프레임 생성
- dict의 key값 -> column name
- dict item은 dateframe의 column으로 정의


```python
df1= pd.DataFrame({'A':[90,80,70],
                   'B':[85,98,75],
                   'C':[88,99,77],                   
                   'D':[87,89,86]},
                 index=['1위','2위','3위'])
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1위</th>
      <td>90</td>
      <td>85</td>
      <td>88</td>
      <td>87</td>
    </tr>
    <tr>
      <th>2위</th>
      <td>80</td>
      <td>98</td>
      <td>99</td>
      <td>89</td>
    </tr>
    <tr>
      <th>3위</th>
      <td>70</td>
      <td>75</td>
      <td>77</td>
      <td>86</td>
    </tr>
  </tbody>
</table>
</div>




```python
#df의 값을 위한 dict
data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2000002],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율":[0.0283, 0.0163, 0.0982,0.0141]
}

#열방향 인덱스(컬럼명) columns=
columns = ['지역','2015','2010','2005','2000','2010-2015 증가율']

#행방향 인덱스 index =
index=['서울','부산','인천','대구']
#pd.DataFrame(데이터,index=,columns)
df3 = pd.DataFrame(data,index=index,columns = columns)
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2010-2015 증가율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>0.0283</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>0.0163</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>0.0982</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2000002</td>
      <td>2456016</td>
      <td>2473990</td>
      <td>0.0141</td>
    </tr>
  </tbody>
</table>
</div>




```python
a = pd.Series([100, 200, 300], ['a', 'b', 'd'])
b = pd.Series([101, 201, 301], ['a', 'b', 'k'])
c = pd.Series([110, 210, 310], ['a', 'b', 'c'])

```

    [100, 200, 300]
    

# 시리즈로 데이터 프레임 생성
- pd.DataFrame(시리즈) : 시리즈를 열로 정의(1개의 시리즈만 전달 가능)
- pd.DataFrame([시리즈,시리즈,..]) : 여러 시리즈를 list로 묶어서 전달해야함
    - list원소 시리자 1개가 한 행으로 정의
    - 시리즈의 인덱스 => 컬럼명으로 만들어 진다


```python
print(pd.DataFrame(a))
pd.DataFrame([a]) #여러개의 시리즈를 리스트 형태로 넘겨주면 시리즈 하나가 하나의 열을 생성한다
```

         0
    a  100
    b  200
    d  300
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100</td>
      <td>200</td>
      <td>300</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame([a,b,c])

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>d</th>
      <th>k</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100.0</td>
      <td>200.0</td>
      <td>300.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>101.0</td>
      <td>201.0</td>
      <td>NaN</td>
      <td>301.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>110.0</td>
      <td>210.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>310.0</td>
    </tr>
  </tbody>
</table>
</div>



#### csv 데이터로 부터 Dataframe 생성
 - 데이터 분석을 위해, dataframe을 생성하는 가장 일반적인 방법
 - 데이터 소스로부터 추출된 csv(comma separated values) 파일로부터 생성
 - pandas.read_csv 함수 사용




```python
# data 출처: https://www.kaggle.com/hesh97/titanicdataset-traincsv/data
train_data = pd.read_csv('../data/train.csv')
print(train_data.shape)
train_data.head() #df의 처음 5행을 출력해준다
train_data.head(10) #df의 처음 10행을 출력해준다
train_data.tail()#df의 마지막 5행을 출력해준다
```

    (891, 12)
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>886</th>
      <td>887</td>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
      <td>male</td>
      <td>27.00</td>
      <td>0</td>
      <td>0</td>
      <td>211536</td>
      <td>13.00</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>female</td>
      <td>19.00</td>
      <td>0</td>
      <td>0</td>
      <td>112053</td>
      <td>30.00</td>
      <td>B42</td>
      <td>S</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>W./C. 6607</td>
      <td>23.45</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>889</th>
      <td>890</td>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
      <td>male</td>
      <td>26.00</td>
      <td>0</td>
      <td>0</td>
      <td>111369</td>
      <td>30.00</td>
      <td>C148</td>
      <td>C</td>
    </tr>
    <tr>
      <th>890</th>
      <td>891</td>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
      <td>male</td>
      <td>32.00</td>
      <td>0</td>
      <td>0</td>
      <td>370376</td>
      <td>7.75</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
  </tbody>
</table>
</div>




```python
train_data.info() #non-null count를 통해 결측값이 있는지 확인할 수 있다.
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 891 entries, 0 to 890
    Data columns (total 12 columns):
     #   Column       Non-Null Count  Dtype  
    ---  ------       --------------  -----  
     0   PassengerId  891 non-null    int64  
     1   Survived     891 non-null    int64  
     2   Pclass       891 non-null    int64  
     3   Name         891 non-null    object 
     4   Sex          891 non-null    object 
     5   Age          714 non-null    float64
     6   SibSp        891 non-null    int64  
     7   Parch        891 non-null    int64  
     8   Ticket       891 non-null    object 
     9   Fare         891 non-null    float64
     10  Cabin        204 non-null    object 
     11  Embarked     889 non-null    object 
    dtypes: float64(2), int64(5), object(5)
    memory usage: 83.7+ KB
    

#### read_csv 함수 파라미터
 - sep - 각 데이터 값을 구별하기 위한 구분자(separator) 설정 
 - header - header를 무시할 경우, None 설정
 - index_col - index로 사용할 column 설정
 - usecols - 실제로 dataframe에 로딩할 columns만 설정



```python
train_data = pd.read_csv('../data/train.csv',index_col = 'PassengerId',usecols=['PassengerId','Survived','Pclass','Name'])
train_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
    </tr>
    <tr>
      <th>PassengerId</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>887</th>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
    </tr>
    <tr>
      <th>888</th>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
    </tr>
    <tr>
      <th>889</th>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
    </tr>
    <tr>
      <th>890</th>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
    </tr>
    <tr>
      <th>891</th>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 3 columns</p>
</div>




```python
train_data.columns
```




    Index(['Survived', 'Pclass', 'Name'], dtype='object')




```python
train_data.index
```




    Int64Index([  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,
                ...
                882, 883, 884, 885, 886, 887, 888, 889, 890, 891],
               dtype='int64', name='PassengerId', length=891)



#### 인덱스와 컬럼의 이해

1. 인덱스(index)
 - index 속성
 - 각 아이템을 특정할 수 있는 고유의 값을 저장
 - 복잡한 데이터의 경우, 멀티 인덱스로 표현 가능
 
 
2. 컬럼(column)
 - columns 속성
 - 각각의 특성(feature)을 나타냄
 - 복잡한 데이터의 경우, 멀티 컬럼으로 표현 가능



```python
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2010-2015 증가율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>0.0283</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>0.0163</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>0.0982</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2000002</td>
      <td>2456016</td>
      <td>2473990</td>
      <td>0.0141</td>
    </tr>
  </tbody>
</table>
</div>




```python
#df의 컬럼명(열 인덱스) 확인 - columns 속성
df3.columns
```




    Index(['지역', '2015', '2010', '2005', '2000', '2010-2015 증가율'], dtype='object')




```python
#df 인덱스(행 인덱스) 확인 - index 속성을 확인
df3.index
```




    Index(['서울', '부산', '인천', '대구'], dtype='object')



#### 행/열 인덱스 이름 설정
- index.name
- colmns.name


```python
df3.index.name = '도시'
df3.columns.name = '특성'
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>특성</th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2010-2015 증가율</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>0.0283</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>0.0163</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>0.0982</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2000002</td>
      <td>2456016</td>
      <td>2473990</td>
      <td>0.0141</td>
    </tr>
  </tbody>
</table>
</div>




```python
#df프레임의 data값만 추출하려면 values 속성 사용
df3.values
```




    array([['수도권', 9904312, 9631482, 9762546, 9853972, 0.0283],
           ['경상권', 3448737, 3393191, 3512547, 3655437, 0.0163],
           ['수도권', 2890451, 2632035, 2517680, 2466338, 0.0982],
           ['경상권', 2466052, 2000002, 2456016, 2473990, 0.0141]], dtype=object)



###  dataframe 데이터 파악하기
 - shape 속성 (row, column)
 - describe 함수 - 숫자형 데이터의 통계치 계산
 - info 함수 - 데이터 타입, 각 아이템의 개수 등 출력



```python
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>특성</th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2010-2015 증가율</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>0.0283</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>0.0163</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>0.0982</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2000002</td>
      <td>2456016</td>
      <td>2473990</td>
      <td>0.0141</td>
    </tr>
  </tbody>
</table>
</div>




```python
#data 전체 양을 확인 - df.shape => (row,column)
df3.shape
```




    (4, 6)




```python
#Dataframe 개요정보 출력
df3.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 4 entries, 서울 to 대구
    Data columns (total 6 columns):
     #   Column         Non-Null Count  Dtype  
    ---  ------         --------------  -----  
     0   지역             4 non-null      object 
     1   2015           4 non-null      int64  
     2   2010           4 non-null      int64  
     3   2005           4 non-null      int64  
     4   2000           4 non-null      int64  
     5   2010-2015 증가율  4 non-null      float64
    dtypes: float64(1), int64(4), object(1)
    memory usage: 224.0+ bytes
    


```python
#판다스 실수 출력 형식 변경 코드
pd.options.display.float_format = '{:.2f}'.format # 일반 실수 표현
```


```python
#DataFrame의 기본 통계량 출력
df3.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>특성</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2010-2015 증가율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4.00</td>
      <td>4.00</td>
      <td>4.00</td>
      <td>4.00</td>
      <td>4.00</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>4677388.00</td>
      <td>4414177.50</td>
      <td>4562197.25</td>
      <td>4612434.25</td>
      <td>0.04</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3507775.58</td>
      <td>3524530.93</td>
      <td>3500544.86</td>
      <td>3538749.06</td>
      <td>0.04</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2466052.00</td>
      <td>2000002.00</td>
      <td>2456016.00</td>
      <td>2466338.00</td>
      <td>0.01</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2784351.25</td>
      <td>2474026.75</td>
      <td>2502264.00</td>
      <td>2472077.00</td>
      <td>0.02</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>3169594.00</td>
      <td>3012613.00</td>
      <td>3015113.50</td>
      <td>3064713.50</td>
      <td>0.02</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>5062630.75</td>
      <td>4952763.75</td>
      <td>5075046.75</td>
      <td>5205070.75</td>
      <td>0.05</td>
    </tr>
    <tr>
      <th>max</th>
      <td>9904312.00</td>
      <td>9631482.00</td>
      <td>9762546.00</td>
      <td>9853972.00</td>
      <td>0.10</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.reset_option('display.float_format') #기본 형태 출력 설정 변경 코드(지수 표현)
```


```python
train_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
    </tr>
    <tr>
      <th>PassengerId</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>887</th>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
    </tr>
    <tr>
      <th>888</th>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
    </tr>
    <tr>
      <th>889</th>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
    </tr>
    <tr>
      <th>890</th>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
    </tr>
    <tr>
      <th>891</th>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 3 columns</p>
</div>




```python
train_data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 891 entries, 1 to 891
    Data columns (total 3 columns):
     #   Column    Non-Null Count  Dtype 
    ---  ------    --------------  ----- 
     0   Survived  891 non-null    int64 
     1   Pclass    891 non-null    int64 
     2   Name      891 non-null    object
    dtypes: int64(2), object(1)
    memory usage: 27.8+ KB
    

### DataFrame 전치
- Pandas DataFrame은 전치를 포함해서 Numpy 2차원 배열에서 사용할 수 있는 속성이나 method를 대부분 지원함
- 전치 : 행과 열을 바꾸는 것
        - 관련 속성 : df.T


```python
# df3 전치 
df3.T['서울'] #dtype: object
```




    특성
    지역                   수도권
    2015             9904312
    2010             9631482
    2005             9762546
    2000             9853972
    2010-2015 증가율       0.03
    Name: 서울, dtype: object




```python
df3.T #원본데이터를 변경하진 않는다.
print(type(df3.T))
```

    <class 'pandas.core.frame.DataFrame'>
    


```python
df3.T.shape
```




    (6, 4)



### DataFrame 내용 변경 
- 열 추가 / 삭제 / 갱신


```python
#사용 예제
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>특성</th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2010-2015 증가율</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>0.03</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>0.02</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>0.10</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2000002</td>
      <td>2456016</td>
      <td>2473990</td>
      <td>0.01</td>
    </tr>
  </tbody>
</table>
</div>



### 해당열이 있으면 내용 갱신, 열이 없으면 추가
- 열추가 : df[열이름(key)]=values
- 열 내용 갱신 : df[열이름(key)]=values



```python
#내용 갱신
df3['2010-2015 증가율'] = df3['2010-2015 증가율'] * 100
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>특성</th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2010-2015 증가율</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>283.00</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>163.00</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>982.00</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2000002</td>
      <td>2456016</td>
      <td>2473990</td>
      <td>141.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
#새로운 열을 추가
df3['2005-2015 증가율'] = ((df3['2015']-df3['2005'])/df3['2005'] *100).round(2)
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>특성</th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2010-2015 증가율</th>
      <th>2005-2015 증가율</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>283.00</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>163.00</td>
      <td>-1.82</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>982.00</td>
      <td>14.81</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2000002</td>
      <td>2456016</td>
      <td>2473990</td>
      <td>141.00</td>
      <td>0.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
del df3['2010-2015 증가율']#원반 반영되기 때문에 두번 이상 실행하면 에러 발생함
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    E:\anaconda\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       3079             try:
    -> 3080                 return self._engine.get_loc(casted_key)
       3081             except KeyError as err:
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: '2010-2015 증가율'

    
    The above exception was the direct cause of the following exception:
    

    KeyError                                  Traceback (most recent call last)

    <ipython-input-105-cef96e65f1e0> in <module>
    ----> 1 del df3['2010-2015 증가율']
    

    E:\anaconda\lib\site-packages\pandas\core\generic.py in __delitem__(self, key)
       3964             # there was no match, this call should raise the appropriate
       3965             # exception:
    -> 3966             loc = self.axes[-1].get_loc(key)
       3967             self._mgr.idelete(loc)
       3968 
    

    E:\anaconda\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       3080                 return self._engine.get_loc(casted_key)
       3081             except KeyError as err:
    -> 3082                 raise KeyError(key) from err
       3083 
       3084         if tolerance is not None:
    

    KeyError: '2010-2015 증가율'



```python
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>특성</th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2005-2015 증가율</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>-1.82</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>14.81</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2000002</td>
      <td>2456016</td>
      <td>2473990</td>
      <td>0.41</td>
    </tr>
  </tbody>
</table>
</div>




### DataFrame의 기본 인덱싱
1. 열인덱싱
2. 인덱서를 사용하지않는 행 인덱싱
- []기호를 이용해서 인덱싱할때 주의점 : []기호는 열 위주 인덱싱이 원칙




```python
#사용예제
df3
```

### 1. 열인덱싱
1.열 라벨(컬럼명)을 키값으로 생각하고 인덱싱한다.
- 인덱스로 라벨값을 하나 넣으면 시리즈 객체가 반환
- 라벨의 배열이나 리스트를 넣으면 부분적 df 가 반환



```python
#인덱스로 라벨 값 1개 사용 - 열 위주 인덱싱
print(type(df3['지역']))
df3['지역'] #시리즈 형태로 반환
```

    <class 'pandas.core.series.Series'>
    




    도시
    서울    수도권
    부산    경상권
    인천    수도권
    대구    경상권
    Name: 지역, dtype: object




```python
#열 1개 접근할때는 .연산자 사용 가능
df3.지역 #시리즈 형태로 반환
```




    도시
    서울    수도권
    부산    경상권
    인천    수도권
    대구    경상권
    Name: 지역, dtype: object




```python
#열 추출할 때 dataframe으로 반환받고자 하면 컬럼명을 list형태로 사용
print(type(df3[['지역']]))
df3[['지역']]
```

    <class 'pandas.core.frame.DataFrame'>
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>특성</th>
      <th>지역</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
    </tr>
  </tbody>
</table>
</div>




```python
#여러개의 열을 추출 - [] list 사용
df3[['2010','2015']] #df반환
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>특성</th>
      <th>2010</th>
      <th>2015</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>9631482</td>
      <td>9904312</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>3393191</td>
      <td>3448737</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>2632035</td>
      <td>2890451</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>2000002</td>
      <td>2466052</td>
    </tr>
  </tbody>
</table>
</div>



### 판다스 데이터 프레임에 열이름(컬럼명)이 문자열일 경우에는
- 수치 인덱스를 사용할 수 없음
- 열 인덱싱 -  위치 인덱싱 기능을 사용할 수 없다. : keyerror 발생



```python
try:
    df3[0]
except:
    print('type')
```

    type
    

- 위치인덱싱 처럼 보이는 예제


```python
#np.arange(12).reshape(3,4)

np.arange(12).reshape(3,4) #np.adaray.reshape(행,열) - 요소의 배치를 변경
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])




```python
df5 = pd.DataFrame(np.arange(12).reshape(3,4))
df5
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
df5[[1,2]] #위치 인덱싱이 아닌 컬럼명이 숫자로 되어있는 df의 인덱싱
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df5[[0:3]] #슬라이싱 불가
```


      File "<ipython-input-134-0be15341c5be>", line 1
        df5[[0:3]]
              ^
    SyntaxError: invalid syntax
    


# 행 단위 인덱싱
- 행단위 인덱싱을 하고자 하면 인덱서라는 특수 기능을 사용하지 않는 경우 슬라이싱을 해야 함(인덱서는 바로 뒤에 배움)
- 인덱스 값이 문자(라벨)면 문자슬라이싱도 가능하다



```python
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>특성</th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2005-2015 증가율</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>-1.82</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>14.81</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2000002</td>
      <td>2456016</td>
      <td>2473990</td>
      <td>0.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 1행 추출 [:1] - 슬라이싱 사용
df3[:1]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>특성</th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2005-2015 증가율</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>1.45</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3[0:3] #시작위치 : 끝 위치 +1 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>특성</th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2005-2015 증가율</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>-1.82</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>14.81</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3['서울':'부산'] #행 인덱스 서울~부산 까지 추출
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>특성</th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2005-2015 증가율</th>
    </tr>
    <tr>
      <th>도시</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>-1.82</td>
    </tr>
  </tbody>
</table>
</div>



- 개별요소 접근[열][행]


```python
df3['2010']['인천']
```




    2632035




```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
