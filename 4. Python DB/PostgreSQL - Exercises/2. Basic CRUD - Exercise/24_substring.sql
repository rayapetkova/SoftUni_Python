CREATE VIEW view_initials
AS SELECT
		  SUBSTRING(first_name FROM 1 FOR 2) AS "initial",
		  last_name
FROM employees
ORDER BY last_name;





-- second solution:

-- CREATE VIEW view_initials AS
-- SELECT first_name AS "initial", last_name
-- FROM employees
-- ORDER BY last_name;
--
-- UPDATE view_initials
-- SET initial = LEFT(initial, 2);