create or replace procedure sp_increase_salaries(
   department_name text
)
language plpgsql
as $$
begin

	UPDATE employees
    SET salary = salary + (0.05 * salary)
    WHERE employees.department_id = (
	SELECT departments.department_id
	FROM departments
	WHERE departments.name = department_name
	);

    commit;
end;$$