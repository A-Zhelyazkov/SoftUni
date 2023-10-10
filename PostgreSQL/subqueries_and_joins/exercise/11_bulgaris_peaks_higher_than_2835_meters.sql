SELECT
	mc.country_code,
	m.mountain_range,
	p.peak_name,
	p.elevation
FROM
	mountains AS m
	JOIN peaks AS p
	ON m.id = p.mountain_id

	JOIN mountains_countries AS mc
	ON mc.mountain_id = m.id
WHERE
	elevation > 2835
	AND
	country_code = 'BG'
ORDER BY
	elevation desc