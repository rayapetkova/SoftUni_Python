SELECT
	   LTRIM(peak_name, 'M') AS "Left Trim",
	   RTRIM(peak_name, 'm') AS "Rigth Trim"
FROM peaks;