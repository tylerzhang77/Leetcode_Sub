# Write your MySQL query statement below
with t1 as (SELECT wimbledon as winner
FROM championships

UNION ALL

SELECT Fr_open as winner
FROM championships

UNION ALL

SELECT US_open as winner
FROM championships

UNION ALL

SELECT Au_open as winner
FROM championships
)

SELECT
    winner as player_id,
    player_name,
    COUNT(*) as grand_slams_count
FROM t1
    JOIN players p ON p.player_id = t1.winner
    
GROUP BY player_id
