# Write your MySQL query statement below
SELECT
    s.seller_name
FROM seller s 
    LEFT JOIN orders o
    ON o.seller_id = s.seller_id AND YEAR(sale_date) = 2020

WHERE order_id IS NULL

ORDER BY s.seller_name