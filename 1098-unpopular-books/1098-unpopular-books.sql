# Write your MySQL query statement below
SELECT
    b.book_id,
    b.name
    
FROM books b
    LEFT JOIN orders o ON o.book_id = b.book_id AND DATEDIFF('2019-06-23', dispatch_date) <= 365
    
WHERE DATEDIFF('2019-06-23', available_from) > 30

GROUP BY b.book_id

HAVING IFNULL(SUM(quantity),0) < 10