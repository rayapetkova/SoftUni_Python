CREATE TABLE categories(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL
);


CREATE TABLE addresses(
	id SERIAL PRIMARY KEY,
	street_name VARCHAR(100) NOT NULL,
	street_number INT NOT NULL CHECK(street_number > 0),
	town VARCHAR(30) NOT NULL,
	country VARCHAR(30) NOT NULL,
	zip_code INT NOT NULL CHECK(zip_code > 0)
);


CREATE TABLE publishers(
	id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	address_id INT NOT NULL,
	website VARCHAR(40),
	phone VARCHAR(20),

	CONSTRAINT fk_publishers_addresses
		FOREIGN KEY (address_id)
			REFERENCES addresses(id)
				ON DELETE CASCADE
				ON UPDATE CASCADE
);


CREATE TABLE players_ranges(
	id SERIAL PRIMARY KEY,
	min_players INT NOT NULL CHECK(min_players > 0),
	max_players INT NOT NULL CHECK(max_players > 0)
);


CREATE TABLE creators(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	email VARCHAR(30) NOT NULL
);


CREATE TABLE board_games(
	id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	release_year INT NOT NULL CHECK(release_year > 0),
	rating NUMERIC(2) NOT NULL,
	category_id INT NOT NULL,
	publisher_id INT NOT NULL,
	players_range_id INT NOT NULL,

	CONSTRAINT fk_board_games_categories
		FOREIGN KEY (category_id)
			REFERENCES categories(id)
				ON DELETE CASCADE
				ON UPDATE CASCADE,

	CONSTRAINT fk_board_games_publishers
		FOREIGN KEY (publisher_id)
			REFERENCES publishers(id)
				ON DELETE CASCADE
				ON UPDATE CASCADE,

	CONSTRAINT fk_board_games_players_ranges
		FOREIGN KEY (players_range_id)
			REFERENCES players_ranges(id)
				ON DELETE CASCADE
				ON UPDATE CASCADE
);


CREATE TABLE creators_board_games(
	creator_id INT NOT NULL,
	board_game_id INT NOT NULL,

	CONSTRAINT fk_creators_board_games_creators
		FOREIGN KEY (creator_id)
			REFERENCES creators(id)
				ON DELETE CASCADE
				ON UPDATE CASCADE,

	CONSTRAINT fk_creators_board_games_board_games
		FOREIGN KEY (board_game_id)
			REFERENCES board_games(id)
				ON DELETE CASCADE
				ON UPDATE CASCADE
);