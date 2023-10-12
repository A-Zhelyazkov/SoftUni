SELECT
	a.name,
	EXTRACT('year' FROM a.birthdate),
	at.animal_type
FROM
	animals AS a
	LEFT JOIN animal_types AS at
	ON a.animal_type_id = at.id
WHERE
	at.animal_type != 'Birds'
	AND
	AGE('01/01/2022', birthdate) < '5 years'
	AND
	owner_id IS NULL
ORDER BY
	a.name
