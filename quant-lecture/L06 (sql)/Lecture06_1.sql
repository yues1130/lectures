-- https://www.youtube.com/watch?v=08Jbh6GiWxI&list=PLkREQFGfPOZ3g1aWNVEHoJRaUWOga10pw&index=23

-- 1. table이 저장될 database를 만들기
-- create database [데이터베이스명];
-- ctrl + shift + enter로 실행
-- Schemas에서 생성된 database 확인 가능
create database shop;

-- 2. 사용하고자 하는 database 지정
-- use [데이터베이스명];
use shop;

-- 3. 테이블 만들기
-- create table <테이블명>
-- (
-- <열 이름 1> <데이터 형태> <해당 열의 제약>,
-- <열 이름 2> <데이터 형태> <해당 열의 제약>,
-- ...
-- <테이블의 제약 1>, <테이블의 제약 1>, ...
-- )
create table goods
(
-- 열이름 데이터형태 
goods_id char(4) not null, -- 문자 4개 / null을 허용 안함
goods_name varchar(100) not null, -- 문자 0~100개
goods_classify varchar(32) not null, -- 
sell_price integer,
buy_price integer,
register_date date, -- 날짜
primary key (goods_id) -- 고유한 데이터임을 구분. 고유한 데이터를 갖는 열을 지정
)

-- 4. 테이블의 정의 변경 (열을 추가 또는 삭제)
-- 4.1. 열 추가
-- alter table <테이블명> add column <열 이름> <열 정의>;
alter table goods add column goods_name_eng varchar(100);

-- 4.2. 열 삭제
-- alter table <테이블명> drop column <열 이름>;
alter table goods drop column goods_name_eng;


-- 5. data를 table에 등록하는 query
-- insert into <테이블명> values (값);
insert into goods values ('0001', '티셔츠','의류',1000,500,'2020-09-20');
insert into goods values ('0002', '펀칭기','사무용품',500,320,'2020-09-11');
insert into goods values ('0003', '와이셔츠','의류',4000,2800,NULL);
insert into goods values ('0004', '식칼','주방용품',3000,2800,'2020-09-20');
insert into goods values ('0005', '압력솥','주방용품',6800,5000,'2020-01-15');
insert into goods values ('0006', '포크','주방용품',500,NULL,'2020-09-20');
insert into goods values ('0007', '도마','주방용품',880,790,'2020-04-28');
insert into goods values ('0008', '볼펜','사무용품',100,NULL,'2020-11-11');