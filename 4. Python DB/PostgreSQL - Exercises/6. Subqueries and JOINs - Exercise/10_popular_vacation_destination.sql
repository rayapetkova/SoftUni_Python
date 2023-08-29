SELECT apartments.country,
COUNT(*) AS "booking_count"
FROM apartments
JOIN bookings ON bookings.apartment_id = apartments.apartment_id
WHERE bookings.booked_at > '2021-05-18 07:52:09.904+03' AND bookings.booked_at < '2021-09-17 19:48:02.147+03'
GROUP BY apartments.country
ORDER BY "booking_count" DESC;