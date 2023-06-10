-- https://www.youtube.com/watch?v=08Jbh6GiWxI&list=PLkREQFGfPOZ3g1aWNVEHoJRaUWOga10pw&index=23

-- 6. 데이터베이스에서 열 선택
-- select <열 이름 1>, ..., <열 이름 n>
-- from <테이블 명>
select goods_id, goods_name, buy_price
from goods;

-- 모든 데이터를 보고 싶으면 *
select * from goods;

-- 이름을 간결하게 하려면
select goods_id as id,
	goods_name as name,
    buy_price as price
from goods;
-- 상수 및 계산식 작성 가능
select '상품' as category,
	38 as num,
    '2022-01-01' as data,
    goods_id,
    goods_name,
    sell_price, buy_price, sell_price - buy_price as profit
from goods;

-- 7. 중복 데이터 제거 & 고유값만 확인
-- select distinct <열 이름>
-- from <테이블 명>;
select distinct goods_classify from goods;

-- 8. 조건에 부합하는 행만 선택 (where)
-- where 뒤에 from 있어야 함
-- select <열 이름>, ...
-- from <테이블명>
-- where <조건식>
select goods_name, goods_classify
from goods
where goods_classify = '의류';

-- 9. 연산자
-- 연산을 위해 사용 (일반적으로 where 구 안에서 사용됨)
-- 산술 / 비교 / 논리 연산자
select *, sell_price - buy_price as profit
from goods
where sell_price - buy_price >= 500;

select goods_name, goods_classify, sell_price
from goods
where sell_price >= 1000;

select goods_name, goods_classify, sell_price
from goods
where register_date < '2020-09-27';

-- 복수의 조건 and / or
select goods_name, goods_classify, sell_price
from goods
where goods_classify < '주방용품';
and sell_price >= 3000;

-- 10. 집약함수
-- count (행 숫자), sum, avg, max, min
select count(*) from goods;

select * from goods;

-- Null을 무시하고 계산
select count(buy_price) from goods;
select sum(sell_price), sum(buy_price) from goods;
select avg(sell_price) from goods;

# 고유값의 개수 count & distinct
select count(distinct goods_classify) from goods;

-- 11. 그룹화와 정렬
-- group by 구 사용
select count(*)
from goods
group by goods_classify;

select goods_classify, count(*)
from goods
group by goods_classify;

select buy_price, count(*)
from goods
group by buy_price;

-- group by 계산 이전 조건 선택 ; where
select buy_price, count(*)
from goods
where goods_classify = '의류'
group by buy_price;

-- group by 계산 이후 조건 선택 ; having
-- select <열 이름 1>, <열 이름 2>, ...
-- from <테이블 명>
-- group by <열 이름 1>, <열 이름 2>, ...;
-- having <그룹 값에 대한 조건>
select goods_classify, avg(sell_price)
from goods
group by goods_classify;
having avg(sell_price) >= 2500;

-- 12. 결과 정렬; order by 구 (오름차순 / 내림차순)
-- select <열 이름 1>, <열 이름 2>, ...
-- from <테이블 명>
-- order by <재정렬 기준 열 1>, ...;
select *
from goods
order by sell_price;

-- 내림차순 desc
select *
from goods
order by sell_price desc;

-- 13 & 14. 뷰 & 서브쿼리
-- 13. 뷰
-- 기초구분만으로는 복잡한 데이터 분석에 한계 -> 뷰 & 서브쿼리 사용
-- view: 테이블과 거의 같으나 table과 달리 실제 데이터를 저장하지 않음
-- 내부적으로 쿼리를 실행해 일시적으로 가상 데이터를 만듦. 데이터가 아닌 쿼리를 저장
-- 기억 장치 용량 절약
-- 자주 사용하는 쿼리를 매번 작성하지 않고 뷰로 저장하면 반복해서 사용 가능
-- create view <뷰 이름>
-- (<뷰의 열 이름1>, <뷰의 열 이름2>, ...)
-- as
-- <쿼리>;
create view GoodSum (goods_classify, cnt_goods)
as
select goods_classify, count(*)
from goods
group by goods_classify;

-- view 보기
select * from goodsum;

-- view 삭제
-- drop view <뷰 명>;
-- 선택 - 우클릭 - drop view
drop view goodsum;

-- 14. 서브쿼리
-- 쿼리 내의 쿼리. 일회용 뷰
-- 뷰를 정의하는 구문을 그대로 다른 구 안에 삽입하는 것
-- 스칼라 서브쿼리: 단일 값이 반환되는 서브쿼리 (비교연산자에 사용 가능)
select avg(sell_price)
from goods;

select * from goods
where sell_price > (select avg(sell_price)
from goods);

-- 스칼라 서브쿼리는 where 구 뿐 아니라 거의 모든 곳에 사용 가능
select goods_id, goods_name, sell_price,
	(select avg(sell_price) from goods) as avg_price
from goods;