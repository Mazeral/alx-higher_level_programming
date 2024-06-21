#!/usr/bin/python3
"""
    A script that lists all the states and sortes
    them by id
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
    cur.execute("""SELECT name FROM states ORDER BY id ASC""")
    results = cur.fetchall()
    for row in results:
        print(row)
