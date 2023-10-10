UPDATE
	countries
SET
	country_name = 'Burma'
WHERE
	country_name = 'Myanmar'
;

INSERT INTO monasteries(monastery_name, country_code)
VALUES
('Hanga Abbey', 'TZ'),
('Myin-Tin-Daik', 'MM');

SELECT
	con.continent_name,
	cou.country_name,
	COUNT(*) AS monasteries_count
FROM
	countries AS cou
LEFT JOIN
	monasteries AS m
USING
	(country_code)
LEFT JOIN
	continents AS con
USING
	(continent_code)
WHERE
	NOT three_rivers
GROUP BY
con.continent_name,
cou.country_name
ORDER BY
	monasteries_count DESC,
	cou.country_name
