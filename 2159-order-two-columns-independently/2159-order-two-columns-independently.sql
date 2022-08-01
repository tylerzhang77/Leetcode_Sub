# Write your MySQL query statement below
with t1 as(
    SELECT
        first_col,
        ROW_NUMBER() OVER(ORDER BY first_col ASC) r1
    FROM data
),
t2 as(
    SELECT
        second_col,
        ROW_NUMBER() OVER(ORDER BY second_col DESC) r2
    FROM data
)
SELECT first_col, second_col
FROM t1
    LEFT JOIN t2
    ON t1.r1 = t2.r2