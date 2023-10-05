SELECT
	first_name,
	last_name,
	TO_CHAR(born, 'YYYY') as year
FROM
	authors
