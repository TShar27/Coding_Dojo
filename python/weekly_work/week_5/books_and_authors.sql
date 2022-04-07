-- authors
select * from authors;

insert into authors (name) values ("Henry Kissenger");
insert into authors (name) values ("Ernest Heminguay");
insert into authors (name) values ("Naval Ravikant");
insert into authors (name) values ("Alexander Pushkin");
insert into authors (name) values ("Nassim Taleb");

-- books
select * from books;

insert into books (title,num_of_pages) values ("C Sharp",250);
insert into books (title,num_of_pages) values ("Java",725);
insert into books (title,num_of_pages) values ("Python",520);
insert into books (title,num_of_pages) values ("PHP",83);
insert into books (title,num_of_pages) values ("Ruby",395);

-- change name of C Sharp to C#
update books set title = "C#" where id = 1;

-- change the first name of the 4th author to bill 
update authors set name = "Bill Pushkin" where id = 4;

-- favorites
select * from favorites;

insert into favorites (author_id,book_id) values (1,1);
insert into favorites (author_id,book_id) values (1,2);
insert into favorites (author_id,book_id) values (2,1);
insert into favorites (author_id,book_id) values (2,2);
insert into favorites (author_id,book_id) values (2,3);
insert into favorites (author_id,book_id) values (3,1);
insert into favorites (author_id,book_id) values (3,2);
insert into favorites (author_id,book_id) values (3,3);
insert into favorites (author_id,book_id) values (3,4);
insert into favorites (author_id,book_id) values (3,5);
insert into favorites (author_id,book_id) values (5,2);


-- retrieve all the authors that favorited the 3rd book 
select 
	a.name
from 
	favorites f
join authors a
	on a.id = f.author_id
where f.book_id = 3;

-- remove the first author of the 3rd book's favorite 
select 
	a.name
from 
	favorites f
join authors a
	on a.id = f.author_id
where f.book_id = 3
limit 2,1;

-- find all the books that the second author favorited

select 
	b.title
from 
	favorites f
join books b 
	on b.id =f.book_id
where f.author_id = 2;

-- find all the authors that favorited the 5th book

select
	a.name
from
	favorites f
join authors a 
	on f.author_id = a.id
where f.book_id = 5;

-- find all the authors that favorited the 2nd book
select
	a.name
from
	favorites f
join authors a 
	on f.author_id = a.id
where f.book_id = 2;

-- display all the book titles that the 2nd author favorited

select 
	b.title as book_title
from 
	favorites f
join books b 
	on b.id =f.book_id
where f.author_id = 2;
	
	




