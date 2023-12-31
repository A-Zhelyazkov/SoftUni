SELECT
	MIN(average) as min_average_area
FROM (SELECT
	  	AVG(area_in_sq_km) AS average
	  FROM
	  	countries
	  GROUP BY
	  	continent_code) AS avg_area