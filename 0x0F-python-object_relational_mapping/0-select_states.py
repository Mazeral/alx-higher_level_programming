#!/usr/bin/python2
import MySQLdb
import sys

db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.excute("SELECT name FROM states ORDER BY id")