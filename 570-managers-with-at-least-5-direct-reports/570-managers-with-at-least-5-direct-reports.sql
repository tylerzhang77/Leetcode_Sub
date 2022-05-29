# Write your MySQL query statement below
SELECT 
    DISTINCT e2.name
FROM employee e1 JOIN employee e2
    ON e1.managerId = e2.id
GROUP BY e1.managerId
HAVING COUNT(*)>4