CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(
	IN animal_name VARCHAR(30),
	OUT owner VARCHAR(50)
)
AS
$$
BEGIN
	SELECT INTO owner
		o.name
	FROM
		animals AS a
		LEFT JOIN owners AS o
		ON a.owner_id = o.id
	WHERE
		a.name = animal_name;
	IF owner IS NULL THEN
		owner := 'For adoption';
	END IF;
	RETURN;
END;
$$
LANGUAGE plpgsql