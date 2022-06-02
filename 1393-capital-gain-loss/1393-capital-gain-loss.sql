# Write your MySQL query statement below
with t1 as (
    SELECT *,
    (CASE WHEN operation = 'Buy' THEN -1
    WHEN operation = 'Sell' THEN 1 
    END) as ind
    FROM stocks
)
SELECT 
    stock_name,
    SUM(ind*price) as capital_gain_loss
FROM t1
GROUP BY stock_name