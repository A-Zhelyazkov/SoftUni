CREATE OR REPLACE FUNCTION fn_creator_with_board_games(creator_fn VARCHAR(30))
RETURNS INT
AS
$$
BEGIN
	RETURN (
		SELECT
		COUNT(*)
		FROM
			creators AS c
			JOIN creators_board_games AS cbg
			ON c.id = cbg.creator_id
		WHERE
			c.first_name = creator_fn
	);
END;
$$
LANGUAGE plpgsql