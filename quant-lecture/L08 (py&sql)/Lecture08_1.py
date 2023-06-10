# 파이썬과 SQL 연결
# 파이썬에서 SQL에 직접 연결 가능
# 파이썬에서 SQL DB에 접속해 데이터 가공 & 다시 DB에 저장 가능

# pymysql: 파이썬에서 SQL DB에 접속
# anaconda prompt에서 pymysql 설치
# conda install pymysql

# 1. SQL DB 연결
import pymysql

# 연결정보의 관리자
con = pymysql.connect(
    user = 'root' # 사용자명
    ,passwd = 'j$wKHcr&Xm+WaM2$' # 비밀번호
    ,host = '127.0.0.1' # 허용 접속 IP (일반적으로는 localhost는 127.0.0.1)
    ,db = 'shop' # 사용할 데이터베이스
    ,charset = 'utf8'# 인코딩 방법
    )

# cursor: 특정 위치, 특정 행을 가르킬 때 커서 사용
# 현재 작업중인 행을 나타내는 객체
mycursor = con.cursor() 



# 2. 데이터 불러오기
query = """
select * from goods;
"""

# execute() 메서드를 사용해 SQL 쿼리를 데이터베이스 서버에 보내 query 실행
mycursor.execute(query)
data = mycursor.fetchall() # 서버로부터 table의 모든 데이터를 받아옴
con.close() # 작업 후 데이터베이스와의 연결 종료



# 3. 데이터를 입력, 수정, 삭제 (DML 문장)
# Data Manipulation Language
con = pymysql.connect(
    user = 'root'
    ,passwd = 'j$wKHcr&Xm+WaM2$'
    ,host = '127.0.0.1'
    ,db = 'shop'
    ,charset = 'utf8'
    )
mycursor = con.cursor() 
query = """
    insert into goods (goods_id, goods_name, goods_classify, sell_price, buy_price, register_date)
    values('0009', '스테이플러', '사무용품', '2000', '1500', '2020-12-30');
"""

mycursor.execute(query)
con.commit() # DML 문장 실행시 commit을 해야 데이터의 확정 갱신하는 작업이 실행됨
data = mycursor.fetchall()
con.close() 


