#!/usr/bin/python3
"""
    A script that lists all the states starting with
    letter 'N'
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
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(query)
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()
