CREATE DATABASE ecommerce;
USE ecommerce;

-- Customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50)
);

-- Orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);

-- Order Items table
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);



INSERT INTO customers VALUES
(1, 'Tirth', 'Delhi'),
(2, 'Piyu', 'Mumbai'),
(3, 'Rohit', 'Bangalore'),
(4, 'Jeet', 'Pune'),
(5, 'Keyur', 'Ahmedabad');



INSERT INTO products VALUES
(1, 'Laptop', 60000),
(2, 'Mobile Phone', 25000),
(3, 'Headphones', 3000),
(4, 'Keyboard', 1500),
(5, 'Monitor', 12000);



INSERT INTO orders VALUES
(101, 1, '2025-01-10', 85000),
(102, 2, '2025-01-15', 25000),
(103, 1, '2025-02-05', 3000),
(104, 3, '2025-02-12', 72000),
(105, 3, '2025-03-01', 1500),
(106, 4, '2025-03-10', 12000);


INSERT INTO order_items VALUES
(101, 1, 1),
(101, 3, 1),
(102, 2, 1),
(103, 3, 1),
(104, 1, 1),
(104, 2, 1),
(105, 4, 1),
(106, 5, 1);

--Total orders per customer
SELECT c.name, COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name;


--Customers who never placed an order
SELECT c.name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;


--Highest selling product (by quantity)
SELECT p.product_name, SUM(oi.quantity) AS total_sold
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC

--Monthly sales report
SELECT 
FORMAT(order_date, 'yyyy-MM') AS month,
 SUM(amount) AS total_sales
FROM orders
GROUP BY FORMAT(order_date, 'yyyy-MM')
ORDER BY month;

--Customers with total purchase > ₹50,000
SELECT c.name, SUM(o.amount) AS total_purchase
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name
HAVING SUM(o.amount) > 50000;


--Top 3 cities by revenue
SELECT c.city, SUM(o.amount) AS revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY revenue DESC

