<<<<<<< Updated upstream
SELECT capital,
       TRANSLATE(capital, 'áãåçéíñóú', 'aaaceinou') AS "translated_name"
=======
SELECT
	   capital,
	   TRANSLATE(capital, 'áãåçéíñóú', 'aaaceinou') AS "translated_name"
>>>>>>> Stashed changes
FROM countries;