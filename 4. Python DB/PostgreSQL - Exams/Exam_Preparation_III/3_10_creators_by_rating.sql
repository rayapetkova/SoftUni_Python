SELECT
	   c.last_name,
	   CEIL(AVG(bg.rating)) AS "average_rating",
	   p.name
FROM creators AS "c"
JOIN creators_board_games AS "cbg" ON cbg.creator_id = c.id
JOIN board_games AS "bg" ON bg.id = cbg.board_game_id
JOIN publishers AS "p" ON bg.publisher_id = p.id
WHERE p.name = 'Stonemaier Games'
GROUP BY c.last_name, p.name
ORDER BY average_rating DESC;