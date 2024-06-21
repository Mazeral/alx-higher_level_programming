#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[0],
                     passwd=sys.argv[1], db=sys.argv[2])
cur = db.cursor()
cur.excute("SELECT states FROM hbtn_0e_0_usa ORDER BY id")
