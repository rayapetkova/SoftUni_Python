SELECT *
FROM departments
INNER JOIN employees ON
departments.id = employees.department_id;