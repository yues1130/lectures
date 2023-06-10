# 제어문
# 작성된 순서대로 실행되는 흐름을 제어하여 실행순서를 바꾸거나 여러번 반복하도록 함

# 1. if문
# if 조건:
#    실행 (조건 만족 시 실행)
x = 2
if x > 0:
    print("값이 0보다 큽니다")
    
# if 조건 1:
#    실행 1
# else 조건 2:
#    실행 2
# elif 조건 3:
#    실행 3
# ...
# else:
#    실행 n

if x >= 10:
    print("값이 10보다 큽니다")
elif x >= 0:
    print("값이 0 이상 10 미만입니다.")
else:
    print("값이 음수입니다.")
    
# 조건문이 if와 else로만 구성될 경우 간단하게 작성
# [조건문이 true인 경우] if 조건문 else [조건문이 false인 경우]
x = 7
'0 이상' if x >= 0 else '음수'


# 2. while문 / 반복문
# 조건을 만족하는 동안 반복

# while 조건:
#    실행

num = 1
while num < 5 :
    print(num)
    num = num + 1

# while 내 if
num = 1
while num < 10 :
    if num % 2 == 0 :
        print(f'{num}은 짝수입니다.')
    num = num + 1

# 특정 조건에서 중단 break
money = 1000
while True:
    money = money - 100
    print(f'잔액은 {money}입니다.')
    
    if money <= 0 :
        break

# 3. for문

# for 변수 in 리스트(또는 튜플, 문자열):
#    실행

var = [1, 2, 3]

for i in var :
    print(i)


var = [10, 15, 17, 20]
for i in var:
    if i % 2 ==0 :
        print(f'{i}는 짝수입니다.')
    else :
        print(f'{i}는 홀수입니다.')

# range 객체 생성

result = []
for i in range(10) :
    result.append(i**2)
print(result)


# 리스트 내포 문법을 쓰면 직관적 & 간결
# [실행 for 변수 in 리스트(또는 튜플, 문자열)]
result = [i**2 for i in range(10)]
print(result)


# 4. try-except문
# for문 중 오류 발생 시 다시 실행해야 해서 비효율적
# 오류 발생시 예외 처리 혹은 무시

# try:
#    expr (실행코드)
# except:    
#    error-handler-code (오류 발생 시 실행 코드)
# else:
#   running-code
# finally:
#    cleanup-code

number = [1, 2, 3, "4", 5]

for i in number:
    try:
        print(i**2)
    except:
        print(f'Error at: {i}')


# 5. 함수
# def f(x):
#    statement
#   return y

# 1) def 키워드로 함수임을 선언
# 2) f는 함수명
# 3) x는 함수에 들어가는 매개변수
# 4) 줄을 바꾼 후 들여쓰기
# 5) statement에 해당하는 코드가 실행
# 6) return 뒤에 적은 y가 반환

def sqrt(x):
    res = x**(1/2)
    return res
sqrt(4)


def multiply(x,y):
    res = x**y
    return res

multiply(x = 3, y = 4)
multiply(2, 3)


def divide(x, n=2): # default 값 설정
    res = x / n
    return res

divide(6)
divide(6,3)


# 람다를 통해 간단히 함수 만들 수 있음
# 함수명 = lambda 매개변수1, 매개변수2, ...: statement

divide_lam = lambda x, n: x/n

divide_lam(10,2)



# 6. 패키지
# 비슷한 기능을 모아둔 꾸러미
# 패키지 설치 -> 패키지 불러오기 -> 함수 사용
# ex) selenium (동적 크롤링에 사용) 설치


# 1) anaconda prompt 실행 -> pip install 패키지명 or conda install 패키지명

# 2) import 패키지명
# 간단히 -> import 패키지명 as 패키지별명
import pandas
import pandas as pd

# 3) 내용을 볼 때 -> dir(패키지명) or dir(패키지별명)

# 4) 자동으로 안 불러오와지는 하위 패키지는 수동으로 불러와야 함

import selenium
dir(selenium)

import selenium.webdriver
dir(selenium.webdriver)


import seaborn as sns
iris = sns.load_dataset('iris')


# 5) 특정 함수만 불러오기

# [from 패키지명 import 함수명]
from seaborn import load_dataset
load_dataset('iris')









