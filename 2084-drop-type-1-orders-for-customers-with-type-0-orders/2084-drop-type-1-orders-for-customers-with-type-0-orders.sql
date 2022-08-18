# Write your MySQL query statement below
SELECT
    *
FROM orders 

WHERE (customer_id, order_type) IN (
    SELECT
        customer_id,
        MIN(order_type)
    FROM orders
    GROUP BY customer_id
)