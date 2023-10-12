CREATE OR REPLACE FUNCTION fn_full_name (first_name VARCHAR(50), last_name VARCHAR(50))
RETURNS VARCHAR(100)
AS
$$
DECLARE
	full_name VARCHAR(50);
BEGIN
	full_name = CONCAT(INITCAP(first_name), ' ', INITCAP(last_name));
	RETURN full_name;
END;
$$
LANGUAGE plpgsql;