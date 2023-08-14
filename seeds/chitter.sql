DROP TABLE IF EXISTS peeps;
DROP SEQUENCE IF EXISTS peeps_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_handle VARCHAR(20),
    name_of_user TEXT,
    email TEXT,
    user_password VARCHAR(20)
);

CREATE SEQUENCE IF NOT EXISTS peeps_id_seq;
CREATE TABLE peeps (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    content VARCHAR(280),
    post_time TEXT,
    tags TEXT,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade
);

INSERT INTO users (user_handle, name_of_user, email, user_password) VALUES ('telon_tusk', 'Telon Tusk', 'telontusk999@server.com', 'NooneWillGuessMe');
INSERT INTO users (user_handle, name_of_user, email, user_password) VALUES ('no_vowel_bot', 'Vowel Hater', 'bot_account@server.com', 'SecretPassword');

INSERT INTO peeps (user_id, post_time, content) VALUES (1, '24/05/2023 17:20:34', 'Now you guys are just being rude.');
INSERT INTO peeps (user_id, post_time, content) VALUES (1, '23/05/2023 12:00:00', 'Just reset chitter...');
INSERT INTO peeps (user_id, post_time, content) VALUES (1, '23/05/2023 12:12:45', 'Wow, my peep is lonely, and so am I!');
INSERT INTO peeps (user_id, post_time, content) VALUES (2, '24/05/2023 17:21:34', 'Nw y gys r jst bng rd.')
