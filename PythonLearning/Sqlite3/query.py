#!/usr/bin/env python

import sqlite3 

conn=sqlite3.connect("school.db")
c=conn.cursor()

#query #1-fetchone
c.execute('SELECT name FROM student ORDER BY grade')
print(c.fetchone())
print(c.fetchone())

#query #2-fetchall
c.execute('SELECT id FROM student')
print(c.fetchall())

#query #3-iterator
for row in c.execute('SELECT id,name,grade FROM student ORDER BY id'):
    print(row)

