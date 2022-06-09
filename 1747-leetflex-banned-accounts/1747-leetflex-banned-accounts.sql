# Write your MySQL query statement below
SELECT
    DISTINCT i1.account_id
FROM loginfo i1
JOIN loginfo i2 

WHERE i1.account_id = i2.account_id AND i1.ip_address != i2.ip_address
    AND ((i1.login BETWEEN i2.login AND i2.logout) OR (i2.logout BETWEEN i1.login AND i1.logout))