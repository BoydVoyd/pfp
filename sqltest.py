#/usr/bin/python2.7
#
#

import psycopg2

# Try to connect

try:
    conn=psycopg2.connect("dbname='hiro' user='hiro' password='$nowCrash'")
except:
    print "I am unable to connect to the database."
insertstring = """INSERT INTO persons (LastName, FirstName,
               Address, City)
               VALUES (%s, %s, %s, %s);"""
libby = ['Mcnairy', 'Libby', '555 Main Street','Brentwood']

bobby = ['Dobbs', 'Bob', '2112 Slack Street','Mars']

cur = conn.cursor()
cur.execute(insertstring, libby)
cur.execute(insertstring, bobby)
conn.commit()
