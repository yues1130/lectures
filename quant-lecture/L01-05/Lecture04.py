# 1. 데이터프레임 합치기
# concat(), merge(), join()

# 1) concat(): 행/열 방향으로 데이터프레임을 이어 붙이는 개념
# 행기준 합치기
import pandas as pd

df1 = pd.DataFrame({
    "A": ["A0","A1","A2","A3"],
    "B": ["B0","B1","B2","B3"],
    "C": ["C0","C1","C2","C3"],
    "D": ["D0","D1","D2","D3"]
    }, index=[0, 1, 2, 3])

df2 = pd.DataFrame({
    "A": ["A4","A5","A6","A7"],
    "B": ["B4","B5","B6","B7"],
    "C": ["C4","C5","C6","C7"],
    "D": ["D4","D5","D6","D7"]
    }, index=[4, 5, 6, 7])

df3 = pd.DataFrame({
    "A": ["A8","A9","A10","A11"],
    "B": ["B8","B9","B10","B11"],
    "C": ["C8","C9","C10","C11"],
    "D": ["D8","D9","D10","D11"]
    }, index=[8, 9, 10, 11])

result = pd.concat([df1, df2, df3]) # 행 방향 합치기


df4 = pd.DataFrame({
    "B": ["B2","B3","B6","B7"],
    "D": ["D2","D3","D6","D7"],
    "F": ["F2","F3","F6","F7"]
    }, index=[2, 3, 6, 7])

result = pd.concat([df1, df4])
result = pd.concat([df1, df4], ignore_index=True) # index 초기화

# 열기준 합치기
result = pd.concat([df1, df4], axis=1) # 합칩합 합치기
result = pd.concat([df1, df4], axis=1, join='inner') # 교집합 합치기

# series 합치기

s1 = pd.Series(["X0", "X1", "X2", "X3"], name="X")
result = pd.concat([df1, s1], axis=1)

# 2) merge(): 기준이 되는 열이나 인덱스, 즉 key를 중심으로 두 df를 합침
# inner join: 양쪽 df에서 기준이 되는 열의 데이터가 모두 있는 교집합 부분만 반환

left = pd.DataFrame({
    "key": ["K0","K1","K2","K3"],
    "A": ["A0","A1","A2","A3"],
    "B": ["B0","B1","B2","B3"]
    })


right = pd.DataFrame({
    "key": ["K0","K1","K3","K4"],
    "C": ["C0","C1","C2","C3"],
    "D": ["D0","D1","D2","D3"]
    })

result = pd.merge(left, right, on="key") # 공통 key를 중심으로 교집합에 해당하는 행만 선택해 열방향으로 합침

# left join: 왼쪽 df는 유지, 오른쪽 df가 key를 기준으로 합쳐짐
result = pd.merge(left, right, on="key", how="left")

# right join: 오른쪽 df가 유지되고, 왼쪽 df이 키를 기준으로 합쳐짐
result = pd.merge(left, right, on="key", how="right")

# outer join: df중 어느 한쪽에만 속하더라도 상관없이 합집합부분을 반환
result = pd.merge(left, right, on="key", how="outer")



# 
# 왼쪽과 오른쪽에 기분이 되는 열 이름이 다를 수도 있음
left = pd.DataFrame({
    "key_left": ["K0","K1","K2","K3"],
    "A": ["A0","A1","A2","A3"],
    "B": ["B0","B1","B2","B3"]
    })

right = pd.DataFrame({
    "key_right": ["K0","K1","K3","K4"],
    "C": ["C0","C1","C2","C3"],
    "D": ["D0","D1","D2","D3"]
    })

result = pd.merge(left, right, 
                  left_on="key_left", right_on="key_right", 
                  how="inner")

# 같은 방식이지만 보다 더 직관적
result = left.merge(right, left_on="key_left", right_on="key_right", how="inner")



# 3) join(): merge함수를 기반으로 만들어져 사용 방법이 거의 비슷
# merge() 함수-> 키를 기준으로 결합
# join() 메서드 -> 행 인덱스를 기준으로 결합

left = pd.DataFrame({
    "A": ["A0","A1","A2","A3"],
    "B": ["B0","B1","B2","B3"]
    }, index=["K0","K1","K2","K3"])

right = pd.DataFrame({
    "C": ["C0","C1","C3","C4"],
    "D": ["D0","D1","D3","D4"]
    }, index=["K0","K1","K3","K4"])

result = left.join(right) # index를 기준으로 join


# 2. df 재구조화
# 행과 열구조 변형, 특정 요인에 따라 집계
# melt, pivot_table, stack, unstack
# melt: ID 변수를 기준으로 원본 df의 열 이름들을 variable 열에, 각 열에 있는 데이터는 value 열에 넣어 아래로 긴 형태로 만듦
import seaborn as sns
df = sns.load_dataset('penguins')

df.melt(id_vars=['species','island'])


# pivot_table: 엑셀의 피벗 테이블과 비슷
# 4개의 입력값 필요
# index: 행 인덱스
# columns: 열 인덱스
# values: 데이터 값
# aggfunc: 데이터 집계 함수, 값이 없으면 NaN

df_pivot_1 = df.pivot_table(index='species',
                            columns='island',
                            values='bill_length_mm',
                            aggfunc='mean')

