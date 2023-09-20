<<<<<<< Updated upstream
SELECT continent_name,
       TRIM(LEADING FROM continent_name)
=======
SELECT
	   continent_name,
	   LTRIM(continent_name)
>>>>>>> Stashed changes
FROM continents;