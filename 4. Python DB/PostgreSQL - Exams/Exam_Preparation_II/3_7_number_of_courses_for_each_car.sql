SELECT
	   c.id,
	   c.make,
	   c.mileage,
	   COUNT(cou.id) AS "count_of_courses",
	   ROUND(AVG(cou.bill), 2)
FROM cars AS "c"
LEFT JOIN courses AS "cou" ON c.id = cou.car_id
GROUP BY c.id, c.make, c.mileage
HAVING COUNT(*) <> 2
ORDER BY count_of_courses DESC, c.id;