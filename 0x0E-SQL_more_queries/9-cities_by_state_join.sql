-- A script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, citites.name, states.name FROM citites INNER JOIN states ON states.id = citites.state_id ORDER BY citites.id; 
