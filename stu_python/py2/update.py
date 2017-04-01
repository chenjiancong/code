#-*- coding: UTF-8 -*-
#/usr/bin/python
#Filename: update.py

import MySQLdb

connect = MySQLdb.connect(
        user = 'root',passwd = 'dbcjc',db = 'testdb',host = 'localhost',charset = 'utf8'
        )

cursor = connect.cursor()

SQL = """
        UPDATE Student SET Sage = '18' WHERE Sno = '20150001'
        """

cursor.execute(SQL)
connect.commit()
cursor.close()
connect.rollback()
connect.close()
