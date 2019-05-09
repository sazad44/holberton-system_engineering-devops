-- Create databases and table with rows
-- Create Database tyrell_corp
DROP DATABASE IF EXISTS tyrell_corp;
CREATE DATABASE IF NOT EXISTS tyrell_corp;
-- Create table nexus6
USE tyrell_corp;
DROP TABLE IF EXISTS nexus6;
CREATE TABLE IF NOT EXISTS nexus6(
       id INT NOT NULL AUTO_INCREMENT,
       PRIMARY KEY(id),
       name VARCHAR(256) NOT NULL);
INSERT INTO nexus6(name) VALUES ('HOLBERTON');
GRANT SELECT ON `tyrell_corp`.* TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
