SELECT
	CONCAT(mou.mountain_range, ' ', p.peak_name) AS "Mountain Information",
	LENGTH(CONCAT(mou.mountain_range, ' ', p.peak_name)) as "Characters Length",
	BIT_LENGTH(CONCAT(mou.mountain_range, ' ', p.peak_name)) AS "Bits of a String"
FROM
	mountains as mou,
	peaks as p
WHERE
	mou.id = p.mountain_id