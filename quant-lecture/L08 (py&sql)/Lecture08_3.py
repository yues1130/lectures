# 6. upsert 기능 구현
# 시계열데이터의 특성
# 1) insert: 시간이 지남에 따라 데이터가 추가됨
# 2) upadate: 간혹 과거 데이터가 수정됨
# upsert: 입력하고자 하는 데이터 업데이트 or 추가하는 기능

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database

user = 'root'
passwd = 'j$wKHcr&Xm+WaM2$'
host = '127.0.0.1'
db = 'exam'

text_database = f'mysql+pymysql://{user}:{passwd}@{host}:3306/{db}'

create_database(text_database)

price = pd.DataFrame({
    "날짜": ['2021-01-02','2021-01-03'],
    "티커": ['000001','000001'],
    "종가": [1340, 1315],
    "거래량": [1000,2000]
    })

price

engine = create_engine(text_database) # engine 정보 생성
price.to_sql('price',con=engine,if_exists='append',index=False) # df이 sql에 저장
# if_exists = 'append': 테이블에 데이터가 존재할 경우 저장
engine.dispose()


# 6.1. 시계열 추가 시
new = pd.DataFrame({
    "날짜": ['2021-01-04'],
    "티커": ['000001'],
    "종가": [1320],
    "거래량": [1500]
    })

price = pd.concat([price, new])

engine = create_engine(text_database)
price.to_sql('price',con=engine,if_exists='append',index=False)
engine.dispose()


