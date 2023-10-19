-- Check if the database exists
SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = 'hbtn_0d_2';
-- If the database doesn't exist, create it
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Check if the user exists
SELECT user FROM mysql.user WHERE user = 'user_0d_2';
-- If the user doesn't exist, create the user and grant SELECT privilege
CREATE USER IF NOT EXISTS 'user_0d_2'@'%' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant SELECT privilege to the user for the hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'%';
-- Apply the privileges
FLUSH PRIVILEGES;

