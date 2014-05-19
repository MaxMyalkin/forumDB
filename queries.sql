select count(*) from Threads;
select count(*) from Posts;
select count(*) from Subscriptions;
select * from Followers;
select * from Subscriptions;
insert into Followers (follower, followee) values ('example3@mail.ru', 'example4@mail.ru');
insert into Subscriptions (thread, user) values(1, 'email3');
select email from Users;
select about , email , Users.id , isAnonymous , name , username, group_concat(thread) 
from Users inner join Subscriptions on Users.email = Subscriptions.user where email = 'email2';
select * from Followers;

select short_name from Forums;


explain select follower from Followers where followee = 'example@mail.ru';


explain select about , email , Users.id , isAnonymous , name , username, group_concat(thread) from Users
              inner join Subscriptions on Users.email = Subscriptions.user where email = 'example@mail.ru';

explain select * from Posts p join Forums f on p.forum = f.short_name join Threads t on p.thread = t.id where p.id = 3;


explain select followee from Followers as f inner join Users as u on f.follower = u.email 
where follower = 'example@mail.ru' and u.id <10 order by u.name ;

select * , group_concat(thread)
from Followers f 
	join Users u on f.follower = u.email 
	join Subscriptions s on u.email = s.user where u.email = 'example2@mail.ru' and u.id < 10 order by u.name asc;

select * from Subscriptions; 


explain update Threads set isClosed = 0 where id = 100;

explain select distinct u_id
        from Posts
        where forum = 'forum1' and u_id >= 10 order by u_id asc;

explain select followee from Followers as f inner join Users as u on f.followee = u.id 
		where follower = 1 and followee > 0 order by u.name;

SELECT * FROM Followers JOIN Users ON Users.email = Followers.follower
where followee = "example3@mail.ru";
