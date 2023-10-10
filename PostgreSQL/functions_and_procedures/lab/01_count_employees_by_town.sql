CREATE FUNCTION fn_count_employees_by_town(town_name VARCHAR)
RETURNS VARCHAR AS
$$
	BEGIN
		RETURN(
			SELECT
		COUNT(*)
	FROM
		employees AS e
		JOIN addresses AS a
		USING(address_id)

		JOIN towns AS t
		USING(town_id)
	WHERE
		a.address_id = e.address_id
		AND
		t.name = town_name
	GROUP BY
		t.name
			);
	END
$$
LANGUAGE plpgsql
