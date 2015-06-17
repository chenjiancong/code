#!/usr/bin/python
#-*- coding:utf-8 -*-
#Filename: testdb.py

import MySQLdb

connect = MySQLdb.connect(
        user = 'root',passwd = 'dbcjc',db = 'testdb',host = 'localhost',charset = 'utf8'
        )

cursor = connect.cursor()
#cursor.execute("CREATE TABLE IF NOT EXISTS tb1(Text char(20))")
#value = ['你好']
#cursor.execute("INSERT INTO tb1 values(%c)",value)

sql = '''
        INSERT INTO Student VALUES('2015001','AA','M',20,'IS')
       '''

cursor.execute(sql)
connect.commit()
cursor.close()
connect.close()
