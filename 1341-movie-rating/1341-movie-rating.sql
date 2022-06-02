# Write your MySQL query statement below
(SELECT name as results
FROM movierating mr
    LEFT JOIN users USING(user_id)
GROUP BY user_id
ORDER BY COUNT(*) DESC, name 
LIMIT 1 )

UNION

(SELECT title as results
FROM movierating mr
    LEFT JOIN movies USING(movie_id)
WHERE SUBSTRING(created_at,1,7) = '2020-02'
GROUP BY movie_id
ORDER BY AVG(rating) DESC, title
LIMIT 1 )