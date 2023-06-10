# 데이터 분석: 데이터를 불러와 수정, 가공 후 분석하는 과정
# pandas 패키지: 1차원 배열인 시리즈 (series) / 2차원 배열인 데이터프레임 (DataFrame)으로 데이터 분석 처리

# 1. 시리즈
# 데이터가 순차적으로 나열된 1차원 배열
# 인덱스(Index)와 값(Value)은 1:1 관계 (딕셔너리와 비슷)

# 1) series 생성 (dictionary)
import pandas as pd

dict_data = {'a': 1, 'b': 2, 'c': 3}
series = pd.Series(dict_data)

print(series.index)
print(series.values)

# 2) series 생성 (list로 생성)
# 정수형 위치 인덱스가 자동 지정
list_data = ['a','b','c']
series = pd.Series(list_data)

series = pd.Series(list_data,
                   index = ['index1','index2','index3'])

# 3) indexing & slicing으로 원하는 원소 선택
capital = pd.Series({
    'Korea':'Seoul',
    'Japan':'Tokyo',
    'China':'Beijing',
    'India':'New Delhi',
    'Taiwan':'Taipei',
    'Singapore':'Singapore'
    })
print(capital)

print(capital['Korea']) # index명으로 선택
print(capital[['Korea','Taiwan']])
print(capital[0])
print(capital[[1,3]])

# series는 4칙 연산 가능
series_1 = pd.Series([1, 2, 3])
series_2 = pd.Series([4, 5, 6])

print(series_1 + series_2)
print(series_1 * 2)


# 2. DataFrame
# series: 1차원 배열
# dataframe: 2차원 배열

# 1) dataframe 생성
# 여러개의 시리즈를 모아둔 것
# 원소의 개수가 동일한 1차원 배열이 여러개 필요
import pandas as pd

dict_data = {'col1': [1, 2, 3],
             'col2': [4, 5, 6],
             'col3': [7, 8, 9],}
df = pd.DataFrame(dict_data)

print(df)
type(df)

# list로 df만들면 list가 행으로 입력됨
# 행index와 열이름은 위치 인덱스 부여
df = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(df)

# 행 index와 열 이름 부여
df = pd.DataFrame([[1, 2, 3],[4, 5, 6],[7, 8, 9]],
                  index = ['index1', 'index2', 'index3'],
                  columns = ['col1', 'col2', 'col3'])

print(df)

# 행 index 변경
df.index = ['행 1','행 2','행 3']
print(df)

# 열 이름 변경
df.columns = ['열 1','열 2','열 3']
print(df)

# 원본 index 데이터 변경
df.rename(index={'행 1':'첫 번째 행'}, inplace=True)
print(df)

df.rename(columns={'열 1':'첫 번째 열'}, inplace=True)
print(df)


# 행/열의 삭제
# 행 삭제: DataFrame.drop(행 인덱스, axis=0)
# 열 삭제: DataFrame.drop(열 이름, axis=1)
df.drop('행 3', axis=0, inplace=True)
df.drop('열 3', axis=1, inplace=True)
print(df)


# 행/열의 선택
dict_data = {'col1':[1, 2, 3, 4],
             'col2':[5, 6, 7, 8],
             'col3':[9, 10, 11, 12],
             'col4':[13, 14, 15, 16]}
df = pd.DataFrame(dict_data, index=['index1','index2','index3','index4'])
print(df)

# 열을 하나만 선택: 
   
# DataFrame['열 이름']
df['col1']
# DataFrame.열 이름 (열 이름이 문자열인 경우에만 가능)
df.col1 

type(df['col1']) # series 객체로 반환 [] 1번
type(df[['col1']]) # df 객체로 반환 [] 2번

df[['col1','col2']]

# 행 선택
# loc & iloc
# loc: 인덱스 이름을 기준으로 행 선택, 범위 끝 포함
# iloc: 위치 인덱스를 기준으로 행 선택, 범위 끝 제외
# 시리즈 객체 반환
df.loc['index1']
df.iloc[0]

# df로 반환 -> 이중 []
df.loc[['index1']]
df.iloc[[0]]

# slicing
df.loc['index1':'index3'] # loc은 범위의 끝을 포함
df.iloc[0:2] # iloc은 범위의 끝을 제외

# 데이터 선택
# DataFrame.loc['행 인덱스', '열 이름']
# DataFrame.iloc[행 위치, 열 위치]
# indexing / slicing으로 원소 선택
df.loc['index1','col1']
df.loc[['index1','index3'],['col1','col4']]
df.loc['index1':'index2','col1':'col3']

df.iloc[0, 0]
df.iloc[[0, 2], [0, 3]]
df.iloc[0:2, 0:3]


# 3. 데이터 불러오기 & 저장하기
# 파일포맷 불러오기 저장하기
# CSV read_csv() to_csv()
# EXCEL read_excel() to_excel()
# SQL read_sql() to_sql()
# HTML read_html() to_html()
# JSON read_json() to_json()
#HDF5 read_hdf() to_hdf()
import pandas as pd
url = 'https://raw.githubusercontent.com/hyunyulhenry/quant_py/main/kospi.csv'
data_csv = pd.read_csv(url)
data_csv.to_csv('data.csv')

url = 'http://github.com/hyunyulhenry/quant_py/raw/main/kospi.xlsx'
data_excel = pd.read_excel(url, sheet_name='kospi')
data_excel.to_excel('data.xlsx')


