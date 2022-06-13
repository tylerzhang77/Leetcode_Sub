# Write your MySQL query statement below
with t1 as(SELECT *,
    (CASE WHEN type = 'Deposit' THEN amount
    WHEN type = 'Withdraw' THEN -amount
    END) as cur

FROM transactions t
)
SELECT
    account_id, day,
    SUM(cur) OVER(partition by account_id ORDER BY day ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as balance
FROM t1