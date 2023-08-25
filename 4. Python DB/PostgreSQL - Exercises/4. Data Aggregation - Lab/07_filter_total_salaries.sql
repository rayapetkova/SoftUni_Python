SELECT department_id,
SUM(salary) AS "max_salary"
FROM employees
GROUP BY department_id
HAVING SUM(salary) < 4200
ORDER BY department_id;