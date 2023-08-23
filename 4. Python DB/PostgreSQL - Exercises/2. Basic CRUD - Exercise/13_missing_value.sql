SELECT id, first_name, last_name
FROM employees
WHERE middle_name is NULL
LIMIT 3;