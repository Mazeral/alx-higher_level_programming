-- A script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE TABLE states(
	PRIMARY KEY id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR (256)
);
