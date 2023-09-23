SELECT
	   last_name,
	   COUNT(notes)
FROM wizard_deposits
WHERE notes LIKE '%Dumbledore%'
GROUP BY last_name