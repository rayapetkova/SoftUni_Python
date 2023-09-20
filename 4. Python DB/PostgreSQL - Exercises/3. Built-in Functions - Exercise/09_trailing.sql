<<<<<<< Updated upstream
SELECT continent_name,
       TRIM(TRAILING FROM continent_name)
=======
SELECT
	   continent_name,
	   RTRIM(continent_name)
>>>>>>> Stashed changes
FROM continents;