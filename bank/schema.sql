\i schema_drop.sql

CREATE TABLE IF NOT EXISTS Investors(
	user_ID integer PRIMARY KEY,
	password varchar(120),
	name varchar(120),
	balance integer 
);

CREATE TABLE IF NOT EXISTS Portfolios(
	record_ID SERIAL PRIMARY KEY,
	user_ID integer REFERENCES Investors(user_ID),
	ticker_symbol varchar(20),
	purchase_price integer,
	quantity integer
);

CREATE TABLE IF NOT EXISTS Market(
	ticker_symbol varchar(20) PRIMARY KEY, 
	current_price integer 
);











