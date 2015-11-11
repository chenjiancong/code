#!/usr/bin/python
#-*- coding:UTF-8 -*-
#Fiename: insert_into_table.py

import MySQLdb

connect = MySQLdb.connect(
        user = 'root',passwd = 'dbcjc',db = 'testdb',host = 'localhost',charset = 'utf8'
        )

cursor = connect.cursor()

#sql = """
#       INSERT INTO Student VALUES('20150004','节是','男','20','IS'),('20150005','小菜','女','19','CS')
#      """

sql = """
        INSERT INTO Student Values(%s,%s,%s,%s,%s)
        """
args =[('2','a1','m','20','IS'),('4','bb','m','18','CS')]
cursor.executemany(sql,args)

connect.commit()
cursor.close()
connect.close()
