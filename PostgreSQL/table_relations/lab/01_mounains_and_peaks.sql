CREATE TABLE Mountains(
	id SERIAL PRIMARY KEY,
	name VARCHAR(30)
);

CREATE TABLE Peaks(
	id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	mountain_id INT,
	CONSTRAINT fk_peaks_mountains
		FOREIGN KEY(mountain_id)
			REFERENCES Mountains(id)

)