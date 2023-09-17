CREATE VIEW view_addresses
AS SELECT
		  CONCAT(employees.first_name, ' ', employees.last_name) AS "Full Name",
		  employees.department_id,
		  CONCAT(addresses.number, ' ', addresses.street) AS "Address"
FROM employees, addresses
WHERE employees.address_id = addresses.id
ORDER BY "Address";






-- second solution:

-- CREATE VIEW view_addresses AS
-- SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
-- 	   department_id,
--        CONCAT(addresses.number, ' ', addresses.street) AS "Address"
-- FROM employees
-- JOIN addresses ON employees.address_id = addresses.id
-- ORDER BY "Address";
