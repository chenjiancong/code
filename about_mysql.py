#Filename: about_mysql.txt
#-*- coding:utf-8 -*-

/*------------关于数据库操作部分-------------*/

本地连接数据库
mysql -uroot -p

查看数据库
show databases;

查看表
show tables;

创建数据库
create database db_name;

创建数据表
create table tb_name;

修改数据库密码
mysql> set password for 'root'@'localhost'=password('newpass');

修改列
alter table tb_name modify 列名 新类型 新参数
alter table tb_name change 旧列名 新列名 新类型 新参数


删除数据库/表
drop database db_name;
drop table tb_name;

备份数据库
mysqldump -hhostname -uusername -ppassword db_name > backupfile.sql

导入数据库
mysql -hhostname -uusername -ppassword db_name < backupfile.sql

插入数据到表里
insert into table_na values(...);

<<<<<<< HEAD
更新数据
update table_na set values=xxx where id=xxx;
=======
删除表中数据
delete from tb_name where id=XXX;

更新表中数据
update tb_name set id=new_date where id=old_date;

>>>>>>> centos

/*-----------SQL ERROR-------------*/

ERROR 2002
stemctl start mysqld/mariadb

<<<<<<< HEAD
<<<<<<< HEAD:about_mysql.py
=======
<<<<<<< HEAD:about_mysql.txt
# schema.sql使用
mysql> source schema.sql
mysql -u yourusername -p yourpassword yourdatabase < schema.sql

python 提示" no module named MySQLdb "
pip install mysql-python
=======
>>>>>>> dev
#limit 指定行业查询
select * from table limit 7,100; //搜索7-100行记录
select * from table limit 7,-1;  //搜索7到最后一行
select * from table limit 7      //搜索前7行
select * from table limit 0,7    //搜索前7行

#like 模糊查询
select * from table_na where id like '%123%'

#统计集合
select count(id) from table_na;

#  Create table
create table Users(id int(10) not null primary key auto_increment,username char(50) not null, password char(50));
<<<<<<< HEAD
=======
# schema.sql使用
mysql> source schema.sql
mysql -u yourusername -p yourpassword yourdatabase < schema.sql

python 提示" no module named MySQLdb "
pip install mysql-python
>>>>>>> aaacfe2011c8d54dfdeb09476ebc5556314cc3b3:about_mysql.txt
=======
>>>>>>> centos_work:about_mysql.py
>>>>>>> dev

