CREATE VIEW view_continents_countries_currencies_details AS
SELECT CONCAT(continents.continent_name, ': ', continents.continent_code) AS "Continent Details",
       CONCAT(countries.country_name, ' - ', countries.capital, ' - ', countries.area_in_sq_km, ' - ', 'km2') AS "Country Information",
       CONCAT(currencies.description, ' (', currencies.currency_code, ')') AS "Currencies"
FROM continents
JOIN countries ON continents.continent_code = countries.continent_code
JOIN currencies ON countries.currency_code = currencies.currency_code
ORDER BY "Country Information" ASC, "Currencies" ASC;