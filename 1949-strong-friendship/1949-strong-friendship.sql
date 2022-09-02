# Write your MySQL query statement below
with temp as (
    SELECT
        user1_id as user, user2_id as fid
    
    FROM friendship f
    
    UNION
    
    SELECT
        user2_id as user, user1_id as fid 
    
    FROM friendship f 
)

SELECT
    user1_id,
    user2_id,
    COUNT(*) as common_friend

FROM friendship f, temp as t1, temp as t2

WHERE f.user1_id = t1.user AND f.user2_id = t2.user AND t1.fid = t2.fid 

GROUP BY f.user1_id, f.user2_id

HAVING COUNT(*) >= 3



