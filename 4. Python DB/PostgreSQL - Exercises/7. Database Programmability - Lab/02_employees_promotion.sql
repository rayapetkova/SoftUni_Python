CREATE OR REPLACE PROCEDURE sp_increase_salaries(
	department_name VARCHAR
) AS
$$
   BEGIN
   		 UPDATE employees
		 SET salary = salary + (0.05 * salary)
		 WHERE employees.department_id = (
		 SELECT 
			    d.department_id
		 FROM departments AS "d"
		 WHERE d.name = department_name
		 );
   END;
$$
LANGUAGE plpgsql;
