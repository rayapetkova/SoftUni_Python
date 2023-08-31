SELECT MIN(avg_area)
FROM (SELECT AVG(countries.area_in_sq_km) AS "avg_area"
FROM countries
GROUP BY continent_code) AS "min_average_area";