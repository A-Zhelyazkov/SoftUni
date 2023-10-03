CREATE TABLE minions_birthdays(
	id INTEGER NOT NULL UNIQUE,
	name VARCHAR(50),
	date_of_birth DATE,
	age INTEGER,
	present VARCHAR(100),
	party TIMESTAMPTZ
)