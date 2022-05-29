# Write your MySQL query statement below
with t1 as (
    SELECT requester_id as re,
        accepter_id as ac 
    FROM requestaccepted 
    UNION
    SELECT accepter_id as re,
        requester_id as ac 
    FROM requestaccepted 
)
SELECT
    re as id,
    COUNT(*) as num
FROM t1
GROUP BY id
ORDER BY num DESC

LIMIT 1
