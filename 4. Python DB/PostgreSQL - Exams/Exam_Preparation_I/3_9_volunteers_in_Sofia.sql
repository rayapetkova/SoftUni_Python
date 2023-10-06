SELECT
	   name,
	   phone_number,
	   SUBSTRING(TRIM(address), 8, LENGTH(address)) AS "address"
FROM volunteers
WHERE department_id = 2 AND SUBSTRING(TRIM(address), 1, 5) = 'Sofia'
ORDER BY name ASC;