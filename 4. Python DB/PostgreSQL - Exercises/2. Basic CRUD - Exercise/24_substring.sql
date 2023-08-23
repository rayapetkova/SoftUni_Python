CREATE VIEW view_initials AS
SELECT first_name AS "initial", last_name
FROM employees
ORDER BY last_name;

UPDATE view_initials
SET initial = LEFT(initial, 2);