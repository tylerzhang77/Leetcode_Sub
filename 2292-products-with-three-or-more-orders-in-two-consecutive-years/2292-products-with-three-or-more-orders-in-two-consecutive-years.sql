# Write your MySQL query statement below
with t1 as(SELECT
    product_id,
    COUNT(*) as cnt,
    YEAR(purchase_date) as yr
FROM orders 
GROUP BY product_id, YEAR(purchase_date))

SELECT
    DISTINCT a.product_id
FROM t1 as a JOIN t1 as b
    ON a.product_id = b.product_id AND b.yr - a.yr = 1
WHERE a.cnt > 2 and b.cnt > 2
    