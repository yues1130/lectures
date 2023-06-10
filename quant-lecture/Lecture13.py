# https://www.youtube.com/watch?v=HloktbVPGVA&list=WL&index=2&t=127s
import requests as rq
from bs4 import BeautifulSoup as bs

# 1. 최근 영업일 수집
url = 'https://finance.naver.com/sise/sise_deposit.nhn'
data = rq.get(url)
data_html = bs(data.content)
parse_day = data_html.select_one(
    'div.subtop_sise_graph2 > ul.subtop_chart_note > li > span.tah').text
import re
biz_day = re.findall('[0-9]+', parse_day)
biz_day = ''.join(biz_day)




# 2. 국내 주식 티커 데이터 크롤링
# 2.1. Kospi
import requests as rq
from io import BytesIO
import pandas as pd

gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
gen_otp_stk = {
    'mktId': 'STK' # Kospi:STL / Kosdaq:KSQ
    ,'trdDd': biz_day
    ,'money': 1
    ,'csvxls_isNo': 'false'
    ,'name': 'fileDown'
    ,'url': 'dbms/MDC/STAT/standard/MDCSTAT03901'
}
headers = {'Referer': 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader'}

otp_stk = rq.post(gen_otp_url, gen_otp_stk, headers=headers).text

down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
down_sector_stk = rq.post(down_url, {'code': otp_stk}, headers=headers)

sector_stk = pd.read_csv(BytesIO(down_sector_stk.content), encoding='EUC-KR')

# 2.2. Kosdaq
"""
import requests as rq
from io import BytesIO
import pandas as pd

gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
gen_otp_ksq = {
    'mktId': 'KSQ' # Kospi:STL / Kosdaq:KSQ
    ,'trdDd': biz_day
    ,'money': 1
    ,'csvxls_isNo': 'false'
    ,'name': 'fileDown'
    ,'url': 'dbms/MDC/STAT/standard/MDCSTAT03901'
}
headers = {'Referer': 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader'}

otp_ksq = rq.post(gen_otp_url, gen_otp_ksq, headers=headers).text

down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
down_sector_ksq = rq.post(down_url, {'code': otp_ksq}, headers=headers)

sector_ksq = pd.read_csv(BytesIO(down_sector_ksq.content), encoding='EUC-KR')
"""

gen_otp_ksq = gen_otp_stk
gen_otp_ksq['mktId'] = 'KSQ'

otp_ksq = rq.post(gen_otp_url, gen_otp_ksq, headers=headers).text
down_sector_ksq = rq.post(down_url, {'code': otp_ksq}, headers=headers)
sector_ksq = pd.read_csv(BytesIO(down_sector_ksq.content), encoding='EUC-KR')

# 2.3. Kospi + Kosdaq
krx_sector = pd.concat([sector_stk, sector_ksq]).reset_index(drop=True)
krx_sector['종목명'] = krx_sector['종목명'].str.strip() # 공백 제거
krx_sector['기준일'] = biz_day

#2.4. 개별종목 PER PBR 배당수익률

gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
gen_otp_data = {
    'searchType': '1'
    ,'mktId': 'ALL'
    ,'trdDd': biz_day
    ,'csvxls_isNo': 'false'
    ,'name': 'fileDown'
    ,'url': 'dbms/MDC/STAT/standard/MDCSTAT03501'
}
headers = {'Referer': 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader'}
otp = rq.post(gen_otp_url, gen_otp_data, headers=headers).text # Kospi Kosdaq 모두 받음

down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
krx_ind = rq.post(down_url, {'code': otp}, headers=headers)

krx_ind = pd.read_csv(BytesIO(krx_ind.content), encoding='EUC-KR')
krx_ind['종목명'] = krx_ind['종목명'].str.strip()
krx_ind['기준일'] = biz_day



# 3. 티커 데이터 클렌징
# 3.1. 하나의 데이터에만 존재하는 종목을 추림
# 일반적이지 않은 종목: 선박펀드, 광물펀드, 해외종목
set(krx_sector['종목명']).symmetric_difference(set(krx_ind['종목명']))

# 3.2. 합침
kor_ticker = pd.merge(krx_sector,
                      krx_ind,
                      on=krx_sector.columns.intersection(krx_ind.columns).tolist(),
                      how='outer')


# 3.3. 종목 구분 (스팩, 우선주, 리츠, 기타)
# 1) 스펙 종목 (종목명에 스팩 또는 제n호라는 단어 들어감)
# kor_ticker[kor_ticker['종목명'].str.contains('스팩| 제[0-9]+호')]['종목명']
kor_ticker_spac = kor_ticker['종목명'].str.contains('스팩| 제[0-9]+호')
kor_ticker[kor_ticker_spac]['종목명']

# 2) 우선주 (종목코드 끝이 0이 아닌 종목은 우선주)
# 우선주는 True 아니면 False
# kor_ticker[kor_ticker['종목코드'].str[-1:] != '0']['종목명']
kor_ticker_prf = kor_ticker['종목코드'].str[-1:] != '0'
kor_ticker[kor_ticker_prf]['종목명']

# 3) 리츠 (종목명 리츠로 끝남)
# kor_ticker[kor_ticker['종목명'].str.endswith('리츠')]['종목명']
kor_ticker_reit = kor_ticker['종목명'].str.endswith('리츠')
kor_ticker[kor_ticker_reit]['종목명']

# 4) 기타 (하나의 테이블에만 존재하는 종목)
# diff = list(set(krx_sector['종목명']).symmetric_difference(set(krx_ind['종목명'])))
# kor_ticker[kor_ticker['종목명'].isin(diff)]['종목명']
diff = list(set(krx_sector['종목명']).symmetric_difference(set(krx_ind['종목명'])))
kor_ticker_etc = kor_ticker['종목명'].isin(diff)
kor_ticker[kor_ticker_etc]['종목명']

# 5) 종목 구분 df에 입력npwhere로 구분 배열
"""
diff = list(set(krx_sector['종목명']).symmetric_difference(set(krx_ind['종목명'])))
import numpy as np
kor_ticker['종목구분'] = np.where(kor_ticker['종목명'].str.contains('스팩| 제[0-9]+호'), '스팩',
                              np.where(kor_ticker['종목코드'].str[-1:] != '0', '우선주',
                                       np.where(kor_ticker['종목명'].str.endswith('리츠'), '리츠',
                                                np.where(kor_ticker['종목명'].isin(diff), '기타',
                                                         '보통주'))))
"""
kor_ticker_spac = kor_ticker['종목명'].str.contains('스팩| 제[0-9]+호')
kor_ticker_prf = kor_ticker['종목코드'].str[-1:] != '0'
kor_ticker_reit = kor_ticker['종목명'].str.endswith('리츠')
diff = list(set(krx_sector['종목명']).symmetric_difference(set(krx_ind['종목명'])))
kor_ticker_etc = kor_ticker['종목명'].isin(diff)
import numpy as np
kor_ticker['종목구분'] = np.where(kor_ticker_spac, '스팩',
                              np.where(kor_ticker_prf, '우선주',
                                       np.where(kor_ticker_reit, '리츠',
                                                np.where(kor_ticker_etc, '기타',
                                                         '보통주'))))
# 3.4. 추가 클렌징
kor_ticker = kor_ticker.reset_index(drop=True) # index reset
kor_ticker.columns = kor_ticker.columns.str.replace(' ', '') # Column의 공백명 제거

# 내가 원하는 열만 선택
kor_ticker = kor_ticker[['종목코드', '종목명', '시장구분', '종가', '시가총액',
                         '기준일', 'EPS', '선행EPS', 'BPS', '주당배당금', '종목구분']]
kor_ticker = kor_ticker.replace({np.nan: None}) # NaN 제거하고 None으로 교체


# 3.5. SQL 연결
"""
import pymysql

con = pymysql.connect(user='root'
                      ,passwd='1234'
                      ,host='127.0.0.1'
                      ,db='stock_db'
                      ,charset='utf8')
mycursor = con.cursor()
query = f
    insert into kor_ticker ()
    
    
"""



# 4. 섹터 데이터 크롤링
# https://www.wiseindex.com/index




