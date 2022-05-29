# Write your MySQL query statement below
SELECT
    ROUND(SUM(tiv_2016),2) as tiv_2016 
FROM insurance

WHERE CONCAT(lat, CONCAT(',',lon)) IN (
    SELECT CONCAT(lat, CONCAT(',',lon))
    FROM insurance 
    GROUP BY lat, lon
    HAVING COUNT(*)=1
) AND 
tiv_2015 IN (
    SELECT tiv_2015
    FROM insurance 
    GROUP BY tiv_2015
    HAVING COUNT(*)>1
)