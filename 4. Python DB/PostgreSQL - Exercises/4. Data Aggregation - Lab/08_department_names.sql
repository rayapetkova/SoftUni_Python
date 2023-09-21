SELECT
	   e.id,
	   e.first_name,
	   e.last_name,
	   ROUND(e.salary, 2),
	   e.department_id,
	   CASE
	   		WHEN e.department_id = 1 THEN 'Management'
			WHEN e.department_id = 2 THEN 'Kitchen Staff'
			WHEN e.department_id = 3 THEN 'Service Staff'
			ELSE 'Other'
	   END
FROM employees AS e
ORDER BY e.id;