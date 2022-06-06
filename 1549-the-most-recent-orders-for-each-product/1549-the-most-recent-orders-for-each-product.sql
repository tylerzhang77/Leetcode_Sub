# Write your MySQL query statement below
with t1 as (SELECT
    *, RANK() OVER(partition by product_id ORDER BY order_date DESC) rk
FROM orders)

SELECT
    product_name, t1.product_id, order_id, order_date
FROM t1
    LEFT JOIN products p USING(product_id)
    LEFT JOIN customers c USING(customer_id)

WHERE rk = 1

ORDER BY product_name, product_id, order_id

