CREATE TABLE users (
    uid INTEGER PRIMARY KEY NOT NULL,
    login CHAR(20) UNIQUE NOT NULL,
    haslo CHAR(50) NOT NULL,
    email CHAR(40) UNIQUE NOT NULL,
    datad INT NOT NULL
);
INSERT INTO users VALUES (NULL, 'admin', 'haslo', 'admin@home.net', time());
