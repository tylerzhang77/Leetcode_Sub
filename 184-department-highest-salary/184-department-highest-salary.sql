# Write your MySQL query statement below
SELECT

d.name as Department,

e.name as Employee,

e.salary as Salary

FROM

(

    SELECT name, salary, departmentid,
        DENSE_RANK() OVER(PARTITION BY departmentID ORDER BY salary DESC) as rk 
    
    FROM employee

) as e

INNER JOIN department as d 
        ON e.departmentid = d.id
        
WHERE e.rk = 1