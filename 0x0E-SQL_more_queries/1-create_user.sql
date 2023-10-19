-- Check if the user exists
SELECT user FROM mysql.user WHERE user = 'user_0d_1';
-- If the user doesn't exist, create the user and grant all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';
-- Apply the privileges
FLUSH PRIVILEGES;
