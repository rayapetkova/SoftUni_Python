create or replace procedure sp_increase_salary_by_id(
   id int
)
language plpgsql
as $$
begin

	UPDATE employees
    SET salary = salary + (0.05 * salary)
    WHERE employees.employee_id = id;

    commit;
end;$$