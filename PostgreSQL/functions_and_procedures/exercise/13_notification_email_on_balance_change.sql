CREATE TABLE notification_emails(
	id SERIAL PRIMARY KEY,
	recipient_id INT,
	subject VARCHAR(150),
	body TEXT
);

CREATE OR REPLACE FUNCTION trigger_fn_send_email_on_balance_change()
RETURNS TRIGGER
AS
$$
BEGIN
	INSERT INTO notification_emails(recipient_id, subject, body)
	VALUES
		(
		NEW.account_id,
		'Balance change for account: ' || account_id,
		CONCAT('On', DATE(), ' your balance was changed from ', OLD.old_sum, ' to ', NEW.new_sum, '.')
	);
	RETURN NEW;
END;
$$
LANGUAGE plpgsql
;

CREATE OR REPLACE TRIGGER tr_send_email_on_balance_change
AFTER UPDATE ON logs
FOR EACH ROW
WHEN
	(OLD.new_sum != NEW.new_sum)
EXECUTE PROCEDURE trigger_fn_send_email_on_balance_change()