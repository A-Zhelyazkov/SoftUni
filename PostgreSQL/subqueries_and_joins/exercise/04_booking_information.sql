SELECT
	b.booking_id,
	a.name AS apartment_owner,
	a.apartment_id,
	CONCAT(c.first_name, ' ', c.last_name) AS customer_name
FROM customers AS c
	FULL JOIN bookings AS b
		ON b.customer_id = c.customer_id
			FULL JOIN apartments AS a
				ON b.booking_id = a.booking_id
ORDER BY
	b.booking_id,
	apartment_owner,
	customer_name
