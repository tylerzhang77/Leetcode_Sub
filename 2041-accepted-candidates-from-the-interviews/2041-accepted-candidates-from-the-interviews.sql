# Write your MySQL query statement below
SELECT
    candidate_id

FROM candidates c
    LEFT JOIN rounds r
    USING(interview_id)

WHERE years_of_exp > 1

GROUP BY candidate_id

HAVING SUM(score) > 15