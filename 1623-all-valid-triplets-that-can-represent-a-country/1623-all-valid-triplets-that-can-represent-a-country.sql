# Write your MySQL query statement below
SELECT
    a.student_name as member_A,
    b.student_name as member_B,
    c.student_name as member_C
FROM schoolA as a JOIN schoolB as b ON a.student_id != b.student_id AND a.student_name != b.student_name
JOIN schoolC as c ON a.student_id != c.student_id AND a.student_name != c.student_name AND c.student_id != b.student_id AND c.student_name != b.student_name