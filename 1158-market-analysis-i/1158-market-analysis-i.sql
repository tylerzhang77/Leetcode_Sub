# Write your MySQL query statement below
SELECT
    user_id as buyer_id, join_date, COUNT(order_date) as orders_in_2019
FROM users u
    LEFT JOIN orders o 
    ON u.user_id = o.buyer_id AND YEAR(order_date)=2019
GROUP BY user_id