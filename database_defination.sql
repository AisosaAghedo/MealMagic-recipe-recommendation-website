DROP DATABASE IF EXISTS recipe_recommendation;

CREATE DATABASE recipe_recommendation;

USE recipe_recommendation;

CREATE TABLE users (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    confirmed BOOLEAN DEFAULT FALSE,
    password VARCHAR(60) NOT NULL,
    profile_picture VARCHAR(120),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE recipes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    img_url TEXT,
    ingredients TEXT,
    directions TEXT,
    recipe_url VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


-- CREATE USER 'team'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON recipe_recommendation.* TO 'team'@'localhost';
FLUSH PRIVILEGES;
