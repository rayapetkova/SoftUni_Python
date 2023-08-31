SELECT COUNT(*) AS "countries_without_mountains"
FROM countries
WHERE countries.country_code NOT IN
(SELECT mountains_countries.country_code FROM mountains_countries);