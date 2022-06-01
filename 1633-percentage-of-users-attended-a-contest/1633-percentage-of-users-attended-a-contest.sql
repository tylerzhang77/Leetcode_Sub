# Write your MySQL query statement below
SELECT
    contest_id,
    ROUND(100*COUNT(*) / (SELECT COUNT(*) FROM users),2) percentage
FROM register r 

GROUP BY contest_id

ORDER BY percentage DESC, contest_id ASC
    
