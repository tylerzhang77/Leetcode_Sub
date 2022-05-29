# Write your MySQL query statement below
with t1 as(
    SELECT 
    *,
        RANK() OVER(partition by customer_id order by order_date) as rk
    FROM delivery
)

SELECT
    ROUND(100*(SUM(
        CASE WHEN order_date = customer_pref_delivery_date THEN 1
        ELSE 0
        END
    ) / COUNT(*)),2) as immediate_percentage
    
FROM t1
WHERE rk = 1