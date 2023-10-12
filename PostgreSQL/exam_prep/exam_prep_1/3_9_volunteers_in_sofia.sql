SELECT
	v.name AS volunteers,
	v.phone_number,
	SUBSTRING(TRIM(REPLACE(v.address, 'Sofia', '')), 3)
FROM
	volunteers AS v
	JOIN volunteers_departments as vd
	ON v.department_id = vd.id
WHERE
	address LIKE '%Sofia%'
	AND
	vd.department_name = 'Education program assistant'
ORDER BY
	name