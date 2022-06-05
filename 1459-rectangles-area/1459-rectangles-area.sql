# Write your MySQL query statement below
SELECT
    p1.id as p1,
    p2.id as p2,
    ABS(p1.x_value - p2.x_value) * ABS(p1.y_value - p2.y_value) as area
FROM points p1
    JOIN points p2 
WHERE p1.id < p2.id
HAVING area != 0
ORDER BY area DESC, p1 ASC, p2 ASC

