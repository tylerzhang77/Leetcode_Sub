# Write your MySQL query statement below
with t1 as (
    SELECT 
    *,
    DENSE_RANK() OVER(partition by student_id ORDER BY grade DESC, course_id ASC) as rk
    FROM enrollments
)
SELECT 
    student_id,
    course_id,
    grade
    
FROM t1 

WHERE rk = 1