# lecture 09: 인코딩
# 사람의 언어를 컴퓨터의 언어(0&1)로 변환
# 반대과정은 디코딩
# 한글의 인코딩: EUC-KR, CP949, UTF-8

# ex) 퀀트
# 1. '퀀'과 '트'라는 문자 자체에 코드 부여
# 2. 구성하는 'ㅋ','ㅜ','ㅓ ','','','',모음과 자음을 나누어 각각에 코드를 부여하고 조합

# 가장 대표적인 것: EUC-KR -> 현대 한글에서 많이 쓰이는 문자 2350개에 번호 부여한 방법
# CP949: EUC-KR의 2350개로는 모든 자모 조합 표현에 부족해 이를 보완하고자 MS가 11720개 문자에 번호를 부여한 방법
# UTF-8: 조합형. 한글뿐 아니라 다양한 언어에 적용 가능해 전세계 웹페이지의 97.6%가 utf-8로 제작됨


# 크롤링: 웹사이트의 정보를 수집하는 과정
# 웹이 어떻게 동작하는지 이해해야 함
# 클라이언트: 데스크탑, 핸드폰 등의 장치 or 크롬이나 파이어폭스와 같은 SW
# 서버: 웹사이트와 앱을 저장하는 컴퓨터

# 요청 (request): 클라이언트가 특정 정보를 요구하는 과정
# 응답 (response): 서버가 해당 정보를 제공하는 과정
# 클라이언트와 서버간 연결하는 공간이 인터넷

# 서버의 고유 주소: 인터넷 주소 or URL

# 클라이언트가 데이터를 요청하는 방식의 규정된 약속/표준: HTTP
# HTTP 요청 방식 (HTTP Request Method): 클라이언트가 서버에게 요청의 목적이나 종류를 알리는 방법
# HTTP 요청 방식의 종류: GET, POST, PUT, DELETE



