#람다 식 : lambda - 교재 pp123
# lambda : 실행 시(런타임) 생성해서 사용할 수 있는 익명 함수
# 익명함수 : 이름이 없는 함수
# 입력과 출력이 있는 간단한 한 행짜리 함수를 만들 때 사용
# 같은 함수를  def  문으로 정의할 때보다 간결
# 형식 : lambda  매개변수 : 표현식(lambda  매개변수 : 리턴값)

##두개의 정수를 인수로 입력 받아 더한 결과를 출력하는 함수
#함수명 : add(a,b)

def add(a,b):
    return a + b

print((lambda a,b:a+b)(3,56)) #위의 add함수와 같은 기능

a = (lambda a,b:a+b)
print(a(3,3)) #lambda를 변수에 할당하여 사용하는것도 가능하다.
