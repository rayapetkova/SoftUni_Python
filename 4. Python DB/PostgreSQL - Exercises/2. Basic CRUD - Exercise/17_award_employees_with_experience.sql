UPDATE employees
SET salary = salary + 1500,
	job_title = CONCAT('Senior ', job_title)
WHERE hire_date BETWEEN 'January 1, 1998' AND 'January 5, 2000';