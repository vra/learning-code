#!/usr/bin/env python

import sqlite3 

#connect database
conn=sqlite3.connect('school.db')

#get cursor
c=conn.cursor()

#insert #1
c.execute("INSERT INTO student VALUES(11210245,'yunfeng',100)")

#insert #2-use '?' to replace unknown datas
c.execute("INSERT INTO student VALUES(?,?,89)",[11210155,'hongwei'])

#insert #3-executemany
students=[(11210250,'jing',100),(11210255,'renai',99)]
c.executemany("INSERT INTO student VALUES(?,?,?)",students)

conn.commit()
conn.close()


#construct data 

