# Write your MySQL query statement below
SELECT question_id AS survey_log
FROM   (SELECT question_id,
               ( Sum(IF(action = 'answer', 1, 0)) / Sum(
                 IF(action = 'show', 1, 0)) ) AS
               show_sum
        FROM   surveylog
        GROUP  BY 1) a
ORDER  BY show_sum DESC,
          question_id ASC
LIMIT  1 