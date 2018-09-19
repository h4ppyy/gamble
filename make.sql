create table gamble_user(
	id int primary key auto_increment,
    username varchar(100) not null,
    password varchar(100) not null,
    money int not null default 0,
    regist_date datetime default now(),
    modify_date datetime default null
);

create table gamble_result(
	id int primary key auto_increment,
    gb_date varchar(100),
    gb_round varchar(100),
    gb_leftright varchar(100),
    gb_threefour varchar(100),
    gb_evenodd varchar(100),
    regist_date datetime default now(),
    modify_date datetime default null
);

create table gamble_bat(
	id int primary key auto_increment,
    user_id int,
    gb_date varchar(100),
    gb_round varchar(100),
    gb_leftright varchar(100),
    gb_threefour varchar(100),
    gb_evenodd varchar(100),
    bat_money int,
    success varchar(100) default 'N',
    regist_date datetime default now(),
    modify_date datetime default null
);

delimiter |
CREATE TRIGGER gamble_trigger after INSERT ON gamble_result
FOR EACH ROW BEGIN
update gamble_bat c
set c.success = 'Y'
where id in (
	select id
    from (
		select id
		from gamble_bat a
		join
		(
			select gb_date, gb_round, gb_leftright, gb_threefour, gb_evenodd
			from gamble_result
			order by regist_date desc
			limit 1
		) b
		on a.gb_date = b.gb_date
		and a.gb_round = b.gb_round
		and a.gb_leftright = b.gb_leftright
		and a.gb_threefour = b.gb_threefour
		and a.gb_evenodd = b.gb_evenodd
		where a.success = 'N'
    ) tmp
);
update gamble_user as x
join (
	select user_id, bat_money*2 as add_money
	from gamble_bat a
	join
	(
		select gb_date, gb_round, gb_leftright, gb_threefour, gb_evenodd
		from gamble_result
		order by regist_date desc
		limit 1
	) b
	on a.gb_date = b.gb_date
	and a.gb_round = b.gb_round
	and a.gb_leftright = b.gb_leftright
	and a.gb_threefour = b.gb_threefour
	and a.gb_evenodd = b.gb_evenodd
	where a.success = 'Y'
) as y
on x.id = y.user_id
set x.money = x.money + y.add_money;
END;
