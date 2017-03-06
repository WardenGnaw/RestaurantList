DROP DATABASE IF EXISTS RestaurantListTest;
CREATE DATABASE RestaurantListTest;
CREATE USER IF NOT EXISTS 'test'@'localhost' IDENTIFIED BY 'test';
GRANT ALL PRIVILEGES ON RestaurantListTest.* TO 'test'@'localhost';
CREATE TABLE RestaurantListTest.Restaurant(id INT AUTO_INCREMENT, Name VARCHAR(100), Address VARCHAR(100), PRIMARY KEY(id));
