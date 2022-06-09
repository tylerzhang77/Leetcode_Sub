# Write your MySQL query statement below
SELECT
    SUM(IFNULL(b.apple_count,0))+SUM(IFNULL(c.apple_count,0)) as apple_count,
    SUM(IFNULL(b.orange_count,0))+SUM(IFNULL(c.orange_count,0)) as orange_count
FROM boxes b
    LEFT JOIN chests c USING(chest_id)
    