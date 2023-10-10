SELECT
	b.booking_id,
	c.first_name AS customer_name
FROM customers AS c
	CROSS JOIN bookings AS b
ORDER BY
	customer_name