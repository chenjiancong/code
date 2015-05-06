-- schema.sql

drop database if exists webdb;

create database webdb;

use webdb;

create table users(
id int(10) not null auto_increment,
name char(20) not null,
sex int(4) not null default '0',
age int(5) not null default '18',
primary key(id)
);

create table orders(
order_id int(20) not null auto_increment,
user_id int(10) not null,
create_time timestamp default current_timestamp,
update_time timestamp default current_timestamp on update current_timestamp,
primary key(order_id),
foreign key(user_id) references users(id)
);
