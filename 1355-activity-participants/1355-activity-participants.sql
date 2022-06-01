# Write your MySQL query statement below
SELECT activity
FROM friends
GROUP BY activity
HAVING COUNT(*)>(
    SELECT COUNT(*)
    FROM friends
    GROUP BY activity
    ORDER BY COUNT(*) ASC
    LIMIT 1
)
AND COUNT(*)<(
    SELECT COUNT(*)
    FROM friends
    GROUP BY activity
    ORDER BY COUNT(*) DESC
    LIMIT 1
)