# index, 데이터 값, 집계 함수를 여러개 입력 가능
df_pivot_2 = df.pivot_table(index=['species','sex'],
                            columns='island',
                            values=['bill_length_mm','flipper_length_mm'],
                            aggfunc=['mean','count'])

# stack: 열인덱스를 행인덱스로 변환
# unstack: 행인덱스를 열인덱스로 변환

df_pivot_3 = df.pivot_table(index=['species','sex'],
                            columns='island',
                            values='bill_length_mm',
                            aggfunc='mean')

df_pivot_4 = df_pivot_3.stack()
type(df_pivot_4) # type: series
type(df_pivot_4.to_frame()) # type: series -> df


df_pivot_5 = df_pivot_3.unstack()


# 3. df에 함수 적용
# apply() 메서드를 사용하면 series나 df의 개별원수에 함수 적용 가능
# series 객체에 apply()메서드를 적용하면 모든 원소를 함수에 적용하여 결과값을 반환
import numpy as np

bill_length_mm = df['bill_length_mm']
bill_length_mm.head()

bill_length_mm.apply(np.sqrt)

def mm_to_cm(num):
    return num / 10

bill_length_mm.apply(mm_to_cm)



# df에 apply() 메서드를 적용하면 모든 열 혹은 행을 하나씩 분리해 함수에 각 원소가 전달된 후 값이 변환

# 각 열에 적용
# DataFrame.apply(함수) 혹은
# DataFrame.apply(함수, axis=0)

# 각 행에 적용
# DataFrame.apply(함수, axis=1)

df_num = df[['bill_length_mm','bill_depth_mm',
             'flipper_length_mm','body_mass_g']]
df_num.apply(max, axis=0)
df_num.apply(max, axis=1)



# 4. 그룹 연산하기
# 그룹 연산: 데이터를 특정 기준에 따라 그룹으로 나눈 후 처리하는 과정
# 일반적으로 3단계로 구성
# 1) 분할 (split): 데이터를 특정 기준에 따라 분할
# 2) 적용 (apply): 데이터를 집계, 변환, 필터링하는 메서드 적용
# 3) 결합 (combine): 적용의 결과를 하나로 결합

# 펭귄 데이터를 species에 따라 분할
df_group = df.groupby(['species'])
df_group.head(2)

df_group.mean()

# group을 여러 기준으로 분할
df_group = df.groupby(['species','sex']).mean()


# 함수를 직접 만든 후 그룹 객체에 적용: agg() 메서드
def min_max(x):
    return x.max() - x.min()

df.groupby(['species'])['bill_length_mm'].agg(min_max)

# agg()메서드는 한번에 여러개의 집계 연산 처리 가능
df_2 = df.groupby(['species']).agg('max','min')

# 각열마다 다른 함수 적용
df_3 = df.groupby(['species']).agg({'bill_length_mm':['max','min'],
                                   'island':['count']})


# agg() 메섣, 이용 시 그룹 별로 연산을 위한 함수를 적용하고 연산 결과를 집계하여 반환
# 반대로 transfer 메서드를 이용 시 그룹 별로 함수를 적용하는 것은 동일하지만,
# 그 결과를 본래의 행/열 인덱스를 기준으로 반환
# 원본 데이터 프레임과 같은 형태로 변형하려 반환

df.groupby(['species'])['bill_length_mm'].agg('mean')
df.groupby(['species'])['bill_length_mm'].transform('mean')

# z-score: 각 데이터의 값이 평균으로 부터 얼마나 떨어져 있는지를 나타내는 수치
# 각 원소를 평균으로 빼고 표준편차로 나누어줌
def z_score(x):
    z = (x - x.mean()) / x.std()
    return(z)

df.groupby(['species'])['bill_length_mm'].transform(z_score)

df.groupby(['species'])['bill_length_mm'].apply(min)
df.groupby(['species'])['bill_length_mm'].apply(z_score)



# 5. 시계열 데이터 다루기
# 시계열 데이터: 시간을 기준으로 측정된 데이터
# 주가나 재무제표 등 투자에 쓰이는 대부분의 데이터
# pandasㅇ서는 문자열을 datetime 객체로 변환 가능

df = sns.load_dataset('taxis')
df.info()

df['pickup'] = pd.to_datetime(df['pickup'])
df['dropoff'] = pd.to_datetime(df['dropoff'])

df.info()

df['pickup'][0].year # 연도 데이터만 추출
df['pickup'][0].month
df['pickup'][0].day

# pickup열의 모든 데이터 중 데이터 추출
# dt 접근자를 사용해 datetime 타입의 열에 접근
df['pickup'].dt.month

df.sort_values('pickup', inplace=True)# 오름차순 정렬
df.reset_index(drop=True, inplace=True)# index 초기화

# 운행 시간 계산
# dt 형태는 열끼리 연산 가능
df['dropoff'] - df['pickup']
df.set_index('pickup', inplace=True)

df.loc['2019-02'] # 특정 시간의 데이터 출력
df.loc['2019-03-01']
df.loc['2019-03-01':'2019-03-02'] # slice: 특정 기간의 데이터 출력


# range() 함수로 숫자 리스트 만듦
# pandas의 date_range()함수를 통해 여러개 날짜의 배열 형태의 시계열 데이터 만들 수 있음
pd.date_range(start='2021-01-01',
              end='2021-12-31',
              freq='M') # 주기는 월

pd.date_range(start='2021-01-01',
              end='2021-01-31',
              freq='3D') # 주기는 3일



