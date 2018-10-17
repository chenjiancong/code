drop table if exists entries;
create table entries(
    id int(10) not null primary key auto_increment,
    title varchar(255) not null,
    text varchar(255) not null
);
