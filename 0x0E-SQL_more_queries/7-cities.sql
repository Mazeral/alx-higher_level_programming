-- A script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_it INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_it) REFERENCES states(id)
);
