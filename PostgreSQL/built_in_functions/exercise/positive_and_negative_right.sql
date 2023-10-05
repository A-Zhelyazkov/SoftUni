SELECT
	peak_name,
	RIGHT(peak_name, 4) as "Positive Right",
	Right(peak_name, -4) as "Negative Right"
FROM
	peaks