SELECT mountains_countries.country_code,
COUNT(*) AS "mountain_range_count"
FROM mountains_countries
JOIN mountains ON mountains_countries.mountain_id = mountains.id
WHERE mountains_countries.country_code IN ('US', 'RU', 'BG')
GROUP BY mountains_countries.country_code
ORDER BY mountain_range_count DESC;