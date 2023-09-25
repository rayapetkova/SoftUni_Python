CREATE OR REPLACE VIEW
			view_performance_rating
AS SELECT
		  e.first_name,
		  e.last_name,
		  e.job_title,
		  e.salary,
		  e.department_id,
		  CASE
		  	   WHEN salary >= 25000 THEN
			   		CASE
						 WHEN job_title LIKE 'Senior%' THEN 'High-performing Senior'
						 WHEN job_title NOT LIKE 'Senior%' THEN 'High-performing Employee'
						 ELSE 'Average-performing'
					END
			   ELSE 'Average-performing'
		  END AS "performance_rating"
FROM employees AS e;








-- second solution

-- CREATE VIEW
-- 			view_performance_rating
-- AS SELECT
-- 		  e.first_name,
-- 		  e.last_name,
-- 		  e.job_title,
-- 		  e.salary,
-- 		  e.department_id,
-- 		  CASE
-- 		  	   WHEN salary >= 25000 AND job_title LIKE 'Senior%' THEN 'High-performing Senior'
-- 			   WHEN salary >= 25000 AND job_title NOT LIKE 'Senior%' THEN 'High-performing Employee'
-- 		  	   ELSE 'Average-performing'
-- 		  END AS "performance_rating"
-- FROM employees AS e;