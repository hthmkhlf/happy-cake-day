CREATE TABLE cake_users(
    userID TEXT PRIMARY KEY,
    pubID TEXT,
    time_added DATETIME DEFAULT CURRENT_TIMESTAMP,
    wished INT DEFAULT 0
);

ALTER TABLE users
ADD COLUMN wished INT DEFAULT 0;


INSERT INTO cake_users(userID,pubID) VALUES('abcdef','abcdef')