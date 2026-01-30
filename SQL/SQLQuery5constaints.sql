CREATE DATABASE ecommerce_db;
USE ecommerce_db;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100) NOT NULL
);


CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    amount INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users VALUES
(1, 'Tirth', 'tirth@gmail.com', 'tirth123'),
(2, 'Jeet', 'jeet@gmail.com', 'jeet23'),
(3, 'Virat', 'virat@gmail.com', 'virat123');

INSERT INTO orders VALUES
(101, 1, '2024-01-10', 5000),
(102, 1, '2024-01-15', 3000),
(103, 2, '2024-02-01', 7000),
(104, 3, '2024-02-05', 2000);


CREATE INDEX idx_user_email
ON users(email);


CREATE VIEW user_order_summary AS
SELECT 
    u.user_id,
    u.name,
    u.email,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM users u
LEFT JOIN orders o
ON u.user_id = o.user_id
GROUP BY u.user_id, u.name, u.email;


--View the Result
SELECT * FROM user_order_summary;
