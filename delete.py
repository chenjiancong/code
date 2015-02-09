#-*- coding: UTF-8 -*-
#!/usr/bin/python
#Filename: delete.py

import MySQLdb

connect = MySQLdb.connect(
        user = 'root', passwd = 'dbcjc', host = 'localhost', db = 'testdb', charset = 'utf8'
        )

cursor = connect.cursor()

SQL = """
        DELETE FROM Student WHERE Sno = '1' OR Sno = '4'
        """

cursor.execute(SQL)
connect.commit()
cursor.close()
connect.close()
