
# 6.3. python으로 upsert
import pymysql
price = pd.DataFrame({
    "날짜": ['2021-01-04', '2021-01-04'],
    "티커": ['000001', '000002'],
    "종가": [1320, 1315],
    "거래량": [2100, 1500]
})

args = price.values.tolist()
con = pymysql.connect(
    user = 'root' # 사용자명
    ,passwd = 'j$wKHcr&Xm+WaM2$' # 비밀번호
    ,host = '127.0.0.1' # 허용 접속 IP (일반적으로는 localhost는 127.0.0.1)
    ,db = 'exam' # 사용할 데이터베이스
    ,charset = 'utf8'# 인코딩 방법
    )

query = """
    insert into price_2 (날짜, 티커, 종가, 거래량)
    values (%s,%s,%s,%s) as new
    on duplicate key update
    종가 = new.종가, 거래량=new.거래량;
"""

mycursor = con.cursor() # cursor() 메서드로 데이터베이스의 커서 객체 가져옴
mycursor.executemany(query,args) # execute() 메서드로 SQL 쿼리를 DB 서버로 보냄
con.commit()
con.close()


