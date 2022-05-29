# Write your MySQL query statement below
SELECT
    ROUND(MIN(sqrt(POWER(p1.x-p2.x,2)+POWER(p1.y-p2.y,2))),2) as shortest
FROM point2d p1 
    JOIN point2d p2 
    ON p1.x != p2.x OR p1.y != p2.y
    