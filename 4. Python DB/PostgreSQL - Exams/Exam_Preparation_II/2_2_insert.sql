INSERT INTO clients(full_name, phone_number)
SELECT
		  CONCAT(d.first_name, ' ', d.last_name),
		  CONCAT('(088) 9999', CAST(d.id*2 AS TEXT))
FROM drivers AS "d"
WHERE d.id BETWEEN 10 AND 20;