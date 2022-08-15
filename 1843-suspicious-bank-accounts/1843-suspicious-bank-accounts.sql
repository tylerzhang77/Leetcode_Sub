# Write your MySQL query statement below
with t1 as(SELECT account_id,
    SUM(amount) as ttl,
    DATE_FORMAT(day,'%Y%m') as mth,
    (CASE WHEN SUM(amount) > max_income THEN 1
    ELSE 0
    END) as ind

FROM transactions t
    LEFT JOIN accounts a
    USING(account_id)

WHERE t.type = 'Creditor'

GROUP BY account_id, mth
          
ORDER BY account_id ASC, mth ASC)

SELECT DISTINCT a.account_id

FROM t1 a 
    JOIN t1 b
    ON a.account_id = b.account_id AND PERIOD_DIFF(b.mth, a.mth) = 1

WHERE a.ind = 1 AND b.ind = 1