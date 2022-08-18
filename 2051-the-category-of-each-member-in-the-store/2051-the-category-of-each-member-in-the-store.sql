# Write your MySQL query statement below
with t1 as(SELECT
    m.member_id,
    name,
    SUM(CASE WHEN charged_amount IS NOT NULL THEN 1
    ELSE 0
    END) / COUNT(*) as rt,
    v.visit_id
    
FROM members m
    LEFT JOIN visits v
    USING(member_id)
    LEFT JOIN purchases p
    USING(visit_id)

GROUP BY m.member_id)

SELECT
    member_id,
    name,
    (CASE WHEN visit_id IS NULL THEN 'Bronze'
    WHEN rt < 0.50 THEN 'Silver'
    WHEN rt >= 0.50 AND rt < 0.80 THEN 'Gold'
    ELSE 'Diamond'
    END) as category

FROM t1

ORDER BY member_id