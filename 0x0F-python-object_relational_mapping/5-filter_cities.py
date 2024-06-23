#!/usr/bin/python3
"""
    a script that takes in the name of a state as an argument
    and lists all cities of that state,
    using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    # First, you need to join the 2 tables on a common key
    # After that, you will select the table you want to fetch the data from
    # Finally, select the data (Remember that this is how SQL works!)
    query = """SELECT cities.name FROM cities\
            FROM states, cities\
            WHERE states.name LIKE BINARY %s\
            INNER JOIN states ON cities.state_id = states.id"""
    cur.execute(query, (sys.argv[4],))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()
