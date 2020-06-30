-- Script to simply create the needed table 

CREATE TABLE cake_users(
    userID TEXT PRIMARY KEY,
    pubID TEXT,
    time_added DATETIME DEFAULT CURRENT_TIMESTAMP,
    wished INT DEFAULT 0
);

-- Simple fake data used to test the Bot
INSERT INTO cake_users(userID,pubID) VALUES('abcdef','abcdef')
INSERT INTO cake_users(userID,pubID) VALUES('u8027js','t2_jki9')
INSERT INTO cake_users(userID,pubID) VALUES('u8028js','t3_jki9')
INSERT INTO cake_users(userID,pubID) VALUES('u4028js','t3_jli9')