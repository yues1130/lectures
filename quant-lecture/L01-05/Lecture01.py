# Lecture 01

# 1. 데이터 타입에 대한 이해
# 숫자형: integer, float 등 숫자 형태의 데이터 타입
# int 정수형
# type() 함수는 데이터 타입을 확인

2 + 1
2 - 1
2 * 3
6 / 2

3 ** 2 # 제곱
7 // 3 # 나눗셈의 몫
7 % 3 # 나눗셈의 나머지


# 문자형 (string)
# 문자형 만들기 4가지
# " " / ' ' 
# """ """ / ''' ''' : 줄 바꿈 유지


# f-string 포매팅
# 문자열에서 특정 부분만 바뀌고 나머지는 일정할 경우 사용
name = '유의상'
birth = '1988'

# f-string 형태: f'문자열 {변수} 문자열'
var = f'나의 이름은 {name}이며, {birth}년에 태어났습니다.' 

# 문자 바꾸기: replace() 함수
var.replace(' ', '_')

# split() 메서드로 값을 기준으로 문자열 나누기
var.split(' ')


# 인덱싱: 문자열 중 특정 위치의 값을 가져옴
# 슬라이싱: 범위에 해당하는 문자열을 가져옴
var = 'Quant'
var[2] # 앞에서 2번째 글자 반환
var[-2] # 뒤에서 2번째 글자 반환
var[0 : 3] # 시작과 마지막 범위 지정해 글자 반환 (마지막 번호는 포함 X)
var[:2] # 처음부터
var[3:] # 끝까지

# 2. 데이터 자료형
# 1) 리스트
a = [] # 리스트는 대괄호[]로 정의
type(a)

list_num = [1,2,3]
list_char = ['a','b','c']

list_nest = [1, 2, ['a', 'b']] # 리스트에는 어떠한 자료형도 들어올 수 있음

# 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]

a + b
a * 3

# 새로운 데이터 추가 / 삽입
var = [1, 2, 3]
var.append(4)

var = [1, 2, 3]
var.append([4,5]) # 중첩된 list 형태로 추가

# 확장 형태로 입력
var = [1, 2, 3]
var.extend([4,5])

# 리스트 값의 수정 / 삭제
var = [1, 2, 3, 4, 5]
var[2] = 10

var[3] = ['a','b','c']

var[0 : 2] = ['가', '나']

var = [1, 2, 3]
del var[0]


var = [1, 2, 3]
var[0 : 1] = []


# remove(x) 메서드; 첫번째로 나오는 x 값 제거
var = [1, 2, 3, 1, 2, 3]
var.remove(1)

var = [1, 2, 3]
var.pop() # 가장 마지막 데이터 출력 후 원래 데이터에서 삭제

# 정렬
var = [2, 4, 1, 3]
var.sort()

# 2) 튜플: 
# 리스트와 마찬가지로 중첩해 사용 가능
# 소괄호()로 정의
# 수정하거나 삭제 불가
var = ()
type(var)


# 값이 하나일 때에는 컴마(,) 넣을 것
var = (1) 
type(var)
var = (1,)
type(var)


var = (1, 2, ('a', 'b'))
del var[0] # error

# indexing & slicing
var = (1, 2, 3, 4, 5)
var[0]
var[0:3]

# 3) dictionary
# 대응 관계를 나타내는 자료형
# 리스트나 dictionary와 달리 순서가 존재하지 않고 대신 key와 value가 존재
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}
# key-value의 형태로 이루어져 있고 각각은 쉼표(,)로 구분

var = {'key1' : 1, 'key2' : 2}

var = {'key1' : [1, 2, 3], 'key2' : ('a', 'b', 'c')}

var = {'key1' : 1, 'key2' : 2, 'key3' : 3 }
var[0] # error
var['key1']

var = {'key1' : 1, 'key2' : 2}
var['key3'] = 3
var

# 삭제
del var['key3']

# key와 value를 한 번에 구하는 법
var.keys() # key값 반환
list(var.keys()) # 리스트로 반환

var.values() # values 반환
list(var.values())

# 4) 집합 (set)
# 집합에 관련된 자료형. set()를 사용해 만듦
# 중복 허용하지 않고 순서 없음
set1 = set([1, 2, 3])
set2 = set('banana') # 중복을 허용하지 않고 순서가 없음


s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5, 6])

s1.union(s2) # 합집합
s1.intersection(s2) # 교집합
s1.difference(s2) # 차집합

# 5) 불리언 / 불 자료형
# 참 / 거짓을 나타내는 자료형. 이 두 가지 값만 가질 수 있음
var = True
type(var)

1 == 1

1 != 1 # 다른지를 확인하는 비교연산자


bool(0)
bool(1)
bool(2)

# 값이 비어 있으면 False
bool(None)
bool("")
bool([])
bool({})
bool(())

# 값이 있으면 True
bool('a')
bool([1,2,3])
bool({'key':'value'})
bool((1,2))

# 6) 날짜와 시간
# 파이썬의 기본 자료형은 아님
# datetime 패키지를 사용
import datetime

var = datetime.datetime.now()
var
type(var)

# 원하는 데이터 추출
var.year
var.month
var.day
var.minute
var.second
var.microsecond

var.weekday() # 0:월요일, 1:화요일, 2:수요일, 3:목요일, 4:금요일, 5:토요일, 7:일요일
var.date() # 날짜
var.time() # 시간

# 포맷 바꾸기
# strftime: 시간 정보 -> 문자열
# strptime: 문자열 -> 시간 정보
var.strftime('%Y-%m-%d') # 날짜 및 시간을 어떤 형식의 문자열로 만들지 결정하는 형식 문자열


datetime.datetime.strptime("2022-12-31 11:59:59", "%Y-%m-%d %H:%M:%S")

# 날자 혹은 시간의 간격
dt1 = datetime.datetime(2022, 12, 31)
dt2 = datetime.datetime(2021, 12, 31)

dt1 - dt2 # 두 날짜의 차이

dt1 + datetime.timedelta(days = 1) # timedelta의 단점 날짜와 초 단위로만 됨

# 월단위 연산 시 dateutil 패키지의 relativedelta 클래스 이용
from dateutil.relativedelta import relativedelta
dt1 + relativedelta(months = 1)
