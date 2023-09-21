SELECT
	   department_id,
	   SUM(salary)
FROM employees
GROUP BY department_id
ORDER BY department_id;