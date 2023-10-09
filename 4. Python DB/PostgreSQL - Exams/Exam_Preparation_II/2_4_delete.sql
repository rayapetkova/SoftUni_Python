DELETE FROM clients AS "cl"
WHERE (SELECT
	  		  COUNT(*)
	  FROM courses AS "cou"
	  WHERE cou.client_id = cl.id) = 0
	  AND LENGTH(full_name) > 3;