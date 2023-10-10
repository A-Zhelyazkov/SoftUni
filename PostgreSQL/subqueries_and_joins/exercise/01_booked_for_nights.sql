SELECT
	CONCAT (a.address, ' ', a.address_2) AS apartment_address,
	booked_for AS nights
FROM bookings AS b
	JOIN apartments AS a
	ON b.booking_id = a.booking_id
ORDER BY
	a.apartment_id