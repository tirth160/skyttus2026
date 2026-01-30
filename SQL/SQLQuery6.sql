CREATE DATABASE bank_db;
USE bank_db;


CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    account_holder VARCHAR(50),
    balance INT
);


INSERT INTO accounts VALUES
(1, 'Tirth', 10000),
(2, 'Tiya', 8000),
(3, 'Meet', 12000);


--Start a Transaction & Insert Record
BEGIN TRANSACTION;

INSERT INTO accounts VALUES
(4, 'Priya', 5000);


--Rollback Changes
ROLLBACK;


--Commit a Valid Transaction

BEGIN TRANSACTION;

INSERT INTO accounts VALUES
(4, 'Priya', 5000);

COMMIT;

--Demonstrate Money Transfer Using Transaction
BEGIN TRANSACTION;

-- Deduct from Amit
UPDATE accounts
SET balance = balance - 2000
WHERE account_id = 1;

-- Add to Neha
UPDATE accounts
SET balance = balance + 2000
WHERE account_id = 2;

COMMIT;


--Transaction with Rollback (If Error Occurs)
BEGIN TRANSACTION;

-- Deduct from Ravi
UPDATE accounts
SET balance = balance - 15000
WHERE account_id = 3;

-- Check condition manually (insufficient balance)
ROLLBACK;

--Check Final Account Balances
SELECT * FROM accounts;
