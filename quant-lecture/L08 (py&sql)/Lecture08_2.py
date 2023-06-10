
# 4. pandas를 이용한 SQL 데이터 읽기 & 쓰기
# 데이터 분석에 편한 df프레임이 아닌 tuple로 불러옴
# Pandas에는 SQL 데이터를 불러오거나 저장하는 함수 있음
import pandas as pd
from sqlalchemy import create_engine

# pandas에서 SQL 연결할 때에는 SQLalchemy ORM을 사용함
# ORM; Object Relational Mapping
# 어플리케이션과 데이터베이스를 연결할 때 SQL 언어가 아닌 어플리케이션 개발언어로 데이터베이스를 접근할 수 있게 해주는 툴
# 파이썬 코드를 SQL 쿼리로 자동변환해 SQL 쿼리 작성 필요 없이 파이썬 코드를 작성하는 것으로 DB 조작 가능

# engine = create_engine('mysql+pymysql://[사용자명]:[비밀번호]@[호스트:포트]/[사용할 데이터베이스]')
user = 'root'
passwd = 'j$wKHcr&Xm+WaM2$'
host = '127.0.0.1'
db = 'shop'
#charset = 'utf8'

#engine = create_engine('mysql+pymysql://root:j$wKHcr&Xm+WaM2$@127.0.0.1:3306/shop')
text_engine = f'mysql+pymysql://{user}:{passwd}@{host}:3306/{db}'
engine = create_engine(text_engine)

query = """select * from goods;"""
# real_sql(쿼리,연결정보) -> df 형태로 데이터 read
goods = pd.read_sql(query, con = engine)
engine.dispose() # 연결 종료


# 5. DF를 SQL DB에 저장; to_sql
import seaborn as sns
iris = sns.load_dataset('iris') # iris dataset 불러오기
iris.head()


engine = create_engine(text_engine)
iris.to_sql(name = 'iris',
            con=engine,
            index = False, # index 값까지 DB에 저장되지 않도록
            if_exists='replace') # 해당 table 존재 시 덮어씀
engine.dispose()


