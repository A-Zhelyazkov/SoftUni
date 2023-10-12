CREATE OR REPLACE FUNCTION fn_difficulty_level (level INT)
RETURNS VARCHAR(50)
AS
$$
DECLARE
	result VARCHAR(50);
BEGIN
	IF level <= 40 THEN
		result = 'Normal Difficulty';
	ELSIF level <= 60 THEN
		result = 'Nightmare Difficulty';
	ELSIF level > 60 THEN
		result = 'Hell Difficulty';
	END IF;
	RETURN result
		;
END;
$$
LANGUAGE plpgsql;

SELECT
	user_id,
	level,
	cash,
	fn_difficulty_level(level)
FROM
	users_games
ORDER BY
	user_id

