--  A script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
CREATE table IF NOT EXISTS second_table (
	`id` INT,
	`name` VARCHAR(256),
	`score` INT
);
-- create these records:
--     id = 1, name = “John”, score = 10
--     id = 2, name = “Alex”, score = 3
--     id = 3, name = “Bob”, score = 14
--     id = 4, name = “George”, score = 8
INSERT INTO `second_table` (`id`, `name`, `score`)
VALUES (1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8);
