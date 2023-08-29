SELECT employees_projects.employee_id,
CONCAT(employees.first_name, ' ', employees.last_name) AS "full_name",
projects.project_id,
projects.name
FROM employees_projects
JOIN employees ON employees.employee_id = employees_projects.employee_id
JOIN projects ON projects.project_id = employees_projects.project_id
WHERE projects.name = 'Classic Vest';