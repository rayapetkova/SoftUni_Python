CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(
	id INT
) AS
$$
   BEGIN
   		 IF (SELECT COUNT(*) FROM employees WHERE employee_id = id) = 1 THEN
			 UPDATE employees
			 SET salary = salary + (0.05 * salary)
			 WHERE employee_id = id;
		 END IF;
   END;
$$
LANGUAGE plpgsql;