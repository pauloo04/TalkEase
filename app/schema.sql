DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS messages;


CREATE TABLE user (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL
);

CREATE TABLE messages (
  message_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  user_message STRING NOT NULL,
  system_response STRING NOT NULL  
);