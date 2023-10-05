CREATE TABLE IF NOT EXISTS bookings_calculation
AS
SELECT
	booked_for
FROM
	bookings
WHERE
	apartment_id = 93;

ALTER TABLE bookings_calculation
ADD COLUMN multiplication NUMERIC,
ADD COLUMN modulo NUMERIC;

UPDATE bookings_calculation
SET modulo = booked_for % 50,
	multiplication = booked_for * 50