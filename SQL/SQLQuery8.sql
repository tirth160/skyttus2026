CREATE DATABASE sales_db;
USE sales_db;


CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);


CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);


INSERT INTO customers VALUES
(1, 'Tirth', 'Delhi'),
(2, 'Jiya', 'Mumbai'),
(3, 'Riyu', 'Bangalore'),
(4, 'Piyu', 'Delhi'),
(5, 'Kenil', 'Chennai');

INSERT INTO orders VALUES
(1001, 1, '2024-01-10', 70000),
(1002, 2, '2024-01-15', 20000),
(1003, 1, '2024-02-05', 30000),
(1004, 3, '2024-02-20', 5000),
(1005, 4, '2024-03-01', 25000),
(1006, 5, '2024-03-05', 15000),
(1007, 2, '2024-03-10', 35000);

--Add index to improve search on orders.customer_id
CREATE INDEX idx_orders_customer
ON orders(customer_id);


--Use EXPLAIN to analyze query
 
SELECT o.order_id, c.name, o.amount
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
WHERE o.customer_id = 2;


--Optimize a slow join query
SELECT o.order_id, c.name
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
WHERE o.customer_id = 2;


CREATE INDEX idx_orders_covering
ON orders(customer_id, order_id, amount);

--Bonus: Check index usage
-- SQL Server
SET STATISTICS IO ON;
SELECT * FROM orders WHERE customer_id = 2;

-- MySQL
 SELECT * FROM orders WHERE customer_id = 2;
