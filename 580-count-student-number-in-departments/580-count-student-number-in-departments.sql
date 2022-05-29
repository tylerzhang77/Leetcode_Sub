# Write your MySQL query statement below
SELECT
    dept_name, IFNULL(COUNT(student_id),0) as student_number
FROM department d 
    LEFT JOIN student s USING(dept_id)
GROUP BY d.dept_id

ORDER BY student_number DESC, dept_name