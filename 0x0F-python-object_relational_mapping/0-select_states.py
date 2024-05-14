#!/bin/bash

import MySQLdb



conn = MySQLdb.connect(host="localhost", port=3306, user="$1", passwd="$2", db="$3", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") 
query_rows = cur.fetchall()
for row in query_rows:
    print("{}: {}".format(row.id, row.name))
cur.close()
conn.close()