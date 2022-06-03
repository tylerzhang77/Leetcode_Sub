# Write your MySQL query statement below
SELECT
    left_operand,
    operator,
    right_operand,
    (CASE WHEN operator = '>' and v1.value > v2.value THEN 'true'
    WHEN operator = '=' and v1.value = v2.value THEN 'true'
    WHEN operator = '<' and v1.value < v2.value THEN 'true'
    ELSE 'false'
    END) as value
FROM expressions e 
    LEFT JOIN variables v1 ON e.left_operand = v1.name 
    LEFT JOIN variables v2 ON e.right_operand = v2.name 