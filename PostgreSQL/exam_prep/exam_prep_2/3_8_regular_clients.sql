SELECT
	cl.full_name,
	COUNT(co.car_id),
	SUM(co.bill)
FROM
	clients AS cl
	JOIN courses AS co
	ON cl.id = co.client_id
WHERE
	SUBSTRING(full_name FROM 2 FOR 1) = 'a'
GROUP BY
	cl.full_name
HAVING
	COUNT(co.car_id) > 1
ORDER BY
	cl.full_name