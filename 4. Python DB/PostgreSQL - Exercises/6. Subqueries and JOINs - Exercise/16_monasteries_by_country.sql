CREATE TABLE monasteries(
	id SERIAL PRIMARY KEY,
	monastery_name VARCHAR(255),
	country_code CHAR(2)
);


INSERT INTO monasteries (monastery_name, country_code)
VALUES ('Rila Monastery "St. Ivan of Rila"', 'BG'),
	   ('Bachkovo Monastery "Virgin Mary"', 'BG'),
	   ('Troyan Monastery "Holy Mother''s Assumption"', 'BG'),
	   ('Kopan Monastery', 'NP'),
	   ('Thrangu Tashi Yangtse Monastery', 'NP'),
	   ('Shechen Tennyi Dargyeling Monastery', 'NP'),
	   ('Benchen Monastery', 'NP'),
	   ('Southern Shaolin Monastery', 'CN'),
	   ('Dabei Monastery', 'CN'),
	   ('Wa Sau Toi', 'CN'),
	   ('Lhunshigyia Monastery', 'CN'),
	   ('Rakya Monastery', 'CN'),
	   ('Monasteries of Meteora', 'GR'),
	   ('The Holy Monastery of Stavronikita', 'GR'),
	   ('Taung Kalat Monastery', 'MM'),
	   ('Pa-Auk Forest Monastery', 'MM'),
	   ('Taktsang Palphug Monastery', 'BT'),
	   ('Sümela Monastery', 'TR');


ALTER TABLE countries
ADD COLUMN "three_rivers" BOOLEAN DEFAULT FALSE;


UPDATE countries
SET three_rivers = TRUE
WHERE (
		SELECT
		   	   COUNT(*)
		FROM countries_rivers AS "cr"
		GROUP BY cr.country_code
	    HAVING cr.country_code = countries.country_code
) >= 3;


SELECT
	   m.monastery_name,
	   c.country_name
FROM monasteries AS "m"
JOIN countries AS "c"
	 ON c.country_code = m.country_code
WHERE c.three_rivers IS FALSE
ORDER BY m.monastery_name ASC;









-- second solution - with WHERE
--
--
-- CREATE TABLE monasteries(
-- 	id SERIAL PRIMARY KEY,
-- 	monastery_name VARCHAR(255),
-- 	country_code CHAR(2)
-- );
--
--
-- INSERT INTO monasteries (monastery_name, country_code)
-- VALUES ('Rila Monastery "St. Ivan of Rila"', 'BG'),
-- 	   ('Bachkovo Monastery "Virgin Mary"', 'BG'),
-- 	   ('Troyan Monastery "Holy Mother''s Assumption"', 'BG'),
-- 	   ('Kopan Monastery', 'NP'),
-- 	   ('Thrangu Tashi Yangtse Monastery', 'NP'),
-- 	   ('Shechen Tennyi Dargyeling Monastery', 'NP'),
-- 	   ('Benchen Monastery', 'NP'),
-- 	   ('Southern Shaolin Monastery', 'CN'),
-- 	   ('Dabei Monastery', 'CN'),
-- 	   ('Wa Sau Toi', 'CN'),
-- 	   ('Lhunshigyia Monastery', 'CN'),
-- 	   ('Rakya Monastery', 'CN'),
-- 	   ('Monasteries of Meteora', 'GR'),
-- 	   ('The Holy Monastery of Stavronikita', 'GR'),
-- 	   ('Taung Kalat Monastery', 'MM'),
-- 	   ('Pa-Auk Forest Monastery', 'MM'),
-- 	   ('Taktsang Palphug Monastery', 'BT'),
-- 	   ('Sümela Monastery', 'TR');
--
--
-- ALTER TABLE countries
-- ADD COLUMN "three_rivers" BOOLEAN DEFAULT FALSE;
--
-- -- ALTER TABLE countries
-- -- DROP COLUMN three_rivers;
--
--
-- UPDATE countries
-- SET three_rivers = TRUE
-- WHERE (
-- 		SELECT
-- 		   	   COUNT(*)
-- 		FROM countries_rivers AS "cr"
-- 		WHERE countries.country_code = cr.country_code
-- ) >= 3;
--
--
-- SELECT
-- 	   m.monastery_name,
-- 	   c.country_name
-- FROM monasteries AS "m"
-- JOIN countries AS "c"
-- 	 ON c.country_code = m.country_code
-- WHERE c.three_rivers IS FALSE
-- ORDER BY m.monastery_name ASC;
