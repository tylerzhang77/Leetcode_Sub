# Write your MySQL query statement below
SELECT
    sp.salesperson_id,
    name,
    IFNULL(SUM(price),0) as total

FROM salesperson sp
    LEFT JOIN customer c
    USING(salesperson_id)
    LEFT JOIN sales s
    USING(customer_id)

GROUP BY sp.salesperson_id