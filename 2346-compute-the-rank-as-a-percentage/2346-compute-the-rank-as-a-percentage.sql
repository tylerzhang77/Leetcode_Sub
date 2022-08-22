# Write your MySQL query statement below
with t1 as(SELECT
    student_id,
    department_id,
    RANK() OVER(partition by department_id order by mark DESC) as rk

FROM students)

SELECT
    student_id,
    department_id,
    ROUND(IFNULL((rk - 1)*100 / (COUNT(*) OVER(partition by department_id) - 1), 0),2) as percentage
FROM t1 

