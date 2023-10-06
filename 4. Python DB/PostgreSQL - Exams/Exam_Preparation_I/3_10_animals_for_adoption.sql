SELECT
	   a.name,
	   EXTRACT(YEAR FROM a.birthdate) AS "birth_year",
	   at.animal_type
FROM animals AS "a"
JOIN animal_types AS "at"
	 ON a.animal_type_id = at.id
WHERE at.animal_type != 'Birds'
	  AND a.owner_id IS NULL
	  AND a.birthdate > '2017-01-01'
ORDER BY a.name ASC;