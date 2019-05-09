-- SQL script to set up user with password
-- Create holberton_user with password projectcorrection280hbtn
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
-- Grant replication client privileges to user
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
