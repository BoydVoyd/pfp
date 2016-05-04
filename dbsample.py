#!/usr/bin/python
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='pfpsite' user='hiro' host='localhost' password='$n0wCrash'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
cur.execute("""SELECT eth_type, protocol from pfp_ethtypes""")
rows = cur.fetchall()
for row in rows:
    print "{}: {}".format(row[0], row[1])
