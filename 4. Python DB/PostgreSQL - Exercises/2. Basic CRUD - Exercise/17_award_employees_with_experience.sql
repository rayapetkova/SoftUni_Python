UPDATE employees
SET job_title = CONCAT('Senior ', job_title),
    salary = salary + 1500
WHERE hire_date BETWEEN 'January 1, 1998' AND 'January 5, 2000';