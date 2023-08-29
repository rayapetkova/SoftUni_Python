SELECT CONCAT(apartments.address, ' ', apartments.address_2) AS "Apartment Address",
bookings.booked_for AS "Nights"
FROM apartments
JOIN bookings ON bookings.booking_id = apartments.booking_id
ORDER BY apartments.apartment_id ASC;