CREATE TABLE user
(
user_id int not null, 
name text not null, 
email text not null, 
profile_pic text not null, 
teacher int not null, 
admin int not null, 
banned int not null
);
CREATE TABLE lost_and_found
(
        item_id INTEGER primary key AUTOINCREMENT,
        user_id int not null,
        item_name text not null,
        lost_or_found int not null,
        location text not null,
        description text,
        lf_time datetime not null,
        post_time datetime not null,
        image text,
        completed int not null,
        item_type text not null
);
CREATE TABLE activity
(
        act_id INTEGER primary key AUTOINCREMENT,
        user_id int not null,
        title text not null,
        image text,
        description text,
        post_time datetime not null,
        deadline datetime not null,
        activity_time datetime,
        location text,
        activity_type text,
        space_used int,
        space_limit int
);
CREATE TABLE resource (resource_id INTEGER primary key AUTOINCREMENT);
