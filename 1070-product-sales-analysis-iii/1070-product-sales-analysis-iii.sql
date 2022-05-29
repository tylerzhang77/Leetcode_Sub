# Write your MySQL query statement below
with t1 as(SELECT *, RANK() OVER(partition by product_id ORDER BY year ASC) as rk

FROM sales)

SELECT product_id, year as first_year, quantity, price 
FROM t1
WHERE rk=1