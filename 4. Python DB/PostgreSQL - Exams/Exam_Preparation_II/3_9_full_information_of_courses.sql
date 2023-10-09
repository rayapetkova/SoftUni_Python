SELECT
	   a.name,
	   CASE
		    WHEN EXTRACT(HOUR FROM cou.start) BETWEEN 6 AND 20 THEN 'Day'
		    ELSE 'Night'
	   END AS "day_time",
	   cou.bill,
	   clients.full_name,
	   cars.make,
	   cars.model,
	   categories.name
FROM courses AS "cou"
JOIN addresses AS "a" ON a.id = cou.from_address_id
JOIN clients ON cou.client_id = clients.id
JOIN cars ON cou.car_id = cars.id
JOIN categories ON cars.category_id = categories.id
ORDER BY cou.id;