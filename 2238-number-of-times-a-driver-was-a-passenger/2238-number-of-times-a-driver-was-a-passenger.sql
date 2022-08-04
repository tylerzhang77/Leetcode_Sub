# Write your MySQL query statement below
with t1 as(SELECT DISTINCT driver_id 

FROM rides 
)

SELECT
    t1.driver_id,
    SUM(CASE WHEN r.ride_id IS NULL THEN 0
    ELSE 1
    END) as cnt
FROM t1 
    LEFT JOIN rides r
    ON t1.driver_id = r.passenger_id
GROUP BY t1.driver_id