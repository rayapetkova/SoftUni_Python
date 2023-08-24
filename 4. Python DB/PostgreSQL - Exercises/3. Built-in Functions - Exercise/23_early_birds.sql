SELECT user_id,
       AGE(starts_at, booked_at) AS "Early Birds"
FROM bookings
WHERE AGE(starts_at, booked_at) > INTERVAL '10 months';