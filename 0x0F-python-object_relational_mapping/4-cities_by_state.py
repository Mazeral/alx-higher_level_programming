#!/usr/bin/python3
"""
    A script that lists all the states
    that match the argument of the user
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
    query = """SELECT cities.id, cities.name, states.name\
    FROM cities, states WHERE cities.state_id = states.id
    ORDER BY cities.id ASC"""
    cur.execute(query)
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()
