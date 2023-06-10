-- 9. 테이블 결합 join
-- inner join, outer join (left, right, full)
﻿
CREATE TABLE StoreGoods 
(store_id CHAR(4) NOT NULL, 
store_name VARCHAR(200) NOT NULL,
goods_id CHAR(4) NOT NULL,
num INTEGER NOT NULL,
PRIMARY KEY (store_id, goods_id));

insert into StoreGoods (store_id, store_name, goods_id, num) values ('000A', '서울', '0001', 30); 
insert into StoreGoods (store_id, store_name, goods_id, num) values ('000A', '서울', '0002', 50); 
insert into StoreGoods (store_id, store_name, goods_id, num) values ('000A', '서울', '0003', 15); 
insert into StoreGoods (store_id, store_name, goods_id, num) values ('000B', '대전', '0002', 30); 
insert into StoreGoods (store_id, store_name, goods_id, num) values ('000B', '대전', '0003', 120); 
insert into StoreGoods (store_id, store_name, goods_id, num) values ('000B', '대전', '0004', 20); 
insert into StoreGoods (store_id, store_name, goods_id, num) values ('000B', '대전', '0006', 10); 
insert into StoreGoods (store_id, store_name, goods_id, num) values ('000B', '대전', '0007', 40); 
insert into StoreGoods (store_id, store_name, goods_id, num) values ('000C', '부산', '0003', 20); 
insert into StoreGoods (store_id, store_name, goods_id, num) values ('000C', '부산', '0004', 50); 
insert into StoreGoods (store_id, store_name, goods_id, num) values ('000C', '부산', '0006', 90); 
insert into StoreGoods (store_id, store_name, goods_id, num) values ('000C', '부산', '0007', 70); 
insert into StoreGoods (store_id, store_name, goods_id, num) values ('000D', '대구', '0001', 100);

select * from goods;
select * from storegoods;

-- 두 테이블을 합침
select *
from storegoods as store -- storegoods table을 store라는 별명으로 가져옴
inner join goods as goods -- goods 테이블을 goods라는 별명으로 가져옴
on store.goods_id  = goods.goods_id; -- 두 테이블에서 해당 열들을 기준으로 합침

-- inner join
select store.goods_id
from storegoods as store -- storegoods table을 store라는 별명으로 가져옴
inner join goods as goods -- goods 테이블을 goods라는 별명으로 가져옴
	on store.goods_id  = goods.goods_id; -- 두 테이블에서 해당 열들을 기준으로 합침

select store.goods_id, store.store_name, store.goods_id,
	goods.goods_name, goods.sell_price
from storegoods as store
inner join goods as goods
	on store.goods_id  = goods.goods_id;

-- outer join (right)
select distinct(goods_id) from Storegoods;
select distinct(goods_id) from goods;
select store.goods_id, store.store_name, store.goods_id,
	goods.goods_name, goods.sell_price
from storegoods as store
right outer join goods as goods
	on store.goods_id  = goods.goods_id;

-- outer join (left)
select distinct(goods_id) from Storegoods;
select distinct(goods_id) from goods;
select store.goods_id, store.store_name, store.goods_id,
	goods.goods_name, goods.sell_price
from storegoods as store
left outer join goods as goods
	on store.goods_id  = goods.goods_id;