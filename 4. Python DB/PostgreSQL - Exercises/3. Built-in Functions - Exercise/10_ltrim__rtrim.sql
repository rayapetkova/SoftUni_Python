SELECT TRIM(LEADING 'M' FROM peak_name) AS "Left Trim",
TRIM(TRAILING 'm' FROM peak_name) AS "Right Trim"
FROM peaks;