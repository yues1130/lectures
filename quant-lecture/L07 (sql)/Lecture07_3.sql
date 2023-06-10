-- 10. 윈도우 함수
-- 고급 집계 처리: 순위 계산, 누적합 계산, 소계
-- 일반적인 집약 처리로는 불가한 고급 처리
-- <윈도우 함수> over
-- ([partition by <열 리스트>])
-- order by <정렬용 열 리스트>
-- )
-- partition by는 생략 가능

-- 윈도우 함수로 사용가능한 함수
-- 윈도우 전용 함수: rank, dense_rank, row_number
-- 집약함수: sum, avg, count, max, min

-- rank; 같은 순위의 행이 복수개 있으면 후순위를 건너뜀
-- 예) 1위가 3개인 경우: 1위, 1위, 1위, 4위
-- sell_price 별로 정렬
select goods_name, goods_classify, sell_price,
	rank() over (order by sell_price) as ranking
from Goods;

-- goods_classify 별로 윈도우(그룹)을 나누고,
-- sell_price 별로 정렬
select goods_name, goods_classify, sell_price,
	rank() over(partition by goods_classify order by sell_price) as ranking
from Goods;

-- dense_rank: 같은 순위의 행이 복수개 있으면 후순위를 건너뛰지 않음
-- 예) 1위가 3개인 경우: 1위, 1위, 1위, 2위

-- row_number: 순위와 상관없이 연속 번호 부여
-- 예) 1위가 3개인 경우: 1위, 2위, 3위, 4위
select goods_name, goods_classify, sell_price,
	rank() over(order by sell_price) as ranking,
	dense_rank() over(order by sell_price) as ranking,
	row_number() over(order by sell_price) as ranking
from Goods;

-- sum / avg도 윈도우 함수로 사용 가능
select goods_name, goods_classify, sell_price,
	sum(sell_price) over() as current_sum
from Goods;

-- 누적 합계
select goods_name, goods_classify, sell_price,
	sum(sell_price) over(order by goods_id) as current_sum
from Goods;

-- 누적 평균
select goods_name, goods_classify, sell_price,
	avg(sell_price) over(order by goods_id) as current_sum
from Goods;

-- 윈도우 별로 집계 partition by
select goods_name, goods_classify, goods_classify, sell_price,
	sum(sell_price) over(partition by goods_classify order by goods_id) as current_sum
from Goods;

-- 범위를 기준으로 frame 만듦
select goods_name, goods_classify, sell_price,
	avg(sell_price) over(order by goods_id rows 2 preceding) as moving_avg
from Goods;

-- 앞의 행 이용 preceding
-- 뒤의 행 이용 following
select goods_name, goods_classify, sell_price,
	avg(sell_price) over(order by goods_id 
    rows between current row and 2 following) as moving_avg
from Goods;

-- preceding & following 동시 사용
select goods_name, goods_classify, sell_price,
	avg(sell_price) over(order by goods_id 
    rows between 1 preceding and 2 following) as moving_avg
from Goods;