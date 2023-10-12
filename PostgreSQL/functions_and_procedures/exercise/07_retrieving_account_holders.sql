CREATE OR REPLACE PROCEDURE
	sp_retrieving_holders_with_balance_higher_than(searched_balance NUMERIC)
AS
$$
DECLARE
	account_info RECORD;
BEGIN
		FOR account_info IN
		SELECT
			CONCAT(ah.first_name, ' ', ah.last_name) as full_name,
			SUM(a.balance) AS total_balance
		FROM
			account_holders AS ah
			JOIN accounts AS a
			ON ah.id = a.account_holder_id
		GROUP BY
			full_name
		HAVING
			SUM(a.balance) > searched_balance
		ORDER BY
			full_name
		LOOP
			RAISE NOTICE '% - %', account_info.full_name, account_info.total_balance;
		END LOOP;
END;
$$
LANGUAGE plpgsql;