SELECT
	COUNT(*) as countries_without_rivers
FROM
	countries
LEFT JOIN
	countries_rivers
USING
	(country_code)
WHERE countries_rivers.country_code IS NULL