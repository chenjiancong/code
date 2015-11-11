#-*- coding:utf-8 -*-
#!/usr/bin/python
#Filename: print_select.py
import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
connect = MySQLdb.connect(
        user = 'root',
        passwd = 'dbcjc',
        db = 'testdb',
        host = 'localhost',
        charset = 'utf8'
        )

cursor = connect.cursor()

SQL = """
    SELECT Cname FROM Course
        """
aa = cursor.execute(SQL)
#print '总共有',aa

info = cursor.fetchmany(aa)

for ii in info:
    print ii

ii.encode('utf-8')
connect.commit()
cursor.close()
connect.close()

