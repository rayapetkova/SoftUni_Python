SELECT id,
       CONCAT(first_name, ' ', last_name) as "full_name",
       job_title, salary
FROM employees
WHERE salary > 1000.00 ORDER BY id;
