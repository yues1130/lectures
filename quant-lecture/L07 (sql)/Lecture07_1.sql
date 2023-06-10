-- https://www.youtube.com/watch?v=QtiDoQIxr4w&list=PLkREQFGfPOZ3g1aWNVEHoJRaUWOga10pw&index=22

-- 1. 함수, 술어와 case 식
-- 1. 산술 함수
create table SampleMath
(m numeric (10,3),
n integer,
p integer);

insert into SampleMath (m, n, p) values (500, 0, NULL);
insert into SampleMath (m, n, p) values (-180, 0, NULL);
insert into SampleMath (m, n, p) values (NULL, NULL, NULL);
insert into SampleMath (m, n, p) values (NULL, 7, 3);
insert into SampleMath (m, n, p) values (NULL, 5, 2);
insert into SampleMath (m, n, p) values (NULL, 4, NULL);
insert into SampleMath (m, n, p) values (NULL, 4, NULL);
insert into SampleMath (m, n, p) values (8, NULL, 3);
insert into SampleMath (m, n, p) values (2.27, 1, NULL);
insert into SampleMath (m, n, p) values (5.555, 2, NULL);
insert into SampleMath (m, n, p) values (NULL, 1, NULL);
insert into SampleMath (m, n, p) values (8.76, NULL, NULL);

select * from samplemath;

-- abs; 절대값
select m, abs(m) as abs_m
from samplemath;

-- mod; 나누기의 나머지
select n, p, mod(n, p) as mod_col
from samplemath;

-- round; 반올림
-- ceil; 올림 / floor; 내림
select m, n, round(m,n) as round_col
from samplemath;

-- 2. 문자열 함수
create table SampleStr
(str1 varchar(40),
str2 varchar(40),
str3 varchar(40));

insert into SampleStr (str1, str2, str3) values ('가나다','라마', NULL);
insert into SampleStr (str1, str2, str3) values ('abc','def',NULL);
insert into SampleStr (str1, str2, str3) values ('김','철수','입니다');
insert into SampleStr (str1, str2, str3) values ('aaa',NULL,NULL);
insert into SampleStr (str1, str2, str3) values (NULL,'가가가',NULL);
insert into SampleStr (str1, str2, str3) values ('@!#$%',NULL,NULL);
insert into SampleStr (str1, str2, str3) values ('ABC',NULL,NULL);
insert into SampleStr (str1, str2, str3) values ('aBC',NULL,NULL);
insert into SampleStr (str1, str2, str3) values ('abc철수','abc','ABC');
insert into SampleStr (str1, str2, str3) values ('abcdefabc','abc','ABC');
insert into SampleStr (str1, str2, str3) values ('아이우','아','우');

select * from samplestr;

-- concat; 문자열 합침
select str1, str2, concat(str1, str2) as str_concat
from SampleStr;

-- lower / upper ; 소/대문자 변환
select str1, lower(str1) as low_str
from SampleStr;

select str1, upper(str1) as low_str
from SampleStr;

-- replace; 일부 문자를 다른 문자로 변경
-- replace(대상문자열, 치환전 문자열, 치환후 문자열)
select str1, str2, str3,
	replace(str1, str2, str3) as rep_str
from SampleStr;

-- 3. 날짜 함수
-- 현재 날자, 시간, 일시 -> from 구문 없이 사용 가능
select current_date, current_time, current_timestamp;

-- extract; 특정 부분만 추출
select
	current_date,
    extract(year from current_date) as year,
    extract(month from current_date) as month,
    extract(day from current_date) as day;

-- 4. 술어
-- like 술어; 부분 일치
-- == ; 완전 일치
create table SampleLike
(strcol varchar(6) not null,
primary key (strcol));

insert into SampleLike (strcol) values ('abcddd');
insert into SampleLike (strcol) values ('dddabc');
insert into SampleLike (strcol) values ('abdddc');
insert into SampleLike (strcol) values ('abcdd');
insert into SampleLike (strcol) values ('ddabc');
insert into SampleLike (strcol) values ('abddc');

select * from samplelike;

-- 전방일치; 검색 조건이 되는 문자열이 검색 대상 문자열의 가장 앞에 위치하고 있는 행을 선택
-- 중간일치; 검색 조건이 되는 문자열이 검색 대상 문자열의 어딘가에 포함되고 있으면 선택
-- 후방일치; 검색 조건이 되는 문자열이 검색 대상 문자열의 가장 뒤에 위치하고 있는 행을 선택

-- 전방일치; %는 '0문자 이상의 임의 문자열'
select *
from samplelike
where strcol like 'ddd%'; 

-- 중간일치
select *
from samplelike
where strcol like '%ddd%'; 

-- 후방일치
select *
from samplelike
where strcol like '%ddd'; 

-- 5. between; 범위 검색
select *
from goods
where sell_price between 100 and 1000;

-- 6. is null 
-- null 포함; is null
select *
from goods
where buy_price is null; -- 그냥 null이면 X. null은 비교가 불가한 특별한 표시어

-- null 제외; is not null
select *
from goods
where buy_price is not null;

-- 7. in 술어
-- 너무 복잡함
select *
from goods
where buy_price = 320
	or buy_price = 500
    or buy_price = 5000;

-- in으로 간단하게
select *
from goods
where buy_price in (320,500,5000);

-- 8. case 식; 경우에 따라 값을 구분
-- case when <평가식 1> then <식 1>
-- 	when <평가식 2> then <식 2>
-- 	when <평가식 3> then <식 3>
--     ...
--     else <식 n>
-- end
select goods_name, sell_price,
case when sell_price >= 6000 then '고기'
	when sell_price >= 3000 and sell_price < 6000 then '중가'
	when sell_price < 3000 then '저가'
	else null
end as price_classify
from goods;


