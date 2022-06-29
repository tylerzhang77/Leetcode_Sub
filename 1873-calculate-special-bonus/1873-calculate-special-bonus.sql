# Write your MySQL query statement below
SELECT
    employee_id,
    (CASE WHEN ((employee_id MOD 2 = 1) AND LEFT(name, 1) != 'M' ) THEN salary
    ELSE 0
    END) as bonus
FROM employees
ORDER BY employee_id


