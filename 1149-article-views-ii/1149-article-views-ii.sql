# Write your MySQL query statement below
SELECT
    DISTINCT viewer_id as id

FROM views 

GROUP BY viewer_id, view_date

HAVING COUNT(DISTINCT article_id)>1

ORDER BY id