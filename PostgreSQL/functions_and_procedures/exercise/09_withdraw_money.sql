CREATE OR REPLACE PROCEDURE sp_withdraw_money(
	account_id INT,
	money_amount NUMERIC(20,4)
)
AS
$$
DECLARE
	curr_balance NUMERIC;
BEGIN
	curr_balance = (SELECT balance FROM accounts WHERE id = account_id);
	IF curr_balance - money_amount > 0 THEN
		UPDATE accounts
		SET balance = balance - money_amount
		WHERE id = account_id;
	ELSE
		RAISE NOTICE 'Unsufficient balance to withdraw %', curr_balance;
	END IF;
END;
$$
LANGUAGE plpgsql