SELECT bookings.booking_id,
bookings.apartment_id,
customers.companion_full_name
FROM bookings
JOIN customers ON bookings.customer_id = customers.customer_id
WHERE apartment_id IS NULL;