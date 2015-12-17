#!/usr/bin/env python

import sqlite3 as sql

#school.db is a file in working directory
conn=sql.connect("school.db")

#get cursor
c=conn.cursor()

#create tables
c.execute('''CREATE TABLE student
    (id int primary key,name varchar(20),grade float)''')

#commit operations
conn.commit()

#close connection with the database
conn.close()
