SELECT
	   *
FROM
	 departments AS "d"
JOIN employees AS "e"
ON d.id = e.department_id;