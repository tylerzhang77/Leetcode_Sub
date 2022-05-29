# Write your MySQL query statement below
SELECT
    DISTINCT c.name as country

FROM person as p

LEFT JOIN country c ON c.country_code = SUBSTRING(phone_number, 1,3)
LEFT JOIN calls ca ON p.id IN (ca.caller_id, ca.callee_id)

GROUP BY c.name

HAVING avg(duration) > (SELECT avg(duration) from calls)

ORDER BY c.name

