# Write your MySQL query statement below
with t1 as(SELECT
    candidateId
    
FROM vote 

GROUP BY candidateId 

ORDER BY COUNT(*) DESC 

LIMIT 1)

SELECT
    name
FROM t1 
    LEFT JOIN candidate c
    ON c.id = t1.candidateId