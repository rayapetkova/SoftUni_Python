create or replace procedure sp_increase_salaries(
   department_name text
) AS
$$
BEGIN

	UPDATE employees
    SET salary = salary + (0.05 * salary)
    WHERE employees.department_id = (
	SELECT departments.department_id
	FROM departments
	WHERE departments.name = department_name
	);

END;
$$
language plpgsql