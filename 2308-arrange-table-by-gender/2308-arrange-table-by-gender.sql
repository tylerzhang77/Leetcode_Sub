# Write your MySQL query statement below
with t1 as (SELECT
    user_id,
    gender,
    RANK() OVER(partition by gender order by user_id) as rk,
    (CASE WHEN gender = 'female' THEN 1
    WHEN gender = 'other' THEN 2
    ELSE 3
    END) as rk2

FROM genders
)
SELECT
    user_id,
    gender

FROM t1 

ORDER BY rk, rk2