# 4. 데이터 요약 및 통계값 계산
# 데이터 맨 위와 맨 아래 일부 확인
# 맨 위: DataFrame.head(n)
# 맨 아래: DataFrame.tail(n)
# n 입력하지 않으면 기본값 5개 행 보여줌
import seaborn as sns
df = sns.load_dataset('titanic')
df.head()
df.tail()

df.shape # 크기 확인 (튜플 형태)
df.info() # 기본 정보 확인
# non-null count -> null 데이터가 아닌 데이터의 수

df['sex'].value_counts() # value_counts() 메서드: 열의 고유값 개수 계산
df[['sex','survived']].value_counts() # 다중 열을 기준으로도 메서드 적용 가능
df[['sex','survived']].value_counts(normalize=True) # 비율로 환산
df[['sex','survived']].value_counts(normalize=True).sort_index() # 인덱스 정렬

df['survived'].mean() # 평균 (0은 사망, 1은 생존)
df[['survived','age']].mean() # 여러 열의 평균

df['fare'].min() # 최소값
df['fare'].max() # 최대값
df['fare'].median() # 중간값
# NaN: Not a number의 약자. 결측치/누락값. 데이터 입력 시 빠지거나 소실된 값
# 결측치 많으면 데이터 품질 떨어지고 제대로된 분석 X

# 5. 결측치 처리하기
# 결측치 찾기
# isnull(): 결측치면 True, 유효한 데이터면 False 반환
# notnull(): 유효한 데이터면 True, 결측치면 False 반환
df.info()
df.head().isnull()
df.head().notnull()

# dropna() 메서드: 결측치가 있는 모든 행 삭제
df.dropna()
df.dropna(subset=['age'], axis=0) # 특정 열에서 결측치 있는 행만 삭제

# dropna(axis=1): 결측치가 있는 모든 열 삭제
df.dropna(axis=1)
df.info()

# 결측치가 n개 이상일 때 삭제하는 기준치 추가
df.dropna(axis=1, thresh=300) # 결측치가 300개 이상인 열을 삭제


# 데이터의 양이 줄어 편향되어 제대로된 분석 어려움
# 데이터의 결측을 특정 값으로 대체
# fillna: na를 채워라
df2 = df.copy()
df2.head(6)

mean_age = df2['age'].mean()
df2['age'].fillna(mean_age, inplace=True)
df2['age'].head(6)

# 서로 이웃한 데이터끼리는 유사성 있음. 특히, 시계열의 경우
# 바로 앞/뒤의 값으로 대체
# ffill: 결측치가 나타나기 전의 값으로 대체
df2['deck_ffill'] = df2['deck'].fillna(method='ffill')
# bfill: 결측치가 있는 경우 아래의 행 중 결측치가 아닌 첫번째 값으로 대체
df2['deck_bfill'] = df2['deck'].fillna(method='bfill')
df2[['deck','deck_ffill','deck_bfill']].head(12)


# 6. 인덱스 다루기 
import seaborn as sns
df = sns.load_dataset('mpg')
df.set_index('name', inplace=True) # set_index(): name열로 인덱스 설정
df.sort_index(inplace=True) # 오름차순 정렬
df.sort_index(inplace=True, ascending=False) # 내림차순 정렬

df.reset_index(inplace=True) # 인덱스 재설정 -> index에 다시 위치 인덱스 입력


# 7. 필터링
# series 또는 df에서 조건을 만족하는 원소만 추출
# boolean indexing 또는 isin 사용

# 1) boolean indexing: 시리즈 객체에 조건을 입력하면 각 원소에 참/거짓을 판별해 True/False로 이루어진 시리즈 반환
# 그 후 참에 해당하는 데이터만 선택해 조건을 만족하는 데이터만 추출
df['cylinders'].unique()

filter_bool = (df['cylinders'] == 4)
df.loc[filter_bool,] # 실린더 수 4 에 해당하는 데이터만 선택

filter_bool = (df['cylinders'] == 4) & (df['horsepower'] >= 100)
df.loc[filter_bool, ['cylinders', 'horsepower', 'name']] # 실린더 수 4 & 100 마력 이상, 보고싶은 열만

# 특정 이름의 데이터
filter_bool = (df['name'] == 'ford maverick') | (
    df['name'] == 'ford mustang ii') | (
        df['name'] == 'chevrolet impala')
df.loc[filter_bool]


# 2) isin (훨씬 간단)
filter_isin = df['name'].isin(['ford maverick','ford mustang ii','chevrolet impala'])
df.loc[filter_isin]


# 8. 새로운 열 만들기
# mpg: 연비, weight: 무게
# mpg/weight: 무게 대비 연비
# 시리즈 끼리는 연산 가능
df['ratio'] = df['mpg'] / df['weight'] * 100

# 특정 열의 조건으로 새로운 열 생성
# numpy패키지의 where()
import numpy as np
import pandas as pd
num = pd.Series([-2, -1, 1, 2])
np.where(num >= 0, '양수', '음수')

# horsepower 구분하는 열
df['horse_power_div'] = np.where(
    df['horsepower'] < 100, '100 미만',
    np.where((df['horsepower'] >= 100) & (df['horsepower'] < 200), '100 이상',
             np.where(df['horsepower'] >= 200, '200 이상', '기타')))

a = df['horse_power_div']





