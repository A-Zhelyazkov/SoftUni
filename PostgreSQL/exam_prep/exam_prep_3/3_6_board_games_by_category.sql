SELECT
	bg.id,
	bg.name,
	bg.release_year,
	c.name
FROM
	board_games AS bg
	JOIN categories AS c
	ON bg.category_id = c.id
WHERE
	c.name = 'Strategy Games'
	OR
	c.name = 'Wargames'
ORDER BY
	release_year DESC