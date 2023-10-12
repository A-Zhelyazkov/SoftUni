SELECT
	a.name,
	CASE
		WHEN EXTRACT('hour' FROM cou.start) BETWEEN 6 and 20 THEN 'Day'
		ELSE 'Night'
	END AS day_time,
	cou.bill,
	cli.full_name,
	car.make,
	car.model,
	cat.name
FROM
	courses AS cou
		JOIN cars AS car
			ON cou.car_id = car.id
				JOIN categories AS cat
					ON car.category_id = cat.id
						JOIN addresses AS a
							ON cou.from_address_id = a.id
								JOIN clients AS cli
									ON cou.client_id = cli.id
ORDER BY
	cou.id