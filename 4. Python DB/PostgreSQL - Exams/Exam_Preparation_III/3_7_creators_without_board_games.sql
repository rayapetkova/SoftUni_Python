SELECT
	   cr.id,
	   CONCAT(cr.first_name, ' ', cr.last_name) AS "creator_name",
	   cr.email
FROM creators AS "cr"
WHERE cr.id NOT IN (
					SELECT creator_id FROM creators_board_games);