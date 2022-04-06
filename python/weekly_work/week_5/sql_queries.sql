select 
	*
from 
	ninjas;

insert into ninjas (first_name,last_name,age) values ("timmy","shar",25);
insert into ninjas (first_name,last_name,age) values ("tony","shar",22);
insert into ninjas (first_name,last_name,age) values ("alex","shar",58);
insert into ninjas (first_name,last_name,age) values ("olga","olevsky",56);
insert into ninjas (first_name,last_name,age) values ("madie","romero",56);
insert into ninjas (first_name,last_name,age) values ("roger","gilespie",60);
insert into ninjas (first_name,last_name,age) values ("marina","jan",55);
insert into ninjas (first_name,last_name,age) values ("chuchu","shar",3);
insert into ninjas (first_name,last_name,age) values ("roca","romero",1);
insert into ninjas (first_name,last_name,age) values ("khing","panusiri",26);
insert into ninjas (first_name,last_name,age) values ("kha","panusiri",26);
insert into ninjas (first_name,last_name,age) values ("brandon","tsao",26);
insert into ninjas (first_name,last_name,age) values ("tommy","kebschull",26);
insert into ninjas (first_name,last_name,age) values ("abraham","ponce",25);


select 
	*
from 
	dojo;

delete from ninjas where id = 16;
delete from dojo where id = 15;
-- dojo_haus
insert into dojo (name,ninjas_id) values ("dojo_haus",1);
insert into dojo (name,ninjas_id) values ("dojo_haus",8);
insert into dojo (name,ninjas_id) values ("dojo_haus",9);
insert into dojo (name,ninjas_id) values ("dojo_haus",13);
insert into dojo (name,ninjas_id) values ("dojo_haus",3);
insert into dojo (name,ninjas_id) values ("dojo_haus",7);


-- dojo_babies
insert into dojo (name,ninjas_id) values ("dojo_babies",2);
insert into dojo (name,ninjas_id) values ("dojo_babies",4);
insert into dojo (name,ninjas_id) values ("dojo_babies",6);
insert into dojo (name,ninjas_id) values ("dojo_babies",14);
insert into dojo (name,ninjas_id) values ("dojo_babies",5);
insert into dojo (name,ninjas_id) values ("dojo_babies",10);
insert into dojo (name,ninjas_id) values ("dojo_babies",11);
insert into dojo (name,ninjas_id) values ("dojo_babies",12);

-- retrieve all ninjas from first dojo

select
	*
from 
	dojo
where name = 'dojo_haus';

-- retrieve all ninjas from the last dojo

select
	*
from 
	dojo
where name = 'dojo_babies';

-- Retrieve last ninjas dojo
select
	name
from 
	dojo
where ninjas_id = 14;




















