show databases;

use mohitdb;

show tables;

create table registration (
first_name varchar(25),
last_name varchar(25),
email_id varchar(25),
mobile_no varchar(25),
username varchar(25),
password varchar(25)
);



select * from registration;

SET SQL_SAFE_UPDATES = 0;

delete from registration
where first_name = 'a';

drop table registration;