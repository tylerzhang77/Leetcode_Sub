select b.visited_on, b.amount,b.average_amount

from

	(select 
		a. visited_on,
		sum(a.amount) over (order by a.visited_on rows between 6 preceding and current row) as amount,
		round(avg(a.amount) over(order by visited_on rows between 6 preceding and current row),2) as average_amount,
		row_number() over (order by a.visited_on ) as row_num
	from 
		(select visited_on,sum(amount) as amount from customer group by visited_on)a)b

where b.row_num >= 7;

