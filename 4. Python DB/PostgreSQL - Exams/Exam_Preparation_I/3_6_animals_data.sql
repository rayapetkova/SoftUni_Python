SELECT
	   a.name,
	   at.animal_type,
	   TO_CHAR(a.birthdate, 'DD.MM.YYYY')
FROM animals AS "a"
JOIN animal_types AS "at"
	 ON at.id = a.animal_type_id
ORDER BY name ASC;