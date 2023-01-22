drop table if exists users;
create table users(
    user_id integer primary key autoincrement, 
    name string not null, 
    email string, 
    phone_number string, 
    date_joined datetime);

drop table if exists friend;
create table friend(
    friendship_id int not null,
    user_id int not null,
    friend_id int not null, 
    foreign key (user_id) references users(user_id), 
    foreign key (friend_id) references users(user_id),
    primary key (friendship_id));

drop table if exists preferences;
create table preferences(
    pref_id int not null, 
    genre string, 
    user_id int not null,
    foreign key (user_id) references users(user_id),
    primary key (pref_id));

drop table if exists recommendations;
create table recommendations(
    rec_id int not null, 
    user_id int not null, 
    entertainment_id int not null, 
    successful bool,
    foreign key (user_id) references users(user_id),
    foreign key (entertainment_id) references entertainment(entertainment_id),
    primary key (rec_id));

drop table if exists entertainment;
create table entertainment(
    entertainment_id int not null, 
    name string not null, 
    genre string, 
    length int,
    description string,
    primary key (entertainment_id));

drop table if exists user_watched_entertainment;
create table user_watched_entertainment(
    watch_id int not null, 
    user_id int not null,
    entertainment_id int not null,
    foreign key (user_id) references users(user_id), 
    foreign key (entertainment_id) references entertainment(entertainment_id),
    primary key (watch_id));

drop table if exists user_favorites_entertainment;
create table user_favorites_entertainment(
    favorite_id int not null,
    user_id int not null,
    entertainment_id int not null,
    foreign key (user_id) references users(user_id), 
    foreign key (entertainment_id) references entertainment(entertainment_id),
    primary key (favorite_id));

drop table if exists user_wants_to_watch_entertainment;
create table user_wants_to_watch_entertainment(
    want_id int not null,
    user_id int not null,
    entertainment_id int not null,
    foreign key (user_id) references users(user_id), 
    foreign key (entertainment_id) references entertainment(entertainment_id),
    primary key (want_id));

drop table if exists user_reviewed_entertainment;
create table user_reviewed_entertainment(
    review_id integer primary key autoincrement, 
    rating int, 
    review_text string, 
    user_id int not null,
    entertainment_id int not null,
    date_reviewed datetime,
    foreign key (user_id) references users(user_id), 
    foreign key (entertainment_id) references entertainment(entertainment_id));

drop table if exists crew;
create table crew(
    crew_id int not null, 
    name string not null,
    primary key (crew_id));

drop table if exists crew_featured_in_entertainment;
create table crew_featured_in_entertainment(
    feature_id int not null, 
    crew_id int not null,
    entertainment_id int not null, 
    foreign key (crew_id) references crew(crew_id), 
    foreign key (entertainment_id) references entertainment(entertainment_id),
    primary key (feature_id));

drop table if exists website;
create table website(
    site_id int not null, 
    name string not null, 
    url string,
    primary key (site_id));

drop table if exists entertainment_can_be_found_on_site;
create table entertainment_can_be_found_on_site(
    found_id int not null, 
    site_id int not null,
    entertainment_id int not null,
    foreign key (site_id) references website(site_id), 
    foreign key (entertainment_id) references entertainment(entertainment_id),
    primary key (found_id));
