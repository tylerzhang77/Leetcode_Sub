# Write your MySQL query statement below
with t1 as(SELECT
    city_id,
    day,
    degree,
    RANK() OVER(partition by city_id order by degree DESC, day ASC) as rk

FROM weather  )

SELECT
    city_id,
    day,
    degree
FROM t1 

WHERE rk = 1