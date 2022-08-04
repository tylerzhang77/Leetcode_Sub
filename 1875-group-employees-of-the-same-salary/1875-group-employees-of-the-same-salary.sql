# Write your MySQL query statement below
SELECT *,
    DENSE_RANK() OVER(ORDER BY salary ASC) as team_id
FROM employees
WHERE salary not in (
    SELECT salary
    FROM Employees
    GROUP BY salary
    HAVING COUNT(*) = 1
)