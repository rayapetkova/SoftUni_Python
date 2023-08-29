SELECT apartments.name AS "Name",
apartments.country AS "Country",
bookings.booked_at::date
FROM apartments
LEFT JOIN bookings ON apartments.booking_id = bookings.booking_id
LIMIT 10;