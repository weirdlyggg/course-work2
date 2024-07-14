create table character (
	c_id integer primary key,
	c_name varchar,
	c_stars integer,
	c_damage_type varchar,
	way_id integer
);

create table way (
	way_id integer primary key,
	way_name varchar
);

create table weapon (
	w_id integer primary key,
	w_name varchar,
	w_stars integer,
	way_id integer
);

create table relic (
	r_id integer primary key,
	r_name varchar,
	r_2_parts_effects varchar,
	r_4_parts_effects varchar
);

create table planet_jewelry (
	pj_id integer primary key,
	pj_name varchar,
	pj_effect varchar
);

create table character_weapon (
	c_id integer references character(c_id),
	w_id integer references weapon(w_id)
);

create table character_relic (
	c_id integer references character(c_id),
	r_id integer references relic(r_id)
);

create table character_jewelry (
	c_id integer references character(c_id),
	pj_id integer references planet_jewelry(pj_id)
);

alter table character 
add foreign key (way_id) references 
way(way_id);

alter table weapon 
add foreign key (way_id) references 
way(way_id);

create table tg_users (
    tg_id integer,
    tg_username varchar,
    tg_rolename varchar
);

create table user_search_history (
    ush_id serial primary key,
    tg_id bigint not null,
    c_name varchar(255) not null,
    search_time timestamp default current_timestamp
);