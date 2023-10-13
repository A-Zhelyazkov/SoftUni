SELECT
	bg.name,
	bg.rating,
	c.name
FROM
	board_games AS bg
	JOIN categories AS c
	ON c.id = bg.category_id
		JOIN players_ranges AS pr
		ON pr.id = bg.players_range_id
WHERE
	(pr.min_players >= 2 AND pr.max_players <= 5)
	AND
	bg.rating > 7.00
	AND
	(bg.name ILIKE '%a%' OR bg.rating > 7.50)
ORDER BY
	bg.name,
	rating DESC
LIMIT 5