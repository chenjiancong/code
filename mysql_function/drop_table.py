#!/usr/bin/python
#Filename: drop_table.py

import MySQLdb

connect = MySQLdb.connect(
        user = 'root',passwd = 'dbcjc',db = 'testdb',host = 'localhost',charset = 'utf-8'
        )
cursor = connect.cursor()
cursor.execute ('DROP TABLE tb11')

cursor.close()
connect.close()
