# Lec 08_1 & 08_2
alter shop;

select * from goods;
select * from iris;
# 아래 저장 버튼으로 CSV 저장이 가능하나 비효율적

# Lec 08_3 
# 6.2.
use exam;
select * from price;

# upsert 기능
# insert into @table 
# (arg1, arg2, arg3) 
# values
# (@arg1, @arg2, @arg3)
# on duplicate key update (key를 제외한 update할 칼럼)
# arg2 = @arg2, arg3 = @arg3
create table price_2(
	날짜 varchar(10),
    티커 varchar(6),
    종가 int,
    거래량 int,
    PRIMARY KEY(날짜, 티커)
);

select * from price_2;


insert into price_2 (날짜, 티커, 종가, 거래량)
values
('2021-01-02','000001',1340,1000),
('2021-01-03','000001',1315,2000),
('2021-01-02','000002',500,200);

select * from price_2;

# upsert 1
insert into price_2 (날짜, 티커, 종가, 거래량)
values
('2021-01-02','000001',1340,1000),
('2021-01-03','000001',1315,2000),
('2021-01-02','000002',500,200),
('2021-01-03','000002',1380,3000)
as new # new라는 별명이로 입력
on duplicate key update # 프라이머리 키에 데이터가 존재하면 업데이트하고 아니면 입력
종가 = new.종가, 거래량=new.거래량;

select * from price_2;

# upsert 2 (업데이트 & 새로 입력)
insert into price_2 (날짜, 티커, 종가, 거래량)
values
('2021-01-02','000001',1300,1100),
('2021-01-04','000001',1300,2000)
as new
on duplicate key update
종가 = new.종가, 거래량=new.거래량;

select * from price_2;