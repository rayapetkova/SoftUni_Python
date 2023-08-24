UPDATE countries
SET iso_code = upper(LEFT(country_name, 3))
WHERE iso_code is NULL;