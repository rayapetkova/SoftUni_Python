ALTER TABLE bookings
ADD COLUMN billing_day TIMESTAMPZ DEFAULT CURRENT_TIMESTAMP;

SELECT TO_CHAR(billing_day, 'DD "Day" MM "Month" YYYY "Year" HH24:MI:SS') AS "Billing Day"
FROM bookings;