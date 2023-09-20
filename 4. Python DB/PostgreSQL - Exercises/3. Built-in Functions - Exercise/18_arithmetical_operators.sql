CREATE TABLE bookings_calculation
AS SELECT
		  bookings.booked_for
FROM bookings
WHERE apartment_id = 93;

ALTER TABLE bookings_calculation
ADD COLUMN multiplication NUMERIC,
ADD COLUMN modulo NUMERIC;

UPDATE bookings_calculation
SET multiplication = booked_for * 50,
	modulo = booked_for % 50;