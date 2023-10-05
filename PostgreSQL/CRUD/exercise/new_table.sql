CREATE TABLE IF NOT EXISTS company_chart
AS
SELECT
	CONCAT(first_name, ' ', last_name) as "Full Name",
	job_title AS "Job Title",
	department_id AS "Department ID",
	manager_id AS "Manager ID"
FROM
	employees