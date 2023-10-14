SELECT
       t.id,
       t.NAME,
       COUNT(p.id) AS "player_count",
       t.fan_base
FROM teams AS "t"
LEFT JOIN players AS "p" ON p.team_id = t.id
WHERE t.fan_base > 30000
GROUP BY t.id, t.NAME, t.fan_base
ORDER BY player_count DESC, t.fan_base DESC;