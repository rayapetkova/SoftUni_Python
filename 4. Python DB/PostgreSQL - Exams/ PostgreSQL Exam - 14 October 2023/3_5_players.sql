SELECT
       CONCAT(first_name, ' ', last_name) AS "full_name",
       age,
       hire_date
FROM players
WHERE first_name LIKE 'M%'
ORDER BY age DESC, full_name ASC;