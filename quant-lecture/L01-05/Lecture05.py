# 1. 데이터 시각화
# 데이터 및 분석된 자료를 시각화해 훨씬 직관적으로 이해 가능
# 데이터 시각화에 matplotlib 혹은 pandas 패키지 사용
# 고급 시각화에는 seaborn 패키지 사용

# 출처: https://matplotlib.org
# 그래프의 구성 요소
# figure: 그림 전체
# axes: 그림 내부의 자표축 혹은 개별 그림
# line: 선 그래프에서 선 (line plot)
# markers: 점 그래프에서 점 (scatter plot)
# legend: 범례
# title: 제목
# grid: 격자
# spines: 윤곽선
# x/y axis label: x/y축 라벨
# major tick / major tick label: 메인 눈금, 메인 눈금 라벨
# minor tick / minor tick label: 서브 눈금, 서브 눈금 라벨

# 패키지의 함수들을 이용해 각각의 요소를 섬세하게 꾸미기 가능
# 하나의 figure 내에는 여러 개의 axes가 그려질 수 있음


# 1. matplotlib 패키지: python 표준 시각화 도구, 널리 사용
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')
df.head()

# scatter
plt.scatter(df['flipper_length_mm'],df['body_mass_g'])
plt.show()

# bar graph
df_group = df.groupby('species')['body_mass_g'].mean().reset_index() # 인덱스 초기화
plt.bar(df_group['species'],height=df_group['body_mass_g'])
plt.show()

# histogram
plt.hist(df['body_mass_g'])
plt.show()

plt.rc('font',family='Malgun Gothic') # matplotlib은 한글폰트 지원하지 않아 깨짐
plt.hist(df['body_mass_g'],bins=30)
plt.xlabel('Body mass')
plt.ylabel('Count')
plt.title('펭귄의 몸무게 분포')
plt.show()


# line graph
import pandas as pd
url = 'https://research.stlouisfed.org/fred2/series/UNRATE/downloaddata/UNRATE.csv' # 미국 실업자 데이터
df_unrate = pd.read_csv(url) # DATE열이 object 객체

df_unrate['DATE'] = pd.to_datetime(df_unrate['DATE']) # to_datetime() 함수를 사용하면 datetime 객체로 변환
plt.plot(df_unrate['DATE'],df_unrate['VALUE'])
plt.show()



# figure 내에 여러 axes 각각 다름
# matplotlib 사용 방법
# 1) stateless API (objected-based)
# 내가 지정한 figure, 내가 지정한 axes에 그림을 그리는 방법

# 2) stateful API (state-based)
# 현재의 figure, 현재의 axes에 그림을 그리는 방법

# stateless 방법은 figure와 axes를 직접 만들어야 하고, 이는 객체지향적 특징
# stateful 방법은 현재의 figure와 axes를 자동으로 찾아 그곳에 그래프를 나타냄
# 처음에는 stateless 방법만 존재했으나 더 편리한 사용을 위해 wrapper 모듈인 pyplot이 개발됨, 이를 통해 stateful 방법을 사용가능
# 간단하게 표현할 때에는 stateful 방법으로 충분. 보다 정교한 작업시 stateless 방법 사용


# 2. stateless API 방법으로 그래프 그리기: figure내에 원하는 만큼 axes 객체를 나눈 후, axes를 직접 지정하여 그래프를 표현하는 방법
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')

fig, axes = plt.subplots(2,1, figsize=(10,6)) # subplot을 통해 하나의 figure에 여러 개의 axes를 나눔
# (2,1)은 2행1열로 2개의 axes 객체를 만들라는 뜻
# figsize: figure의 가로 세로 길이 설정

axes[0].scatter(df['flipper_length_mm'],df['body_mass_g'])
axes[0].set_xlabel('날개 길이 (mm)')
axes[0].set_ylabel('몸무게 (g)')
axes[0].set_title('날개와 몸무게간의 관계')

axes[1].hist(df['body_mass_g'], bins=30)
axes[1].set_xlabel('Body Mass')
axes[1].set_ylabel('Count')
axes[1].set_title('펭귄의 몸무게 분포')


