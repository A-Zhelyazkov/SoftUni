SELECT
	id AS ID,
	CONCAT(first_name,
		   ' ',
		   middle_name,
		   ' ',
		   last_name) AS "Full Name",
	hire_date as "Hire Date"
FROM
	employees
ORDER BY hire_date
OFFSET 9