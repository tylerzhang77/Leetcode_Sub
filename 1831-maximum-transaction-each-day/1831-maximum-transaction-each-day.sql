# Write your MySQL query statement below
with t1 as(
    SELECT *,
        DENSE_RANK() OVER(partition by DATE(day) ORDER BY amount DESC) as rk
    FROM transactions
)
SELECT transaction_id
FROM t1
WHERE rk = 1
ORDER BY transaction_id ASC