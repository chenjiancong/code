#-*- coding: utf-8 -*-
#!/usr/bin/python
#Filename: insert_into_executemany.py

import MySQLdb
connect = MySQLdb.connect(
        user = 'root',passwd = 'dbcjc',db = 'testdb',host = 'localhost',charset = 'utf8'
        )

cursor = connect.cursor()

SQL = """
        INSERT INTO SC VALUES (%s,%s,%s)
        """

args = [
        (20150001,1,92),
        (20150002,2,85),
        (20150003,3,88),
        (20150004,4,70),
        (20150005,5,59),
        (20150006,1,40),
        (20150007,2,100),
        (20150008,6,65)
        ]

cursor.executemany(SQL,args)
connect.commit()
cursor.close()
connect.close()
