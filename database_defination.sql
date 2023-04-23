DROP DATABASE IF EXISTS recipe_recommendation;

CREATE DATABASE recipe_recommendation;

USE recipe_recommendation;

CREATE TABLE users (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    confirmed BOOLEAN DEFAULT FALSE,
    password VARCHAR(60) NOT NULL,
    profile_picture VARCHAR(120)
);

CREATE TABLE recipes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    img_url TEXT,
    ingredients TEXT,
    directions TEXT,
    recipe_url VARCHAR(255)
);

CREATE TABLE ratings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    rate_number INT NOT NULL,
    user_id VARCHAR(60) NOT NULL,
    recipe_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (recipe_id) REFERENCES recipes (id)
);

CREATE TABLE reviews (
    id INT PRIMARY KEY AUTO_INCREMENT,
    content TEXT,
    user_id VARCHAR(60) NOT NULL,
    recipe_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (recipe_id) REFERENCES recipes (id)
);

CREATE TABLE link (
    users_id VARCHAR(65),
    recipes_id INT,
    PRIMARY KEY (users_id, recipes_id),
    FOREIGN KEY (users_id) REFERENCES users (id),
    FOREIGN KEY (recipes_id) REFERENCES recipes (id)
);

CREATE USER 'team'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON recipe_recommendation.* TO 'team'@'localhost';
FLUSH PRIVILEGES;
