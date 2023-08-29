SELECT apartments.name,
SUM(bookings.booked_for)
FROM apartments
JOIN bookings ON bookings.apartment_id = apartments.apartment_id
GROUP BY apartments.name
ORDER BY apartments.name ASC;