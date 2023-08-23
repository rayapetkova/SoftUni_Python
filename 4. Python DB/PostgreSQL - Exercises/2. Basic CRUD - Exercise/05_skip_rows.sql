SELECT id, CONCAT(first_name, ' ', middle_name, ' ', last_name) AS "Full Name",
       hire_date AS "Hire Date"
FROM employees
ORDER BY hire_date ASC
OFFSET 9;
