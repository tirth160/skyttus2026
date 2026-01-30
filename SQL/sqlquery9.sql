CREATE DATABASE company_db;
USE company_db;
 

 CREATE TABLE worker (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary INT,
    hire_date DATE
);
  

  CREATE TABLE worker_backup (
    emp_id INT,
    emp_name VARCHAR(50),
    salary INT
);


INSERT INTO worker VALUES
(1, 'Tirth', 50000, '2025-05-10'),
(2, 'Niva', 60000, '2025-07-01'),
(3, 'Rachana', 55000, '2024-12-20'),
(4, 'Tiya', 70000, '2025-09-01'),
(5, 'Kajal', 60000, '2025-06-15'),
(6, 'Neva', 60000, '2025-07-01'), 
(7, 'Ayu', 50000, '2025-05-10'); 
 

 INSERT INTO worker_backup VALUES
(2, 'Nera', 60000),
(3, 'Riyu', 55000),
(8, 'Sevu', 45000);

--Find Nth Highest Salary
SELECT emp_name, salary
FROM (
    SELECT emp_name, salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
) t
WHERE rnk = 3;


--Remove Duplicate Records
WITH cte AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY emp_name, salary, hire_date
               ORDER BY emp_id
           ) AS rn
    FROM worker
)
DELETE FROM cte
WHERE rn > 1;


--Find Records Common in Two Tables

SELECT e.*
FROM worker e
INNER JOIN worker_backup b
ON e.emp_id = b.emp_id;


--Find Employees Hired in Last 6 Months

SELECT *
FROM worker
WHERE hire_date >= DATEADD(MONTH, -6, GETDATE());
  -- WHERE hire_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH);


 -- Find Continuous Duplicate Values

 SELECT emp_id, emp_name, salary
FROM (
    SELECT *,
           LAG(salary) OVER (ORDER BY emp_id) AS prev_salary
    FROM employees
) t
WHERE salary = prev_salary;

