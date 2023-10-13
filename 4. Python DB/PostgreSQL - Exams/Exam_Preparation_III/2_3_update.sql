UPDATE players_ranges
SET max_players = max_players + 1
WHERE min_players = 2 AND max_players = 2;

UPDATE board_games
SET name = CONCAT(name, ' V2')
WHERE release_year >= 2020;