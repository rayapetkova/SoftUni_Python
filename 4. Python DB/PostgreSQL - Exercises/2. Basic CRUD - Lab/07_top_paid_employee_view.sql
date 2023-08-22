CREATE VIEW top_paid_employee AS
SELECT id, first_name, last_name, job_title, department_id, salary
FROM employees
WHERE salary = (SELECT max(salary) FROM employees);

SELECT * FROM top_paid_employee;
