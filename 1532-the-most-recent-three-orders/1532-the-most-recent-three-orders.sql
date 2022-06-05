# Write your MySQL query statement below
with t1 as(
        SELECT *, ROW_NUMBER() OVER(partition by customer_id ORDER BY order_date DESC) as rk
        FROM orders
)
SELECT
    name as customer_name,
    t1.customer_id,
    order_id,
    order_date
FROM t1 
    JOIN customers c ON c.customer_id = t1.customer_id AND rk <= 3
ORDER BY customer_name ASC, customer_id ASC, order_date DESC
    