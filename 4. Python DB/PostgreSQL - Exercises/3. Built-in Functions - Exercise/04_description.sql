UPDATE currencies
SET description = SUBSTRING(description, 5, LENGTH(description));

SELECT description AS "substring"
FROM currencies;