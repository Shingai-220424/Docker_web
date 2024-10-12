CREATE DATABASE test_mysql;
USE test_mysql;
CREATE TABLE person (id INT NOT NULL PRIMARY KEY, name VARCHAR(100) NOT NULL, size DOUBLE);
CREATE TABLE human (id INT NOT NULL PRIMARY KEY, name VARCHAR(100) NOT NULL, height DOUBLE, weight DOUBLE);

INSERT INTO person (id, name, size) VALUES (1, 'A', 100), (2, 'B', 150), (3, 'C', 200);
INSERT INTO human (id, name, height, weight) VALUES (1, 'A', 160.0, 70.7), (2, 'B', 170.2, 63.8), (3, 'C', 188.5, 108.9);
