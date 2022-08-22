# Write your MySQL query statement below
with temp as (
    SELECT product_id,
    user_id,
    SUM(quantity) as quantity
    FROM sales
    GROUP BY user_id, product_id
)

,t1 as (SELECT
    user_id,
    product_id,
    RANK() OVER(partition by user_id order by price * quantity DESC) as rk
FROM temp
    LEFT JOIN product
    USING(product_id)

)

SELECT
    user_id,
    product_id
FROM t1
WHERE rk = 1
ORDER BY user_id