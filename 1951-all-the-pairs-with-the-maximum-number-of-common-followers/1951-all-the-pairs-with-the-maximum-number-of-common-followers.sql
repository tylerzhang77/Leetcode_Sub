# Write your MySQL query statement below
SELECT
    user1_id, user2_id
FROM(SELECT r1.user_id as user1_id, r2.user_id as user2_id,
    RANK() OVER(ORDER BY COUNT(*) DESC) as rk

FROM relations r1
JOIN relations r2
ON r1.follower_id = r2.follower_id AND r1.user_id<r2.user_id

GROUP BY r1.user_id, r2.user_id
) t
WHERE rk = 1