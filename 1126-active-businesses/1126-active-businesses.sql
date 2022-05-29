# Write your MySQL query statement below
with t1 as (
    SELECT 
        distinct event_type,
        SUM(occurences) / COUNT(*) as avg_act
    FROM events 
    
    GROUP BY event_type
)

SELECT
    business_id
FROM events e
    LEFT JOIN t1 USING(event_type)
    
WHERE e.occurences > t1.avg_act

GROUP BY business_id

HAVING COUNT(*) > 1



