-- Shows all the tables from a database name provided by the user
-- Declaring a variable for the databse name
@dbname = ?;

-- Show the tables from a database
SHOW TABLES FROM @dbname;
