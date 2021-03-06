##지역변수 : 함수 내부에서 생성되어 함수가 종료되면 제거되는 변수
#함수 외부에서는 사용 불가능
def show():
    a = 1 #함수 내에서 정의된 지역변수
    a = a + 1
    print(a)

show() #2
#show(a) => error ; a는 함수 내에서 정의된 지역변수이므로 함수 외부에서는 실행되지 않는다.

def show1(b): #인수가 b에 저장되면서 지역변수 b가 생성됨
    b = b + 1
    print(b)

show1(20) #함수 호출 -> 인수 20을 들고 show1 함수로 이동해서 인수20을 매개변수에 저장
###########################################################################
##전역변수 : 함수 외부에서 정의된 변수
##프로그램 내 모든 곳에서 사용 가능
##함수 내에서 전역 변수 값을 변경하려면 global 키워드 사용

a = 1 #함수 밖에서 정의된 전역변수

def show():
    c = b + a #전역변수 a
    print(a)
    print(b)
    print(c)


def add():
    print(a)
    print(b)


b = 10 #함수 밖에서 정의된 전역변수 b
# print(c)#함수 외부에서 전역변수를 이용해서 실행할 때 실행전에 전역변수가 생성되어 있어야 한다


##전역변수의 특징 : 프로그램 내 어디서든 사용 가능하다
#전역변수가 정의된 위치는 함수 앞/뒤 상관없다
#함수 외부에서 전역변수를 이용해서 실행할 때 실행전에 전역변수가 생성되어 있어야 한다

###############################################################################
##전역변수를 함수 내부에서 변경하려면 global 키워드 사용
d = 1 #함수 밖에서 정의된 전역변수 d
def show2():
    global d
    d = d+1
    f = d+e
    # print(d)
    # print(e)
    # print(f)

e = 4
print('함수 호출 전 : ' ,d) #1
show2() #global d가 없으면 error 발생함
        #전역변수를 함수 내에서 조작하려 했기 때문
print('함수 1번 호출 : ' ,d) #2
show2()
print('gkatn 2번 호출 : ',d) #3

# 함수 실행이 거듭될 수록 d=d+1이 중첩 실행되어 d값이 증가한다