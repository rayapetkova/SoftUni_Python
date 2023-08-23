CREATE VIEW view_addresses AS
SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
	   department_id,
       CONCAT(addresses.number, ' ', addresses.street) AS "Address"
FROM employees
JOIN addresses ON employees.address_id = addresses.id
ORDER BY "Address";