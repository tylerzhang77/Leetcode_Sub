# Write your MySQL query statement below
SELECT DISTINCT p1.user_id

FROM purchases p1   
    INNER JOIN purchases p2
    ON  p1.user_id = p2.user_id AND p1.purchase_id <> p2.purchase_id
        AND abs(datediff(p1.purchase_date, p2.purchase_date))<=7

ORDER BY p1.user_id


