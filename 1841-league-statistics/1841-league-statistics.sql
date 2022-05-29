# Write your MySQL query statement below
SELECT
    t.team_name as team_name,
    COUNT(*) as matches_played,
    SUM(CASE 
            WHEN home > away then 3 
            WHEN home = away then 1 
            ELSE 0
        END) as points,
    SUM(home) as goal_for,
    SUM(away) as goal_against,
    SUM(home) - SUM(away) as goal_diff

FROM
    (   
        SELECT home_team_id, home_team_goals as home, away_team_goals as away
            FROM Matches 
    
        UNION ALL
        
        SELECT away_team_id as home_team_id, away_team_goals as home, home_team_goals as away
            FROM Matches
    ) as u
    
    LEFT JOIN teams as t 
        ON t.team_id = u.home_team_id
        
GROUP BY 1

ORDER BY 3 DESC, 6 DESC, 1


