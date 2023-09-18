SELECT first_name,
	   last_name,
	   EXTRACT(YEAR FROM born) AS "year"
FROM authors;