# Write your MySQL query statement below
SELECT DISTINCT num as ConsecutiveNums
FROM
(
    SELECT num,
        LAG(num) OVER(ORDER BY id) as la,
        LEAD(num) OVER(ORDER BY id) as le
    FROM logs
) t
WHERE num = la AND num = le