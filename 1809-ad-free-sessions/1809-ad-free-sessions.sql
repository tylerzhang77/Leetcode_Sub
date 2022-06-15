# Write your MySQL query statement below
SELECT 
    DISTINCT session_id
    
FROM playback p 
    LEFT JOIN ads a
    ON p.customer_id = a.customer_id
    AND a.timestamp BETWEEN start_time AND end_time
WHERE a.timestamp IS NULL

