-- Create Database
CREATE DATABASE IF NOT EXISTS ecommerce;

USE ecommerce;

-- Customer Table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) NOT NULL
);

-- Product Table
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL
);

-- Orders Table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_price DECIMAL(10,2),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Sample Products
INSERT INTO products(product_name, price, quantity)
VALUES
('Laptop', 65000.00, 5),
('Mouse', 500.00, 20),
('Keyboard', 1200.00, 15),
('Monitor', 12000.00, 8),
('Headphones', 2000.00, 10),
('USB Cable', 250.00, 30),
('Webcam', 3500.00, 12);

-- Check Data
SELECT * FROM customers;
SELECT * FROM products;
SELECT * FROM orders;
