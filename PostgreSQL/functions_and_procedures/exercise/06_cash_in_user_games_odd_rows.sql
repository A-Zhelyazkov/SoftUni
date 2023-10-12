CREATE OR REPLACE FUNCTION fn_cash_in_users_games (game_name VARCHAR(50))
RETURNS TABLE(
	total_cash NUMERIC
)
AS
$$
BEGIN
	RETURN QUERY
	WITH game_finder AS(
		SELECT
			cash,
			ROW_NUMBER() OVER (ORDER by CASH DESC) AS "row"
		FROM
			users_games AS ug
			JOIN games AS g
			ON g.id = ug.game_id
		WHERE
			g.name = game_name
	)
		SELECT
			SUM(ROUND(cash, 2))
		FROM
			game_finder
		WHERE
			"row" % 2 = 1
		;
END;
$$
LANGUAGE plpgsql;