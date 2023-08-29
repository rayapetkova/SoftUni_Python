SELECT employees.employee_id,
CONCAT(employees.first_name, ' ', employees.last_name),
departments.department_id,
departments.name
FROM employees
JOIN departments ON departments.manager_id = employees.employee_id
ORDER BY employees.employee_id
LIMIT 5;