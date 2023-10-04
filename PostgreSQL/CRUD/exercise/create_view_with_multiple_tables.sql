CREATE VIEW view_addresses
AS
SELECT
	CONCAT(first_name, ' ', last_name) AS "full name",
	department_id,
	CONCAT(number, ' ', street) AS Address
FROM
	employees,
	addresses
WHERE
	employees.address_id = addresses.id
ORDER BY Address