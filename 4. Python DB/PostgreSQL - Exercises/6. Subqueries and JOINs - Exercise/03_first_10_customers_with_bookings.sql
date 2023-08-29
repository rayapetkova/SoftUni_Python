SELECT bookings.booking_id AS "Booking ID",
bookings.starts_at::date AS "Start Date",
bookings.apartment_id AS "Apartment ID",
CONCAT(customers.first_name, ' ', customers.last_name) AS "Customer Name"
FROM bookings
RIGHT JOIN customers ON customers.customer_id = bookings.customer_id
ORDER BY "Customer Name" ASC
LIMIT 10;