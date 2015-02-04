#!/usr/bin/python
#Filename: create_tables.py

import MySQLdb

connect = MySQLdb.connect(
       user = 'root', passwd = 'dbcjc',db = 'testdb',host = 'localhost',charset = 'utf-8'
        )

cursor = connect.cursor()
#cursor.execute('DROP TABLE Course')
#cursor.execute('CREATE TABLE IF NOT EXISTS Student(Sno CHAR(9) PRIMARY KEY,Sname CHAR(20) UNIQUE,Ssex CHAR(2),Sage SMALLINT,Sdept CHAR(20))')
cursor.execute('CREATE TABLE IF NOT EXISTS Course(Cno char(4) PRIMARY KEY,Cname CHAR(20),Cpno CHAR(4),Ccredit SMALLINT,FOREIGN KEY(Cpno) REFERENCES Course(Cno))')
cursor.execute('CREATE TABLE IF NOT EXISTS SC(Sno CHAR(9),Cno CHAR(9),Grade SMALLINT,PRIMARY KEY (Sno,Cno),FOREIGN KEY (Sno) REFERENCES Student(Sno),FOREIGN KEY(Cno) REFERENCES Course(Cno))')

cursor.close()
connect.close()
