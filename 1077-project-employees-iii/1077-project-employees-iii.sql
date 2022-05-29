# Write your MySQL query statement below
with t1 as(SELECT
    p.project_id, p.employee_id,
    RANK() OVER(partition by project_id ORDER BY experience_years DESC) as rk
FROM project p
    LEFT JOIN employee USING(employee_id)    )
    
SELECT
    project_id, employee_id
FROM t1
WHERE rk=1
