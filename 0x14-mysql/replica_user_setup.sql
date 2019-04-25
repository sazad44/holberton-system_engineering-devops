-- Setup user with replication permissions
-- Create replica_user if it doesn't exist
CREATE USER IF NOT EXISTS 'replica_user'@'localhost' IDENTIFIED BY 'replica_user';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'localhost';
GRANT SELECT ON `mysql`.`user` TO 'holberton_user'@'localhost';
