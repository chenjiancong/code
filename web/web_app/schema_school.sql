-- schema.sql

drop database if exists school;
create database school;
use school;

create table student(
stu_id int(4) not null auto_increment,
name varchar(20) not null,
cla_id int(4) not null,
primary key(stu_id)
);

create table classes(
cla_id int(4) not null,
name varchar(10) not null,
gra_id int(2),
primary key(cla_id)
);

create table grade(
gra_id int(2),
name varchar(10),
primary key(gra_id)
);

insert into student values('1001','Jack','102');
insert into student values('1002','Tom','102');
insert into student values('1003','Marry','103');

insert into classes values('102','Class_2','1');
insert into classes values('103','Class_3','2');

insert into grade values('1','grade_1');
insert into grade values('2','grade_2');
