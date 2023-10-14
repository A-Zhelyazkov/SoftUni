UPDATE coaches
SET salary = c.salary * c.coach_level
FROM
	players_coaches AS pc
	JOIN coaches AS c
	ON c.id = pc.coach_id
WHERE
	c.first_name LIKE 'C%'