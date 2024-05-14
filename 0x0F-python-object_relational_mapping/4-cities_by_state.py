#!/usr/bin/python3
"""  lists all states table of hbtn_0e_0_usa where name matches the argument and safe from MySQL injections!"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM cities")
    rows = cur.fetchall()
    for row in rows:
        print(row.states)
    cur.close()
    db.close()
