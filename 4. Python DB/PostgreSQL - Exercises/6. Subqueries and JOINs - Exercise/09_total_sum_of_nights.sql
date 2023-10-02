SELECT
	   a.name,
	   SUM(b.booked_for)
FROM apartments AS "a"
JOIN bookings AS "b"
	 ON a.apartment_id = b.apartment_id
GROUP BY a.name
ORDER BY a.name ASC;