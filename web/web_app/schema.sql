-- schema.sql

drop database if exists webdb;
create database webdb;

use webdb;

grant select, insert, update, delete on awesome.* to 'www-data'@'localhost' identified by 'www-data';

create table users (
id int(4) not null default '1000',
email varchar(50) not null,
password int(50) not null,
admin int(1) not null default '0',
name varchar(50) not null,
image varchar(500) not null,
created_at float(24) not null,
unique key idx_email (email),
key idx_created_at (created_at),
primary key (id)
)engine=innodb default charset=utf8;

create table blogs (
id int(20) not null,
user_id int(50) not null,
user_name varchar(50) not null,
user_imge varchar(500) not null,
name varchar(50) not null,
summary varchar(50) not null,
content varchar(200) not null,
created_at float(24) not null,
key idx_created_at (created_at),
primary key (id)
)engine=innodb default charset=utf8;

create table comments (
id int(20) not null,
blog_id int(50) not null,
user_id int(50) not null,
user_name varchar(50) not null,
user_imge varchar(500) not null,
content mediumtext not null,
created_at float(24) not null,
key idx_created_at (created_at),
primary key (id)
)engine=innodb default charset=utf8

