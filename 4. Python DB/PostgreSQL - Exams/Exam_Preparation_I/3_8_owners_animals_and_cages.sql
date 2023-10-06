SELECT
	   CONCAT(o.name, ' - ', a.name) AS "Owners - Animals",
	   o.phone_number AS "Phone Number",
	   ac.cage_id AS "Cage ID"
FROM animals AS "a"
JOIN owners AS "o"
	 ON a.owner_id = o.id
JOIN animals_cages AS "ac"
	 ON ac.animal_id = a.id
WHERE a.animal_type_id = 1
ORDER BY o.name ASC, a.name DESC;