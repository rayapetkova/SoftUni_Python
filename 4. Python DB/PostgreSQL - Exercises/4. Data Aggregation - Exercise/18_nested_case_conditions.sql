CREATE VIEW view_performance_rating AS
SELECT first_name,
	   last_name,
	   job_title,
	   salary,
	   department_id,
	   CASE
	   	   WHEN salary >= 25000 THEN
		   CASE
		       WHEN LEFT(job_title, 6) = 'Senior' THEN 'High-performing Senior'
			   WHEN LEFT(job_title, 6) != 'Senior' THEN 'High-performing Employee'
		   	   ELSE 'Average-performing'
		   END
		   ELSE 'Average-performing'
	   END AS "performance_rating"
FROM employees;