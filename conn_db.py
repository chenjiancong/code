#/usr/bin/python
# Filename: conn_db.py

import MySQLdb

connect = MySQLdb.connect(
        user = 'root',passwd = 'dbcjc',db = 'testdb',host = 'localhost',charset = 'utf-8'
        )

cursor = connect.cursor()

cursor.execute('create table tab1(id int,name char(20))')

cursor.close()
connect.close()
