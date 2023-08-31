SELECT mountains_countries.country_code,
mountains.mountain_range,
peaks.peak_name,
peaks.elevation
FROM mountains_countries
JOIN mountains ON mountains.id = mountains_countries.mountain_id
JOIN peaks ON peaks.mountain_id = mountains_countries.mountain_id
WHERE peaks.elevation > 2835 AND mountains_countries.country_code = 'BG'
ORDER BY elevation DESC;
