# Write your MySQL query statement below
with t1 as(
    SELECT *,
    RANK() OVER(partition by user_id ORDER BY activity_date ASC) as rk
    FROM traffic
    WHERE activity = 'login'
)
SELECT
    activity_date as login_date,
    COUNT(DISTINCT user_id) as user_count
FROM t1

WHERE DATEDIFF('2019-06-30', activity_date)<=90 AND rk = 1

GROUP BY activity_date