#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: 数据查询

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host="localhost",user="root",passwd="cjcdb",db="webdb" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM users"

try:
# 执行SQL语句
    cursor.execute(sql)
# 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        sex = row[2]
        age = row[3]
    # 打印结果
        print "id=%s,name=%s,sex=%d,age=%s" % \
            (id, name, sex, age)
except:
    print "Error: unable to fecth data"

# 关闭数据库连接
db.close()
