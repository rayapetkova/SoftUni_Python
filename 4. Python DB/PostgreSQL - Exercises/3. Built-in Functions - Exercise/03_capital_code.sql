ALTER TABLE countries
ADD COLUMN capital_code TEXT; -- we can write CHAR(2) too

UPDATE countries
SET capital_code = SUBSTRING(capital, 1, 2);