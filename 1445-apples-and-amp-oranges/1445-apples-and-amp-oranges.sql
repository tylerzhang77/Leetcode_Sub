# Write your MySQL query statement below
SELECT
    sale_date,
    SUM(IF(fruit = 'apples', sold_num, -sold_num)) as diff
FROM sales
GROUP BY sale_date
ORDER BY sale_date