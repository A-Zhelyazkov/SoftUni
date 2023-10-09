SELECT
	e.employee_id,
	CONCAT(first_name, ' ', last_name),
	p.project_id,
	p.name
FROM employees AS e
	JOIN employees_projects AS ep
		ON e.employee_id = ep.employee_id
			JOIN projects as p
				ON p.project_id = ep.project_id
WHERE p.project_id = 1