# subplots_adjust() 함수: subplot들의 여백/간격을 조정
plt.subplots_adjust(left=0.1,
                    right=0.95,
                    bottom=0.1,
                    top=0.95,
                    wspace=0.5,
                    hspace=0.5)

plt.show()


# 3. stateful API 방법: subplot()을 통해 현재 axes를 설정하면 axes를 입력 안해도 해당 axes에 그래프를 그림
plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
plt.scatter(df['flipper_length_mm'],df['body_mass_g'])
plt.xlabel('날개 길이 (mm)')
plt.ylabel('몸무게 (g)')
plt.title('날개와 몸무게간의 관계')

plt.subplot(2,1,2)
plt.hist(df['body_mass_g'], bins=30)
plt.xlabel('Body Mass')
plt.ylabel('Count')
plt.title('펭귄의 몸무게 분포')

plt.subplots_adjust(left=0.1,
                    right=0.95,
                    bottom=0.1,
                    top=0.95,
                    wspace=0.5,
                    hspace=0.5)

plt.show()

# 4. pands를 이용한 데이터 시각화
# pd 패키지는 mpl 패키지의 기능 일부를 내장. 시리즈 혹은 df 객체를 바로 그래프로 표현 가능
# line (선 그래프), bar (수직 막대 그래프), barh (수평 막대 그래프), hist (히스토그램)
# box (박스 플롯), kde(커널 밀도 그래프), area (면적 그래프), 
# pie (파이 그래프), scatter (산점도 그래프), hexbin (고밀도 산점도 그래프)
import seaborn as sns

df = sns.load_dataset('diamonds')

import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

# df.plot() -> df 객체를 그림으로 나타낸
df.plot.scatter(x='carat', y='price', figsize=(10,6), title='캐럿과 가격 간의 관계')
plt.show()

# cut별로 색을 다르게
df.plot.scatter(x='carat', y='price', c='cut', cmap='Set2') 
plt.show()

df['price'].plot.hist(bins=20)
plt.show()

# 데이터 분석과 시각화를 동시에
df.groupby('color')['carat'].mean().plot.bar()
plt.show()



# 5. seaborn을 이용한 데이터 시각화
# mpl보다 좀더 화려하고 복잡한 그래프를 표현 가능
import seaborn as sns
df = sns.load_dataset('titanic')

sns.scatterplot(data=df, x='age', y='fare',
                hue='class', style='class')
plt.show()

df_pivot = df.pivot_table(index='class',
                          columns='sex',
                          values='survived',
                          aggfunc='mean')
sns.heatmap(df_pivot, annot=True, cmap='coolwarm')
plt.show()



# 6. 표현 방법에 따라 사용하는 함수가 다름: figure-level과 axes-level 함수로 구성
# figure-level:
# matplotlib과 별개로 seaborn의 figure를 만들어 그곳에 그래프를 나타냄.
# 따라서, figure-level 함수 사용 시 facetgrid(seaborn의 figure)를 통해 레이아웃을 변경하고, 여러개의 그래프를 나타낼 수 있음
# replot (relational) / displot (distributions) / catplot (categorical)

# axes-level:
# matplotlib의 axes에 그래프를 나타냄
# scatterplot, lineplot (relational) / 
# histplot, kdeplot, ecdfplot, rugplot (distributions) / 
# stripplot, swarmplot, boxplot, violinplot, pointrplot, barplot (categorical)


# figure-level graph
import seaborn as sns
df = sns.load_dataset('titanic')
sns.displot(data=df, x='age', hue='class', kind='hist', alpha=0.3)

# class 별로 각각 개별 그래프로 표현
sns.displot(data=df, x='age', col='class', kind='hist')
sns.displot(data=df, x='age', row='class', kind='hist')
sns.displot(data=df, x='age', col='class', row='sex', kind='hist')

# axes-level grpah
# sns.histplot(data=df, x='age', col='class') # 오류 발생 -> axes-level 에서는 facetgrid를 할 수 없기 때문
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

g, axes = plt.subplots(2,1, figsize=(8,6))

sns.histplot(data=df, x='age', hue='class', ax=axes[0])
sns.barplot(data=df, x='class', y='age', ax=axes[1])

axes[0].set_title('클래스 별 나이 분포도')
axes[1].set_title('클래스 별 평균 나이')

g.tight_layout()

















