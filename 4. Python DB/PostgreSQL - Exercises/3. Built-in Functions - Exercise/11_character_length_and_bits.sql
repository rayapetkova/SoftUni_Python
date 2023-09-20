SELECT
	   CONCAT(mountains.mountain_range, ' ', peaks.peak_name) AS "Mountain Information",
	   LENGTH(CONCAT(mountains.mountain_range, ' ', peaks.peak_name)) AS "Characters Length",
	   BIT_LENGTH(CONCAT(mountains.mountain_range, ' ', peaks.peak_name)) AS "Bits of a String"
FROM mountains
JOIN peaks ON mountains.id = peaks.mountain_id;