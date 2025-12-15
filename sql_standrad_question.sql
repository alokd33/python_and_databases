https://console.neon.tech/app/org-morning-tree-78682112/projects

-- Summary of Defaults
-- Keyword	Full Form	Meaning
-- Default	ASC (Ascending)	Sorts from lowest value to highest value (A to Z, 1 to 10, oldest date to newest date).
-- DESC	DESC (Descending)	Sorts from highest value to lowest value (Z to A, 10 to 1, newest date to oldest date).
-- Example of Default Behavior
-- Alok Notes : Lead default order by ASC null last, leg default order by null first
-- The following two queries produce the exact same result:
-- sql
-- -- Explicitly states ASC, but this is the default
-- SELECT first_name FROM employees ORDER BY first_name ASC;

-- -- Default behavior (same as above)
-- SELECT first_name FROM employees ORDER BY first_name;

--SELECT
--    EXTRACT(YEAR FROM your_date_column) AS year_value,
--    EXTRACT(MONTH FROM your_date_column) AS month_value
--FROM
--    your_table;

--SELECT
--    DATE_PART('year', your_date_column) AS year_value,
--    DATE_PART('month', your_date_column) AS month_value
--FROM
--    your_table;

--SELECT
--    TO_CHAR(your_date_column, 'YYYY-MM') AS year_month_text,
--    TO_CHAR(your_date_column, 'Month YYYY') AS year_month_formatted
--FROM
--    your_table;
--
--SELECT
--    DATE_TRUNC('month', your_date_column)::date AS first_day_of_month
--FROM
--    your_table;

(base) Alok-ka-MacBook-Pro:~ alokdadarya$ brew services list
Name          Status  User        File
neo4j         stopped alokdadarya ~/Library/LaunchAgents/homebrew.mxcl.neo4j.plist
postgresql@14 started alokdadarya ~/Library/LaunchAgents/homebrew.mxcl.postgresql@14.plist


Method 1 – Easy Install using Homebrew (recommended)
If you already have Homebrew installed (you do):
brew install --cask dbeaver-community

After installation:
open /Applications/DBeaver.app

Step-1: Create a New Schema
Let’s name it ecom (you can choose any name like training, practice, learning).
CREATE SCHEMA ecom;

If you want schema owned by a specific user:
CREATE SCHEMA AUTHORIZATION alokdadarya;


Step-2: Set Default Schema for Your Session
So you don't need to prefix ecom.tableName each time:
SET search_path TO ecom;

(You will run this once per session or configure it permanently — instructions below.)
Now the database will automatically use tables inside schema ecom.

Step-3: Create Your Tables Under This Schema (no constraints first)
-- Use schema explicitly if search_path NOT set
CREATE TABLE ecom.customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    registration_date DATE,
    customer_type VARCHAR(50),
    country VARCHAR(50),
    total_purchases DECIMAL(10,2),
    last_purchase_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ecom.orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER,
    order_date TIMESTAMP,
    product_id INTEGER,
    product_name VARCHAR(100),
    quantity INTEGER,
    unit_price DECIMAL(10,2),
    total_amount DECIMAL(10,2),
    payment_method VARCHAR(50),
    order_status VARCHAR(50),
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


Step-4: Add Constraints & Indexes Modularly
-- Customers constraints
ALTER TABLE ecom.customers
ADD CONSTRAINT uq_customers_email UNIQUE (email);

ALTER TABLE ecom.customers
ADD CONSTRAINT chk_customers_total_purchases_nonneg CHECK (total_purchases >= 0);

ALTER TABLE ecom.customers
ADD CONSTRAINT chk_customers_last_purchase_after_reg
CHECK (last_purchase_date IS NULL OR last_purchase_date >= registration_date);

ALTER TABLE ecom.customers
ADD CONSTRAINT chk_customers_type_valid
CHECK (customer_type IN ('regular','premium','vip'));

-- Orders constraints
ALTER TABLE ecom.orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id)
REFERENCES ecom.customers(customer_id)
ON UPDATE CASCADE
ON DELETE RESTRICT;

ALTER TABLE ecom.orders
ADD CONSTRAINT uq_orders_natural UNIQUE (customer_id, order_date, product_id);

ALTER TABLE ecom.orders
ADD CONSTRAINT chk_orders_quantity_positive CHECK (quantity > 0);

ALTER TABLE ecom.orders
ADD CONSTRAINT chk_orders_unit_price_nonneg CHECK (unit_price >= 0);

ALTER TABLE ecom.orders
ADD CONSTRAINT chk_orders_total_amount_nonneg CHECK (total_amount >= 0);

ALTER TABLE ecom.orders
ADD CONSTRAINT chk_orders_total_amount_correct CHECK (total_amount = quantity * unit_price);

ALTER TABLE ecom.orders
ADD CONSTRAINT chk_orders_payment_method_valid
CHECK (payment_method IN ('credit_card','debit_card','paypal','cash'));

ALTER TABLE ecom.orders
ADD CONSTRAINT chk_orders_status_valid
CHECK (order_status IN ('pending','paid','shipped','delivered','cancelled'));

-- Index for faster join
CREATE INDEX idx_orders_customer_id ON ecom.orders(customer_id);


Step-5 (Optional): Make ecom default schema permanently
So you don’t need SET search_path every session.
ALTER DATABASE testdb SET search_path = ecom, public;

Reconnect → now your schema applies automatically.

Quick Verification
SELECT current_schema;

SELECT * FROM information_schema.tables WHERE table_schema = 'ecom';

\d ecom.customers;
\d ecom.orders;

Meaning of EXCLUDED
When you use:
INSERT ... ON CONFLICT (column) DO UPDATE

PostgreSQL keeps two versions of the row:
Reference
Meaning
customers.column
The existing row in the table (what’s already stored)
EXCLUDED.column
The new row you attempted to insert (what you sent in VALUES)

So EXCLUDED = "the row that was excluded from insertion due to conflict".

Visual Example
You run this:
INSERT INTO customers (email, total_purchases)
VALUES ('alice@example.com', 50.00)
ON CONFLICT(email)
DO UPDATE
SET total_purchases = customers.total_purchases + EXCLUDED.total_purchases;

Case 1 — email not found → normal insert
email
total_purchases
alice@example.com
50 (inserted)

Case 2 — email exists → conflict happens, so:
customers.total_purchases → current DB value


EXCLUDED.total_purchases → new incoming value


Example current data:
email
total_purchases
alice@example.com
250

New insert attempts:
VALUES ('alice@example.com', 50)

Conflict→Update:
customers.total_purchases = 250 (existing)
EXCLUDED.total_purchases = 50 (new)

Update result:
total_purchases = 250 + 50 = 300
email
total_purchases
alice@example.com
300


Breakdown of your UPSERT code
SET total_purchases = customers.total_purchases + EXCLUDED.total_purchases

Meaning:
📌 keep previous total AND add new purchase value.

SET last_purchase_date = GREATEST(customers.last_purchase_date, EXCLUDED.last_purchase_date)

keeps the most recent purchase date between old and new



SET notes = 'Updated via upsert';

updates notes with message



Simple wording to remember 💡
EXCLUDED.column = the values you tried to insert but were rejected due to conflict.
Useful when updating instead of inserting.

Think like this:
insert succeeds → row is inserted


insert conflicts → EXCLUDED holds the new row → use it to update existing row



If you want, I can give you a live example to run:
Practice Exercise
Insert Alice first time:


INSERT INTO ecom.customers (customer_name, email, registration_date,
    customer_type, country, total_purchases, last_purchase_date)
VALUES ('Alice Johnson','alice@example.com','2024-01-10','regular','USA',50,'2024-04-20');

Insert again to trigger UPSERT:


INSERT INTO ecom.customers (customer_name, email, registration_date,
    customer_type, country, total_purchases, last_purchase_date)
VALUES ('Alice Johnson','alice@example.com','2024-01-10','regular','USA',80,'2024-05-01')
ON CONFLICT(email)
DO UPDATE
SET total_purchases = customers.total_purchases + EXCLUDED.total_purchases,
    last_purchase_date = GREATEST(customers.last_purchase_date, EXCLUDED.last_purchase_date);

Check result:


SELECT * FROM ecom.customers WHERE email='alice@example.com';

You should see: total increased + latest date retained.

--select * from ecom.customers
--select * from ecom.orders
--select * from information_schema.tables
--SELECT current_database();
--
--+-------------------------------+
--|          customers            |
--+-------------------------------+
--| PK  customer_id               |
--| AK  email                     |
--|     customer_name             |
--|     email                     |
--|     registration_date         |
--|     customer_type             |
--|     country                   |
--|     total_purchases           |
--|     last_purchase_date        |
--|     notes (NULL allowed)      |
--|     created_at (timestamp)    |
--+-------------------------------+
--            1
--            |
--            |
--            *
--+-------------------------------+
--|            orders             |
--+-------------------------------+
--| PK  order_id                  |
--| FK  customer_id               |
--| AK  (customer_id, order_date, |
--|      product_id)              |
--|     order_date                |
--|     product_id                |
--|     product_name              |
--|     quantity                  |
--|     unit_price                |
--|     total_amount              |
--|     payment_method            |
--|     order_status              |
--|     remarks (NULL allowed)    |
--|     created_at (timestamp)    |
--+-------------------------------+
--CREATE SCHEMA ecom;
--Step-3: Create Your Tables Under This Schema (no constraints first)
INSERT INTO ecom.customers (
   customer_name, email, registration_date, customer_type,
   country, total_purchases, last_purchase_date, notes
) VALUES
('Alice Johnson',  'alice@example.com',  '2024-01-10', 'regular', 'USA', 250.00, '2024-03-15', 'Likes discounts'),
('Bob Smith',      'bob@example.com',    '2024-02-05', 'premium', 'USA', 1200.50, '2024-04-01', 'High-value customer'),
('Charlie Singh',  'charlie@example.com','2024-02-20', 'regular', 'Canada', 340.00, '2024-03-28', NULL),
('Diana Lopez',    'diana@example.com',  '2024-03-01', 'vip',     'Mexico', 3000.00, '2024-04-10', 'VIP customer'),
('Ethan Lee',      'ethan@example.com',  '2024-03-15', 'regular', 'USA', 0.00, NULL, 'New signup'),
('Fatima Khan',    'fatima@example.com', '2024-03-20', 'premium', 'UK', 850.75, '2024-04-05', NULL),
('George Brown',   'george@example.com', '2024-04-01', 'regular', 'USA', 50.00, '2024-04-02', 'Occasional buyer'),
('Hiro Tanaka',    'hiro@example.com',   '2024-04-05', 'vip',     'Japan', 5000.00, '2024-04-15', 'Top spender');
INSERT INTO ecom.orders (
   customer_id, order_date, product_id, product_name,
   quantity, unit_price, total_amount,
   payment_method, order_status, remarks
) VALUES
-- Alice (id 1)
(1, '2024-03-01 10:15:00', 101, 'Wireless Mouse', 1, 25.00, 25.00, 'credit_card', 'delivered', 'First order'),
(1, '2024-03-10 14:30:00', 102, 'Keyboard',       1, 45.00, 45.00, 'credit_card', 'delivered', NULL),
(1, '2024-03-15 09:00:00', 103, 'USB-C Cable',    2, 10.00, 20.00, 'paypal',      'shipped',   'Shipped quickly'),
-- Bob (id 2)
(2, '2024-03-20 11:00:00', 201, '27" Monitor',    1, 300.00, 300.00, 'credit_card', 'paid',      'Upgraded monitor'),
(2, '2024-03-25 16:45:00', 202, 'Laptop Stand',   1, 40.00, 40.00,   'debit_card',  'delivered', NULL),
(2, '2024-04-01 13:20:00', 203, 'Webcam',         1, 80.50, 80.50,   'credit_card', 'pending',   'Awaiting shipment'),
-- Charlie (id 3)
(3, '2024-03-18 08:30:00', 101, 'Wireless Mouse', 1, 25.00, 25.00, 'cash',        'delivered', NULL),
-- Diana (id 4)
(4, '2024-03-22 19:00:00', 301, 'Gaming Laptop',  1, 1500.00, 1500.00, 'credit_card', 'delivered', 'Big order'),
(4, '2024-03-30 10:10:00', 302, 'Headset',        1, 120.00, 120.00,   'credit_card', 'delivered', NULL),
-- Ethan (id 5)
(5, '2024-04-02 09:45:00', 103, 'USB-C Cable',    3, 10.00, 30.00, 'paypal',       'paid',      NULL),
-- Fatima (id 6)
(6, '2024-03-29 15:00:00', 401, 'Office Chair',   1, 220.75, 220.75, 'credit_card', 'shipped',  NULL),
-- George (id 7)
(7, '2024-04-02 20:00:00', 101, 'Wireless Mouse', 2, 25.00, 50.00, 'cash',        'pending',   'COD'),
-- Hiro (id 8)
(8, '2024-04-10 12:00:00', 501, '4K TV',          1, 2000.00, 2000.00, 'credit_card', 'delivered', 'Premium electronics'),
(8, '2024-04-15 18:30:00', 502, 'Soundbar',       1, 500.00,  500.00,  'credit_card', 'paid',      NULL);
--
--CRUD: INSERT, UPDATE, UPSERT
--INSERT (you’ve already done above)
--
--Example: add a new customer:
INSERT INTO ecom.customers (
   customer_name, email, registration_date, customer_type,
   country, total_purchases, last_purchase_date, notes
) VALUES (
   'New User', 'newuser@example.com', CURRENT_DATE,
   'regular', 'USA', 0.00, NULL, 'Signup from referral'
);
--UPDATE
--
--Example: update total purchases and last purchase date for Alice:
UPDATE ecom.customers
SET total_purchases   = total_purchases + 100.00,
   last_purchase_date = CURRENT_DATE
WHERE email = 'alice@example.com';
INSERT INTO ecom.customers (
   customer_name, email, registration_date, customer_type,
   country, total_purchases, last_purchase_date, notes
) VALUES (
   'Alice Johnson', 'alice@example.com', '2024-01-10',
   'regular', 'USA', 50.00, '2024-04-20', 'Upsert demo'
)
ON CONFLICT (email)  -- natural key we defined as UNIQUE
DO UPDATE
SET total_purchases   = customers.total_purchases + EXCLUDED.total_purchases,
   last_purchase_date = GREATEST(customers.last_purchase_date, EXCLUDED.last_purchase_date),
   notes              = 'Updated via upsert';


Q1. Total amount spent by each customer
Question:
 Return each customer’s total amount spent across all orders.
SQL:
SELECT
    c.customer_id,
    c.customer_name,
    SUM(o.total_amount) AS total_spent
FROM ecom.customers c
JOIN ecom.orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY c.customer_id;

Expected output (8 rows):
customer_id | customer_name   | total_spent
----------- | --------------- | -----------
1           | Alice Johnson   |  90.00
2           | Bob Smith       | 420.50
3           | Charlie Singh   |  25.00
4           | Diana Lopez     | 1620.00
5           | Ethan Lee       |  30.00
6           | Fatima Khan     | 220.75
7           | George Brown    |  50.00
8           | Hiro Tanaka     | 2500.00


Q2. Top 3 customers by total spend (CTE + ORDER BY + LIMIT)
Question:
 Find the top 3 customers by total order amount.
SQL:
WITH customer_totals AS (
    SELECT
        c.customer_id,
        c.customer_name,
        SUM(o.total_amount) AS total_spent
    FROM ecom.customers c
    JOIN ecom.orders o ON o.customer_id = c.customer_id
    GROUP BY c.customer_id, c.customer_name
)
SELECT *
FROM customer_totals
ORDER BY total_spent DESC
LIMIT 3;

Expected output:
customer_id | customer_name | total_spent
----------- | ------------- | ----------
8           | Hiro Tanaka   | 2500.00
4           | Diana Lopez   | 1620.00
2           | Bob Smith     |  420.50


Q3. Number of orders by order_status (GROUP BY)
Question:
 Return the count of orders per order_status.
SQL:
SELECT
    order_status,
    COUNT(*) AS order_count
FROM ecom.orders
GROUP BY order_status
ORDER BY order_status;

Expected output:
order_status | order_count
------------ | -----------
delivered    | 7
paid         | 3
pending      | 2
shipped      | 2


Q4. Latest order date per customer (MAX)
Question:
 For each customer, return their most recent order_date.
SQL:
SELECT
    c.customer_id,
    c.customer_name,
    MAX(o.order_date) AS last_order_date
FROM ecom.customers c
JOIN ecom.orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY c.customer_id;

Expected output (8 rows):
customer_id | customer_name   | last_order_date
----------- | --------------- | -----------------------
1           | Alice Johnson   | 2024-03-15 09:00:00
2           | Bob Smith       | 2024-04-01 13:20:00
3           | Charlie Singh   | 2024-03-18 08:30:00
4           | Diana Lopez     | 2024-03-30 10:10:00
5           | Ethan Lee       | 2024-04-02 09:45:00
6           | Fatima Khan     | 2024-03-29 15:00:00
7           | George Brown    | 2024-04-02 20:00:00
8           | Hiro Tanaka     | 2024-04-15 18:30:00


Q5. Customers with at least one pending order (JOIN + filter)
Question:
 Find customers who have at least one order with order_status = 'pending'.
SQL:
SELECT DISTINCT
    c.customer_id,
    c.customer_name
FROM ecom.customers c
JOIN ecom.orders o ON o.customer_id = c.customer_id
WHERE o.order_status = 'pending'
ORDER BY c.customer_id;

Expected output:
customer_id | customer_name
----------- | -------------
2           | Bob Smith
7           | George Brown


Q6. Segment customers by spend using CASE

Here’s the standard SQL CASE syntax (no examples, just patterns).

1️⃣ Simple CASE (compare one expression to values)
CASE <expression>
    WHEN <value_1> THEN <result_1>
    WHEN <value_2> THEN <result_2>
    ...
    [ELSE <default_result>]
END


2️⃣ Searched CASE (use full boolean conditions)
CASE
    WHEN <condition_1> THEN <result_1>
    WHEN <condition_2> THEN <result_2>
    ...
    [ELSE <default_result>]
END


3️⃣ General placement in a query
SELECT
    ...,
    CASE
        WHEN <condition> THEN <result>
        ...
        [ELSE <default_result>]
    END AS <alias>
FROM <table_name>

That’s the core standard syntax for CASE in SQL.

Question:
 Classify each customer as 'low', 'medium', or 'high' spender based on total order amount:
< 100 → low


100–1000 → medium


> 1000 → high


SQL:
SELECT
    c.customer_id,
    c.customer_name,
    SUM(o.total_amount) AS total_spent,
    CASE
        WHEN SUM(o.total_amount) < 100 THEN 'low'
        WHEN SUM(o.total_amount) BETWEEN 100 AND 1000 THEN 'medium'
        ELSE 'high'
    END AS spend_segment
FROM ecom.customers c
JOIN ecom.orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY c.customer_id;

Expected output:
customer_id | customer_name   | total_spent | spend_segment
----------- | --------------- | ----------- | -------------
1           | Alice Johnson   |  90.00      | low
2           | Bob Smith       | 420.50      | medium
3           | Charlie Singh   |  25.00      | low
4           | Diana Lopez     | 1620.00     | high
5           | Ethan Lee       |  30.00      | low
6           | Fatima Khan     | 220.75      | medium
7           | George Brown    |  50.00      | low
8           | Hiro Tanaka     | 2500.00     | high


Q7. Most recent order per customer (ROW_NUMBER window)
Question:
 Return each customer’s most recent order row, using a window function.
SQL (PostgreSQL):
WITH ranked AS (
    SELECT
        o.*,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY o.order_date DESC
        ) AS rn
    FROM ecom.orders o
)
SELECT
    customer_id,
    order_id,
    order_date,
    total_amount
FROM ranked
WHERE rn = 1
ORDER BY customer_id;

Expected output:
customer_id | order_id | order_date           | total_amount
----------- | -------- | -------------------- | -----------
1           | 3        | 2024-03-15 09:00:00  |  20.00
2           | 6        | 2024-04-01 13:20:00  |  80.50
3           | 7        | 2024-03-18 08:30:00  |  25.00
4           | 9        | 2024-03-30 10:10:00  | 120.00
5           | 10       | 2024-04-02 09:45:00  |  30.00
6           | 11       | 2024-03-29 15:00:00  | 220.75
7           | 12       | 2024-04-02 20:00:00  |  50.00
8           | 14       | 2024-04-15 18:30:00  | 500.00


Q8. Running total spend per customer (window SUM)
Question:
 For each customer, show their orders in time order and a running (cumulative) total of total_amount.
SQL:
SELECT
    customer_id,
    order_id,
    order_date,
    total_amount,
    SUM(total_amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM ecom.orders
ORDER BY customer_id, order_date;

Expected output (abridged):
customer_id | order_id | order_date           | total_amount | running_total
----------- | -------- | -------------------- | ----------- | -------------
1           | 1        | 2024-03-01 10:15:00  |  25.00      |  25.00
1           | 2        | 2024-03-10 14:30:00  |  45.00      |  70.00
1           | 3        | 2024-03-15 09:00:00  |  20.00      |  90.00
2           | 4        | 2024-03-20 11:00:00  | 300.00      | 300.00
...         | ...      | ...                  |  ...        |  ...
8           | 13       | 2024-04-10 12:00:00  | 2000.00     | 2000.00
8           | 14       | 2024-04-15 18:30:00  | 500.00      | 2500.00


Q9. Top products by revenue
Question:
 For each product, compute total revenue and order count, ordered by revenue descending.
SQL:
SELECT
    product_id,
    product_name,
    SUM(total_amount) AS revenue,
    COUNT(*) AS order_count
FROM ecom.orders
GROUP BY product_id, product_name
ORDER BY revenue DESC, product_id;

Expected output:
product_id | product_name    | revenue | order_count
---------- | --------------- | ------- | -----------
501        | 4K TV           | 2000.00 | 1
301        | Gaming Laptop   | 1500.00 | 1
502        | Soundbar        |  500.00 | 1
201        | 27" Monitor     |  300.00 | 1
401        | Office Chair    |  220.75 | 1
302        | Headset         |  120.00 | 1
101        | Wireless Mouse  |  100.00 | 3
203        | Webcam          |   80.50 | 1
103        | USB-C Cable     |   50.00 | 2
102        | Keyboard        |   45.00 | 1
202        | Laptop Stand    |   40.00 | 1


Q10. Revenue and customer count by country
Question:
 For each country, show number of distinct customers and total revenue.
SQL:
SELECT
    c.country,
    COUNT(DISTINCT c.customer_id) AS customer_count,
    SUM(o.total_amount) AS total_revenue
FROM ecom.customers c
JOIN ecom.orders o ON o.customer_id = c.customer_id
GROUP BY c.country
ORDER BY total_revenue DESC;

Expected output:
country | customer_count | total_revenue
------- | -------------- | -------------
Japan   | 1              | 2500.00
Mexico  | 1              | 1620.00
USA     | 4              |  590.50
UK      | 1              |  220.75
Canada  | 1              |   25.00


Q11. Average order amount by payment method
Question:
 Compute order_count and average total_amount by payment_method.
SQL:
SELECT
    payment_method,
    COUNT(*) AS order_count,
    ROUND(AVG(total_amount), 2) AS avg_amount
FROM ecom.orders
GROUP BY payment_method
ORDER BY payment_method;

Expected output:
payment_method | order_count | avg_amount
-------------- | ----------- | ----------
cash           | 2           |  37.50
credit_card    | 9           | 532.36
debit_card     | 1           |  40.00
paypal         | 2           |  25.00


Q12. Customers who use only credit cards (EXISTS + NOT EXISTS)
Question:
 Return customers who have at least one order and all their orders use payment_method = 'credit_card'.
SQL:
SELECT
    c.customer_id,
    c.customer_name
FROM ecom.customers c
WHERE EXISTS (
    SELECT 1
    FROM ecom.orders o
    WHERE o.customer_id = c.customer_id
)
AND NOT EXISTS (
    SELECT 1
    FROM ecom.orders o
    WHERE o.customer_id = c.customer_id
      AND o.payment_method <> 'credit_card'
)
ORDER BY c.customer_id;

Expected output:
customer_id | customer_name
----------- | -------------
4           | Diana Lopez
6           | Fatima Khan
8           | Hiro Tanaka


Q13. Customers with more than 2 orders (CTE + HAVING-style)
Question:
 Find customers who have placed more than 2 orders.
SQL:
WITH order_counts AS (
    SELECT
        customer_id,
        COUNT(*) AS order_count
    FROM ecom.orders
    GROUP BY customer_id
)
SELECT
    oc.customer_id,
    c.customer_name,
    oc.order_count
FROM order_counts oc
JOIN ecom.customers c ON c.customer_id = oc.customer_id
WHERE oc.order_count > 2
ORDER BY oc.order_count DESC;

Expected output:
customer_id | customer_name   | order_count
----------- | --------------- | -----------
1           | Alice Johnson   | 3
2           | Bob Smith       | 3


Q14. Monthly revenue (March vs April 2024)
Question:
 Group revenue by calendar month.
SQL (PostgreSQL):
SELECT
    to_char(order_date, 'YYYY-MM') AS year_month,
    SUM(total_amount) AS total_revenue,
    COUNT(*) AS order_count
FROM ecom.orders
GROUP BY to_char(order_date, 'YYYY-MM')
ORDER BY year_month;

Expected output:
year_month | total_revenue | order_count
---------- | ------------- | -----------
2024-03    | 2295.75       | 9
2024-04    | 2660.50       | 5


Q15. Days between consecutive orders (LAG window)
Question:
 For each customer, show the number of days since their previous order.
SQL (PostgreSQL):
SELECT
    customer_id,
    order_id,
    order_date,
    LAG(order_date) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS prev_order_date,
    ROUND(
        EXTRACT(EPOCH FROM (
            order_date
            - LAG(order_date) OVER (
                PARTITION BY customer_id
                ORDER BY order_date
            )
        )) / 86400.0
    , 2) AS days_since_prev
FROM ecom.orders
ORDER BY customer_id, order_date;

Expected output (abridged):
customer_id | order_id | order_date           | prev_order_date       | days_since_prev
----------- | -------- | -------------------- | --------------------- | ---------------
1           | 1        | 2024-03-01 10:15:00  | NULL                  | NULL
1           | 2        | 2024-03-10 14:30:00  | 2024-03-01 10:15:00   |  9.18
1           | 3        | 2024-03-15 09:00:00  | 2024-03-10 14:30:00   |  4.77
2           | 4        | 2024-03-20 11:00:00  | NULL                  | NULL
...         | ...      | ...                  | ...                   | ...
8           | 14       | 2024-04-15 18:30:00  | 2024-04-10 12:00:00   |  5.27


Q16. Percentage of total revenue by customer
Question:
 Compute each customer’s total spend and their percentage of overall revenue.
SQL:
WITH customer_totals AS (
    SELECT
        customer_id,
        SUM(total_amount) AS total_spent
    FROM ecom.orders
    GROUP BY customer_id
),
grand_total AS (
    SELECT SUM(total_spent) AS grand_total
    FROM customer_totals
)
SELECT
    c.customer_id,
    cu.customer_name,
    c.total_spent,
    ROUND(100.0 * c.total_spent / g.grand_total, 2) AS pct_of_revenue
FROM customer_totals c
CROSS JOIN grand_total g
JOIN ecom.customers cu ON cu.customer_id = c.customer_id
ORDER BY pct_of_revenue DESC;


select customer_id, customer_name, total_spent, pct_of_revenue from 
(select 
o.customer_id, 
c.customer_name,
sum(o.total_amount) over(partition by o.customer_id)  as total_spent, 
round(((sum(o.total_amount) over(partition by o.customer_id))/(sum(o.total_amount) over()))*100,2) as pct_of_revenue,
row_number() over(partition by o.customer_id) as row_number_customer
from ecom.orders o
inner join ecom.customers c on c.customer_id = o.customer_id 
) t1
where row_number_customer = 1
order by pct_of_revenue desc


Expected output (rounded):
customer_id | customer_name   | total_spent | pct_of_revenue
----------- | --------------- | ----------- | --------------
8           | Hiro Tanaka     | 2500.00     | 50.44
4           | Diana Lopez     | 1620.00     | 32.69
2           | Bob Smith       |  420.50     |  8.48
6           | Fatima Khan     |  220.75     |  4.45
1           | Alice Johnson   |   90.00     |  1.82
7           | George Brown    |   50.00     |  1.01
5           | Ethan Lee       |   30.00     |  0.61
3           | Charlie Singh   |   25.00     |  0.50


Q17. First and last order date per customer
Question:
 Return each customer’s first_order_date, last_order_date, and number of orders.
SQL:
SELECT
    c.customer_id,
    c.customer_name,
    MIN(o.order_date) AS first_order_date,
    MAX(o.order_date) AS last_order_date,
    COUNT(*) AS order_count
FROM ecom.customers c
JOIN ecom.orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY c.customer_id;

select 
customer_id,
customer_name,
first_order_date,
last_order_date, 
order_count
from 
(select 
o.customer_id, 
c.customer_name,
o.order_id,
o.order_date,
min(order_date) over(partition by o.customer_id ) as first_order_date,
max(order_date) over(partition by o.customer_id ) as last_order_date,
count(order_id) over(partition by o.customer_id) as order_count,
row_number() over(partition by o.customer_id) as row_num_by_cust
from ecom.orders o 
inner join ecom.customers c on o.customer_id = c.customer_id 
) t1
where row_num_by_cust = 1

Expected output:
customer_id | customer_name   | first_order_date       | last_order_date        | order_count
----------- | --------------- | ---------------------- | ---------------------- | -----------
1           | Alice Johnson   | 2024-03-01 10:15:00    | 2024-03-15 09:00:00    | 3
2           | Bob Smith       | 2024-03-20 11:00:00    | 2024-04-01 13:20:00    | 3
3           | Charlie Singh   | 2024-03-18 08:30:00    | 2024-03-18 08:30:00    | 1
4           | Diana Lopez     | 2024-03-22 19:00:00    | 2024-03-30 10:10:00    | 2
5           | Ethan Lee       | 2024-04-02 09:45:00    | 2024-04-02 09:45:00    | 1
6           | Fatima Khan     | 2024-03-29 15:00:00    | 2024-03-29 15:00:00    | 1
7           | George Brown    | 2024-04-02 20:00:00    | 2024-04-02 20:00:00    | 1
8           | Hiro Tanaka     | 2024-04-10 12:00:00    | 2024-04-15 18:30:00    | 2


Q18. Customers with orders in both March and April 2024
Question:
 Return customers who ordered in March 2024 and again in April 2024.
SQL (PostgreSQL):
WITH months AS (
    SELECT DISTINCT
        customer_id,
        CASE
            WHEN to_char(order_date, 'YYYY-MM') = '2024-03' THEN 'march'
            WHEN to_char(order_date, 'YYYY-MM') = '2024-04' THEN 'april'
        END AS month_label
    FROM ecom.orders
    WHERE to_char(order_date, 'YYYY-MM') IN ('2024-03','2024-04')
)
SELECT
    c.customer_id,
    c.customer_name
FROM ecom.customers c
JOIN months m1 ON m1.customer_id = c.customer_id AND m1.month_label = 'march'
JOIN months m2 ON m2.customer_id = c.customer_id AND m2.month_label = 'april'
ORDER BY c.customer_id;


SELECT
  c.customer_id,
  c.customer_name
FROM ecom.customers c
JOIN ecom.orders o
  ON o.customer_id = c.customer_id
WHERE o.order_date >= DATE '2024-03-01'
  AND o.order_date <  DATE '2024-05-01'
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(DISTINCT DATE_TRUNC('month', o.order_date)) = 2
ORDER BY c.customer_id;

Expected output:
customer_id | customer_name
----------- | -------------
2           | Bob Smith


Q19. Top-spend product per customer (ROW_NUMBER per customer)
Question:
 For each customer, find the single order where they spent the most (highest total_amount).
SQL:
WITH per_order AS (
    SELECT
        o.customer_id,
        o.product_id,
        o.product_name,
        o.total_amount,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY o.total_amount DESC
        ) AS rn
    FROM ecom.orders o
)
SELECT
    customer_id,
    product_id,
    product_name,
    total_amount AS top_spend_amount
FROM per_order
WHERE rn = 1
ORDER BY customer_id;

Expected output:
customer_id | product_id | product_name    | top_spend_amount
----------- | ---------- | --------------- | ----------------
1           | 102        | Keyboard        |  45.00
2           | 201        | 27" Monitor     | 300.00
3           | 101        | Wireless Mouse  |  25.00
4           | 301        | Gaming Laptop   | 1500.00
5           | 103        | USB-C Cable     |  30.00
6           | 401        | Office Chair    | 220.75
7           | 101        | Wireless Mouse  |  50.00
8           | 501        | 4K TV           | 2000.00


Q20. Customers whose total_purchases doesn’t match order sums
Question:
 Compare customers.total_purchases vs actual sum of orders.total_amount.
 Return customers where they don’t match (common data quality / reconciliation question).
SQL:
WITH order_sums AS (
    SELECT
        customer_id,
        SUM(total_amount) AS total_spent
    FROM ecom.orders
    GROUP BY customer_id
)
SELECT
    c.customer_id,
    c.customer_name,
    c.total_purchases,
    os.total_spent
FROM ecom.customers c
JOIN order_sums os ON os.customer_id = c.customer_id
WHERE c.total_purchases <> os.total_spent
ORDER BY c.customer_id;

select 
customer_id,
customer_name,total_purchases,total_spent
from 
(select
o.customer_id,
c.customer_name,
c.total_purchases, 
sum(o.total_amount ) as total_spent
from 
ecom.orders o 
inner join ecom.customers c 
on o.customer_id = c.customer_id 
group by o.customer_id,
c.customer_name, c.total_purchases
order by o.customer_id
) t1 
where total_purchases !=total_spent

Expected output:
customer_id | customer_name   | total_purchases | total_spent
----------- | --------------- | --------------- | ----------
1           | Alice Johnson   |  250.00         |  90.00
2           | Bob Smith       | 1200.50         | 420.50
3           | Charlie Singh   |  340.00         |  25.00
4           | Diana Lopez     | 3000.00         | 1620.00
5           | Ethan Lee       |    0.00         |  30.00
6           | Fatima Khan     |  850.75         | 220.75
8           | Hiro Tanaka     | 5000.00         | 2500.00

(George Brown is the only one whose total_purchases matches the orders exactly.)

Q20. Customers whose total_purchases doesn’t match order sums
Question:
 Compare customers.total_purchases vs actual sum of orders.total_amount.
 Return customers where they don’t match (common data quality / reconciliation question).
SQL:
WITH order_sums AS (
    SELECT
        customer_id,
        SUM(total_amount) AS total_spent
    FROM ecom.orders
    GROUP BY customer_id
)
SELECT
    c.customer_id,
    c.customer_name,
    c.total_purchases,
    os.total_spent
FROM ecom.customers c
JOIN order_sums os ON os.customer_id = c.customer_id
WHERE c.total_purchases <> os.total_spent
ORDER BY c.customer_id;

Expected output:
customer_id | customer_name   | total_purchases | total_spent
----------- | --------------- | --------------- | ----------
1           | Alice Johnson   |  250.00         |  90.00
2           | Bob Smith       | 1200.50         | 420.50
3           | Charlie Singh   |  340.00         |  25.00
4           | Diana Lopez     | 3000.00         | 1620.00
5           | Ethan Lee       |    0.00         |  30.00
6           | Fatima Khan     |  850.75         | 220.75
8           | Hiro Tanaka     | 5000.00         | 2500.00

(George Brown is the only one whose total_purchases matches the orders exactly.)

If you want, next I can:
Turn this into a checklist/plan (Day 1–3 focus: basics, Day 4–7 windows/CTEs), or


Add 5 more harder “Block-style” questions (nested subqueries, tricky edge cases, performance hints).


You said:
Add 20 more questions based on analaytic function row, rank, dense rank, over partition by lead and leg and etc and case statement, sum and and cte leetcode style and asked on SirusXM or Block company or top 20 question in this most asked
ChatGPT said:
Thought for 9s
Nice, this is exactly the right way to grind SQL for FAANG/Block/SiriusXM-style interviews.
Below are 20 more questions focused on:
ROW_NUMBER, RANK, DENSE_RANK


LAG, LEAD, FIRST_VALUE, LAST_VALUE


SUM()/AVG() OVER (PARTITION BY …)


CASE, CTEs, and LeetCode-style patterns


All queries use your tables under schema ecom:
ecom.customers


ecom.orders


I’ll give question + solution. You can run them in DBeaver and inspect the actual results from your data.


Q21. Rank customers by total spend (RANK)
SQL:
WITH customer_totals AS (
    SELECT
        c.customer_id,
        c.customer_name,
        SUM(o.total_amount) AS total_spent
    FROM ecom.customers c
    JOIN ecom.orders o ON o.customer_id = c.customer_id
    GROUP BY c.customer_id, c.customer_name
)
SELECT
    customer_id,
    customer_name,
    total_spent,
    RANK() OVER (ORDER BY total_spent DESC) AS spend_rank
FROM customer_totals
ORDER BY spend_rank, customer_id;

Expected output:
customer_id | customer_name   | total_spent | spend_rank
----------- | --------------- | ----------- | ----------
8           | Hiro Tanaka     |   2500.00   |    1
4           | Diana Lopez     |   1620.00   |    2
2           | Bob Smith       |    420.50   |    3
6           | Fatima Khan     |    220.75   |    4
1           | Alice Johnson   |     90.00   |    5
7           | George Brown    |     50.00   |    6
5           | Ethan Lee       |     30.00   |    7
3           | Charlie Singh   |     25.00   |    8


Q22. Rank customers within each country (DENSE_RANK)
SQL:
WITH customer_totals AS (
    SELECT
        c.customer_id,
        c.customer_name,
        c.country,
        SUM(o.total_amount) AS total_spent
    FROM ecom.customers c
    JOIN ecom.orders o ON o.customer_id = c.customer_id
    GROUP BY c.customer_id, c.customer_name, c.country
)
SELECT
    country,
    customer_id,
    customer_name,
    total_spent,
    DENSE_RANK() OVER (
        PARTITION BY country
        ORDER BY total_spent DESC
    ) AS country_rank
FROM customer_totals
ORDER BY country, country_rank, customer_id;

Expected output:
country | customer_id | customer_name   | total_spent | country_rank
------- | ----------- | --------------- | ----------- | ------------
Canada  | 3           | Charlie Singh   |     25.00   |     1
Japan   | 8           | Hiro Tanaka     |   2500.00   |     1
Mexico  | 4           | Diana Lopez     |   1620.00   |     1
UK      | 6           | Fatima Khan     |    220.75   |     1
USA     | 2           | Bob Smith       |    420.50   |     1
USA     | 1           | Alice Johnson   |     90.00   |     2
USA     | 7           | George Brown    |     50.00   |     3
USA     | 5           | Ethan Lee       |     30.00   |     4


Q23. Top 2 orders per customer by amount (ROW_NUMBER)
SQL:
WITH ranked_orders AS (
    SELECT
        o.*,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY o.total_amount DESC
        ) AS rn
    FROM ecom.orders o
)
SELECT
    customer_id,
    order_id,
    order_date,
    total_amount
FROM ranked_orders
WHERE rn <= 2
ORDER BY customer_id, rn;

Expected output:
customer_id | order_id | order_date           | total_amount
----------- | -------- | -------------------- | -----------
1           | 2        | 2024-03-10 14:30:00  |    45.00
1           | 1        | 2024-03-01 10:15:00  |    25.00
2           | 4        | 2024-03-20 11:00:00  |   300.00
2           | 6        | 2024-04-01 13:20:00  |    80.50
3           | 7        | 2024-03-18 08:30:00  |    25.00
4           | 8        | 2024-03-22 19:00:00  |  1500.00
4           | 9        | 2024-03-30 10:10:00  |   120.00
5           | 10       | 2024-04-02 09:45:00  |    30.00
6           | 11       | 2024-03-29 15:00:00  |   220.75
7           | 12       | 2024-04-02 20:00:00  |    50.00
8           | 13       | 2024-04-10 12:00:00  |  2000.00
8           | 14       | 2024-04-15 18:30:00  |   500.00


Q24. Difference from previous order amount (LAG)
SQL:
SELECT
    customer_id,
    order_id,
    order_date,
    total_amount,
    LAG(total_amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS prev_amount,
    total_amount
      - COALESCE(
            LAG(total_amount) OVER (
                PARTITION BY customer_id
                ORDER BY order_date
            ),
            0
        ) AS diff_from_prev
FROM ecom.orders
ORDER BY customer_id, order_date;

Expected output:
customer_id | order_id | order_date           | total_amount | prev_amount | diff_from_prev
----------- | -------- | -------------------- | ------------ | ----------- | --------------
1           | 1        | 2024-03-01 10:15:00  |      25.00   |   NULL      |      25.00
1           | 2        | 2024-03-10 14:30:00  |      45.00   |   25.00     |      20.00
1           | 3        | 2024-03-15 09:00:00  |      20.00   |   45.00     |     -25.00
2           | 4        | 2024-03-20 11:00:00  |     300.00   |   NULL      |     300.00
2           | 5        | 2024-03-25 16:45:00  |      40.00   |  300.00     |    -260.00
2           | 6        | 2024-04-01 13:20:00  |      80.50   |   40.00     |      40.50
3           | 7        | 2024-03-18 08:30:00  |      25.00   |   NULL      |      25.00
4           | 8        | 2024-03-22 19:00:00  |    1500.00   |   NULL      |    1500.00
4           | 9        | 2024-03-30 10:10:00  |     120.00   | 1500.00     |   -1380.00
5           | 10       | 2024-04-02 09:45:00  |      30.00   |   NULL      |      30.00
6           | 11       | 2024-03-29 15:00:00  |     220.75   |   NULL      |     220.75
7           | 12       | 2024-04-02 20:00:00  |      50.00   |   NULL      |      50.00
8           | 13       | 2024-04-10 12:00:00  |    2000.00   |   NULL      |    2000.00
8           | 14       | 2024-04-15 18:30:00  |     500.00   | 2000.00     |   -1500.00


Q25. Days until next order (LEAD)
SQL:
SELECT
    customer_id,
    order_id,
    order_date,
    LEAD(order_date) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS next_order_date,
    ROUND(
        EXTRACT(EPOCH FROM (
            LEAD(order_date) OVER (
                PARTITION BY customer_id
                ORDER BY order_date
            ) - order_date
        )) / 86400.0,
        2
    ) AS days_to_next_order
FROM ecom.orders
ORDER BY customer_id, order_date;

Expected output:
customer_id | order_id | order_date           | next_order_date       | days_to_next_order
----------- | -------- | -------------------- | --------------------- | ------------------
1           | 1        | 2024-03-01 10:15:00  | 2024-03-10 14:30:00   |        9.18
1           | 2        | 2024-03-10 14:30:00  | 2024-03-15 09:00:00   |        4.77
1           | 3        | 2024-03-15 09:00:00  | NULL                  |        NULL
2           | 4        | 2024-03-20 11:00:00  | 2024-03-25 16:45:00   |        5.24
2           | 5        | 2024-03-25 16:45:00  | 2024-04-01 13:20:00   |        6.86
2           | 6        | 2024-04-01 13:20:00  | NULL                  |        NULL
3           | 7        | 2024-03-18 08:30:00  | NULL                  |        NULL
4           | 8        | 2024-03-22 19:00:00  | 2024-03-30 10:10:00   |        7.63
4           | 9        | 2024-03-30 10:10:00  | NULL                  |        NULL
5           | 10       | 2024-04-02 09:45:00  | NULL                  |        NULL
6           | 11       | 2024-03-29 15:00:00  | NULL                  |        NULL
7           | 12       | 2024-04-02 20:00:00  | NULL                  |        NULL
8           | 13       | 2024-04-10 12:00:00  | 2024-04-15 18:30:00   |        5.27
8           | 14       | 2024-04-15 18:30:00  | NULL                  |        NULL


Q26. First product ever ordered by each customer (FIRST_VALUE)
SQL:
SELECT
    customer_id,
    order_id,
    order_date,
    product_name,
    FIRST_VALUE(product_name) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS first_product_for_customer
FROM ecom.orders
ORDER BY customer_id, order_date;

Expected output:
customer_id | order_id | order_date           | product_name    | first_product_for_customer
----------- | -------- | -------------------- | --------------- | --------------------------
1           | 1        | 2024-03-01 10:15:00  | Wireless Mouse  | Wireless Mouse
1           | 2        | 2024-03-10 14:30:00  | Keyboard        | Wireless Mouse
1           | 3        | 2024-03-15 09:00:00  | USB-C Cable     | Wireless Mouse
2           | 4        | 2024-03-20 11:00:00  | 27" Monitor     | 27" Monitor
2           | 5        | 2024-03-25 16:45:00  | Laptop Stand    | 27" Monitor
2           | 6        | 2024-04-01 13:20:00  | Webcam          | 27" Monitor
3           | 7        | 2024-03-18 08:30:00  | Wireless Mouse  | Wireless Mouse
4           | 8        | 2024-03-22 19:00:00  | Gaming Laptop   | Gaming Laptop
4           | 9        | 2024-03-30 10:10:00  | Headset         | Gaming Laptop
5           | 10       | 2024-04-02 09:45:00  | USB-C Cable     | USB-C Cable
6           | 11       | 2024-03-29 15:00:00  | Office Chair    | Office Chair
7           | 12       | 2024-04-02 20:00:00  | Wireless Mouse  | Wireless Mouse
8           | 13       | 2024-04-10 12:00:00  | 4K TV           | 4K TV
8           | 14       | 2024-04-15 18:30:00  | Soundbar        | 4K TV


Q27. Flag each order as FIRST / LAST / NULL
SQL:
WITH order_bounds AS (
    SELECT
        o.*,
        FIRST_VALUE(order_id) OVER (
            PARTITION BY customer_id
            ORDER BY order_date
        ) AS first_order_id,
        LAST_VALUE(order_id) OVER (
            PARTITION BY customer_id
            ORDER BY order_date
            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
        ) AS last_order_id
    FROM ecom.orders o
)
SELECT
    customer_id,
    order_id,
    order_date,
    total_amount,
    CASE
        WHEN order_id = first_order_id THEN 'FIRST'
        WHEN order_id = last_order_id  THEN 'LAST'
        ELSE NULL
    END AS position_flag
FROM order_bounds
ORDER BY customer_id, order_date;

Expected output:
customer_id | order_id | order_date           | total_amount | position_flag
----------- | -------- | -------------------- | ------------ | -------------
1           | 1        | 2024-03-01 10:15:00  |     25.00    | FIRST
1           | 2        | 2024-03-10 14:30:00  |     45.00    | NULL
1           | 3        | 2024-03-15 09:00:00  |     20.00    | LAST
2           | 4        | 2024-03-20 11:00:00  |    300.00    | FIRST
2           | 5        | 2024-03-25 16:45:00  |     40.00    | NULL
2           | 6        | 2024-04-01 13:20:00  |     80.50    | LAST
3           | 7        | 2024-03-18 08:30:00  |     25.00    | FIRST
4           | 8        | 2024-03-22 19:00:00  |   1500.00    | FIRST
4           | 9        | 2024-03-30 10:10:00  |    120.00    | LAST
5           | 10       | 2024-04-02 09:45:00  |     30.00    | FIRST
6           | 11       | 2024-03-29 15:00:00  |    220.75    | FIRST
7           | 12       | 2024-04-02 20:00:00  |     50.00    | FIRST
8           | 13       | 2024-04-10 12:00:00  |   2000.00    | FIRST
8           | 14       | 2024-04-15 18:30:00  |    500.00    | LAST


Q28. Running total revenue per country
SQL:
SELECT
    c.country,
    o.customer_id,
    o.order_id,
    o.order_date,
    o.total_amount,
    SUM(o.total_amount) OVER (
        PARTITION BY c.country
        ORDER BY o.order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_country_revenue
FROM ecom.orders o
JOIN ecom.customers c ON c.customer_id = o.customer_id
ORDER BY c.country, o.order_date;

Expected output:
country | customer_id | order_id | order_date           | total_amount | running_country_revenue
------- | ----------- | -------- | -------------------- | ------------ | -----------------------
Canada  | 3           | 7        | 2024-03-18 08:30:00  |     25.00    |       25.00
Japan   | 8           | 13       | 2024-04-10 12:00:00  |   2000.00    |     2000.00
Japan   | 8           | 14       | 2024-04-15 18:30:00  |    500.00    |     2500.00
Mexico  | 4           | 8        | 2024-03-22 19:00:00  |   1500.00    |     1500.00
Mexico  | 4           | 9        | 2024-03-30 10:10:00  |    120.00    |     1620.00
UK      | 6           | 11       | 2024-03-29 15:00:00  |    220.75    |      220.75
USA     | 1           | 1        | 2024-03-01 10:15:00  |     25.00    |       25.00
USA     | 1           | 2        | 2024-03-10 14:30:00  |     45.00    |       70.00
USA     | 1           | 3        | 2024-03-15 09:00:00  |     20.00    |       90.00
USA     | 2           | 4        | 2024-03-20 11:00:00  |    300.00    |      390.00
USA     | 2           | 5        | 2024-03-25 16:45:00  |     40.00    |      430.00
USA     | 2           | 6        | 2024-04-01 13:20:00  |     80.50    |      510.50
USA     | 5           | 10       | 2024-04-02 09:45:00  |     30.00    |      540.50
USA     | 7           | 12       | 2024-04-02 20:00:00  |     50.00    |      590.50


Q29. Percentage of customer spend per order
SQL:
SELECT
    o.customer_id,
    o.order_id,
    o.total_amount,
    SUM(o.total_amount) OVER (
        PARTITION BY o.customer_id
    ) AS customer_total,
    ROUND(
        100.0 * o.total_amount
        / SUM(o.total_amount) OVER (PARTITION BY o.customer_id),
        2
    ) AS pct_of_customer_spend
FROM ecom.orders o
ORDER BY o.customer_id, o.order_id;

Expected output:
customer_id | order_id | total_amount | customer_total | pct_of_customer_spend
----------- | -------- | ------------ | -------------- | ---------------------
1           | 1        |     25.00    |     90.00      |        27.78
1           | 2        |     45.00    |     90.00      |        50.00
1           | 3        |     20.00    |     90.00      |        22.22
2           | 4        |    300.00    |    420.50      |        71.34
2           | 5        |     40.00    |    420.50      |         9.51
2           | 6        |     80.50    |    420.50      |        19.14
3           | 7        |     25.00    |     25.00      |       100.00
4           | 8        |   1500.00    |   1620.00      |        92.59
4           | 9        |    120.00    |   1620.00      |         7.41
5           | 10       |     30.00    |     30.00      |       100.00
6           | 11       |    220.75    |    220.75      |       100.00
7           | 12       |     50.00    |     50.00      |       100.00
8           | 13       |   2000.00    |   2500.00      |        80.00
8           | 14       |    500.00    |   2500.00      |        20.00


Q30. Customers whose max order > 50% of their total
SQL:
WITH stats AS (
    SELECT
        customer_id,
        SUM(total_amount) AS sum_per_customer,
        MAX(total_amount) AS max_per_customer
    FROM ecom.orders
    GROUP BY customer_id
)
SELECT customer_id
FROM stats
WHERE max_per_customer > 0.5 * sum_per_customer
ORDER BY customer_id;

Expected output:
customer_id
-----------
2
3
4
5
6
7
8

(Only customer 1 fails the condition because 45 is exactly 50% of 90, not > 50%.)

Q31. Two most recent orders per customer (ROW_NUMBER)
SQL:
WITH ranked AS (
    SELECT
        o.*,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY o.order_date DESC
        ) AS rn
    FROM ecom.orders o
)
SELECT
    customer_id,
    order_id,
    order_date,
    total_amount
FROM ranked
WHERE rn <= 2
ORDER BY customer_id, order_date DESC;

Expected output:
customer_id | order_id | order_date           | total_amount
----------- | -------- | -------------------- | -----------
1           | 3        | 2024-03-15 09:00:00  |    20.00
1           | 2        | 2024-03-10 14:30:00  |    45.00
2           | 6        | 2024-04-01 13:20:00  |    80.50
2           | 5        | 2024-03-25 16:45:00  |    40.00
3           | 7        | 2024-03-18 08:30:00  |    25.00
4           | 9        | 2024-03-30 10:10:00  |   120.00
4           | 8        | 2024-03-22 19:00:00  |  1500.00
5           | 10       | 2024-04-02 09:45:00  |    30.00
6           | 11       | 2024-03-29 15:00:00  |   220.75
7           | 12       | 2024-04-02 20:00:00  |    50.00
8           | 14       | 2024-04-15 18:30:00  |   500.00
8           | 13       | 2024-04-10 12:00:00  |  2000.00


Q32. Compare each order to customer’s average (CASE + AVG OVER)
SQL:
SELECT
    customer_id,
    order_id,
    total_amount,
    AVG(total_amount) OVER (
        PARTITION BY customer_id
    ) AS avg_for_customer,
    CASE
        WHEN total_amount >
            AVG(total_amount) OVER (PARTITION BY customer_id)
        THEN 'above_avg'
        ELSE 'below_or_equal'
    END AS size_vs_avg
FROM ecom.orders
ORDER BY customer_id, order_id;

Expected output:
customer_id | order_id | total_amount | avg_for_customer | size_vs_avg
----------- | -------- | ------------ | ---------------- | -----------
1           | 1        |     25.00    |    30.000000     | below_or_equal
1           | 2        |     45.00    |    30.000000     | above_avg
1           | 3        |     20.00    |    30.000000     | below_or_equal
2           | 4        |    300.00    |   140.166667     | above_avg
2           | 5        |     40.00    |   140.166667     | below_or_equal
2           | 6        |     80.50    |   140.166667     | below_or_equal
3           | 7        |     25.00    |    25.000000     | below_or_equal
4           | 8        |   1500.00    |   810.000000     | above_avg
4           | 9        |    120.00    |   810.000000     | below_or_equal
5           | 10       |     30.00    |    30.000000     | below_or_equal
6           | 11       |    220.75    |   220.750000     | below_or_equal
7           | 12       |     50.00    |    50.000000     | below_or_equal
8           | 13       |   2000.00    |  1250.000000     | above_avg
8           | 14       |    500.00    |  1250.000000     | below_or_equal


Q33. Same-status order count per customer
SQL:
SELECT
    customer_id,
    order_id,
    order_status,
    COUNT(*) OVER (
        PARTITION BY customer_id, order_status
    ) AS same_status_count_for_customer
FROM ecom.orders
ORDER BY customer_id, order_status, order_id;

Expected output:
customer_id | order_id | order_status | same_status_count_for_customer
----------- | -------- | ------------ | --------------------------------
1           | 1        | delivered    | 2
1           | 2        | delivered    | 2
1           | 3        | shipped      | 1
2           | 4        | paid         | 1
2           | 5        | delivered    | 1
2           | 6        | pending      | 1
3           | 7        | delivered    | 1
4           | 8        | delivered    | 2
4           | 9        | delivered    | 2
5           | 10       | paid         | 1
6           | 11       | shipped      | 1
7           | 12       | pending      | 1
8           | 13       | delivered    | 1
8           | 14       | paid         | 1


Q34. Orders where amount > previous order (per customer)
SQL:
WITH compared AS (
    SELECT
        customer_id,
        order_id,
        order_date,
        total_amount,
        LAG(total_amount) OVER (
            PARTITION BY customer_id
            ORDER BY order_date
        ) AS prev_amount
    FROM ecom.orders
)
SELECT *
FROM compared
WHERE prev_amount IS NOT NULL
  AND total_amount > prev_amount
ORDER BY customer_id, order_date;

Expected output:
customer_id | order_id | order_date           | total_amount | prev_amount
----------- | -------- | -------------------- | ------------ | -----------
1           | 2        | 2024-03-10 14:30:00  |     45.00    |    25.00
2           | 6        | 2024-04-01 13:20:00  |     80.50    |    40.00


Q35. Second-highest order amount per customer
SQL:
WITH per_order AS (
    SELECT
        customer_id,
        total_amount,
        DENSE_RANK() OVER (
            PARTITION BY customer_id
            ORDER BY total_amount DESC
        ) AS amt_rank
    FROM ecom.orders
)
SELECT
    customer_id,
    total_amount AS second_highest_amount
FROM per_order
WHERE amt_rank = 2
ORDER BY customer_id;

Expected output:
customer_id | second_highest_amount
----------- | ----------------------
1           |     25.00
2           |     80.50
4           |    120.00
8           |    500.00

(Other customers only have one distinct order amount, so no second highest.)

Q36. Peak order per month per customer
SQL:
WITH monthly_orders AS (
    SELECT
        customer_id,
        order_id,
        order_date,
        to_char(order_date, 'YYYY-MM') AS year_month,
        total_amount,
        RANK() OVER (
            PARTITION BY customer_id, to_char(order_date, 'YYYY-MM')
            ORDER BY total_amount DESC
        ) AS amt_rank
    FROM ecom.orders
)
SELECT
    customer_id,
    year_month,
    order_id,
    total_amount
FROM monthly_orders
WHERE amt_rank = 1
ORDER BY customer_id, year_month;

Expected output:
customer_id | year_month | order_id | total_amount
----------- | ---------- | -------- | -----------
1           | 2024-03    | 2        |    45.00
2           | 2024-03    | 4        |   300.00
2           | 2024-04    | 6        |    80.50
3           | 2024-03    | 7        |    25.00
4           | 2024-03    | 8        |  1500.00
5           | 2024-04    | 10       |    30.00
6           | 2024-03    | 11       |   220.75
7           | 2024-04    | 12       |    50.00
8           | 2024-04    | 13       |  2000.00


Q37. Delivered revenue vs total revenue per customer
SQL:
SELECT
    customer_id,
    order_id,
    order_status,
    total_amount,
    SUM(CASE WHEN order_status = 'delivered' THEN total_amount ELSE 0 END)
        OVER (PARTITION BY customer_id) AS delivered_revenue_per_customer,
    SUM(total_amount) OVER (
        PARTITION BY customer_id
    ) AS total_revenue_per_customer
FROM ecom.orders
ORDER BY customer_id, order_id;

Expected output:
customer_id | order_id | order_status | total_amount | delivered_revenue_per_customer | total_revenue_per_customer
----------- | -------- | ------------ | ------------ | ------------------------------ | ---------------------------
1           | 1        | delivered    |     25.00    |       70.00                    |  90.00
1           | 2        | delivered    |     45.00    |       70.00                    |  90.00
1           | 3        | shipped      |     20.00    |       70.00                    |  90.00
2           | 4        | paid         |    300.00    |       40.00                    | 420.50
2           | 5        | delivered    |     40.00    |       40.00                    | 420.50
2           | 6        | pending      |     80.50    |       40.00                    | 420.50
3           | 7        | delivered    |     25.00    |       25.00                    |  25.00
4           | 8        | delivered    |   1500.00    |     1620.00                    | 1620.00
4           | 9        | delivered    |    120.00    |     1620.00                    | 1620.00
5           | 10       | paid         |     30.00    |        0.00                    |  30.00
6           | 11       | shipped      |    220.75    |        0.00                    | 220.75
7           | 12       | pending      |     50.00    |        0.00                    |  50.00
8           | 13       | delivered    |   2000.00    |     2000.00                    | 2500.00
8           | 14       | paid         |    500.00    |     2000.00                    | 2500.00


Q38. Compare each order to global avg order amount
SQL:
SELECT
    order_id,
    customer_id,
    total_amount,
    AVG(total_amount) OVER () AS global_avg_order_amount,
    CASE
        WHEN total_amount >
             AVG(total_amount) OVER ()
        THEN 'above_global_avg'
        ELSE 'below_or_equal_global_avg'
    END AS vs_global_avg
FROM ecom.orders
ORDER BY order_id;

Global average across all orders = 354.017857...
Expected output:
order_id | customer_id | total_amount | global_avg_order_amount | vs_global_avg
-------- | ----------- | ------------ | ------------------------ | --------------------------
1        | 1           |     25.00    | 354.017857              | below_or_equal_global_avg
2        | 1           |     45.00    | 354.017857              | below_or_equal_global_avg
3        | 1           |     20.00    | 354.017857              | below_or_equal_global_avg
4        | 2           |    300.00    | 354.017857              | below_or_equal_global_avg
5        | 2           |     40.00    | 354.017857              | below_or_equal_global_avg
6        | 2           |     80.50    | 354.017857              | below_or_equal_global_avg
7        | 3           |     25.00    | 354.017857              | below_or_equal_global_avg
8        | 4           |   1500.00    | 354.017857              | above_global_avg
9        | 4           |    120.00    | 354.017857              | below_or_equal_global_avg
10       | 5           |     30.00    | 354.017857              | below_or_equal_global_avg
11       | 6           |    220.75    | 354.017857              | below_or_equal_global_avg
12       | 7           |     50.00    | 354.017857              | below_or_equal_global_avg
13       | 8           |   2000.00    | 354.017857              | above_global_avg
14       | 8           |    500.00    | 354.017857              | above_global_avg


Q39. Rank orders by time within country
SQL:
SELECT
    c.country,
    o.customer_id,
    o.order_id,
    o.order_date,
    RANK() OVER (
        PARTITION BY c.country
        ORDER BY o.order_date
    ) AS order_time_rank_in_country
FROM ecom.orders o
JOIN ecom.customers c ON c.customer_id = o.customer_id
ORDER BY c.country, order_time_rank_in_country;

Expected output:
country | customer_id | order_id | order_date           | order_time_rank_in_country
------- | ----------- | -------- | -------------------- | --------------------------
Canada  | 3           | 7        | 2024-03-18 08:30:00  | 1
Japan   | 8           | 13       | 2024-04-10 12:00:00  | 1
Japan   | 8           | 14       | 2024-04-15 18:30:00  | 2
Mexico  | 4           | 8        | 2024-03-22 19:00:00  | 1
Mexico  | 4           | 9        | 2024-03-30 10:10:00  | 2
UK      | 6           | 11       | 2024-03-29 15:00:00  | 1
USA     | 1           | 1        | 2024-03-01 10:15:00  | 1
USA     | 1           | 2        | 2024-03-10 14:30:00  | 2
USA     | 1           | 3        | 2024-03-15 09:00:00  | 3
USA     | 2           | 4        | 2024-03-20 11:00:00  | 4
USA     | 2           | 5        | 2024-03-25 16:45:00  | 5
USA     | 2           | 6        | 2024-04-01 13:20:00  | 6
USA     | 5           | 10       | 2024-04-02 09:45:00  | 7
USA     | 7           | 12       | 2024-04-02 20:00:00  | 8


Q40. Customers whose two most recent orders are both > their avg
SQL:
WITH avg_per_customer AS (
    SELECT
        customer_id,
        AVG(total_amount) AS avg_amount
    FROM ecom.orders
    GROUP BY customer_id
),
ranked_orders AS (
    SELECT
        o.*,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY o.order_date DESC
        ) AS rn
    FROM ecom.orders o
)
SELECT DISTINCT
    r.customer_id
FROM ranked_orders r
JOIN avg_per_customer a
  ON a.customer_id = r.customer_id
WHERE r.rn <= 2
GROUP BY r.customer_id, a.avg_amount
HAVING COUNT(*) FILTER (
           WHERE r.total_amount > a.avg_amount
       ) = 2
ORDER BY r.customer_id;

Expected output:
-- No rows (empty result set)

For no customer are both of their two most recent orders strictly above their own average.

How to use this for prep
You now have 40 solid questions total:
First 20: core SELECT, joins, group by, CTE, CASE


Next 20: window functions-heavy (exactly the style used at fintech & media companies)


If you want, next I can:
Turn all 40 into a printable checklist (question only).


Create a “mock interview”: I’ll pick 8–10 from these and ask you to solve them, then we compare.


Add a 3rd table (products or payments) and design more system-design-ish SQL questions.




Part 1 – Full 40-Question Printable Checklist (Question Only)
A. Core SQL, Joins, Aggregations, CTEs, CASE (Q1–Q20)
Q1.
 Return each customer’s total amount spent across all orders.
 Columns: customer_id, customer_name, total_spent (sum of orders.total_amount).

Q2.
 Find the top 3 customers by total spend (sum of total_amount).
 Order by total spend descending.

Q3.
 Return the number of orders per order_status.
 Columns: order_status, order_count.

Q4.
 For each customer, return their most recent order_date.
 Columns: customer_id, customer_name, last_order_date.

Q5.
 Find customers who have at least one order with order_status = 'pending'.
 Return distinct customer_id, customer_name.

Q6.
 Segment each customer as low, medium, or high spender based on total spend:
< 100 → low


100–1000 → medium


> 1000 → high


Return customer_id, customer_name, total_spent, spend_segment.

Q7.
 Using a window function, return each customer’s most recent order row (one row per customer).
 Columns: customer_id, order_id, order_date, total_amount.

Q8.
 For each customer, show their orders in time order and the running total of total_amount.
 Columns: customer_id, order_id, order_date, total_amount, running_total.

Q9.
 For each product, compute its total revenue and number of orders.
 Columns: product_id, product_name, revenue, order_count.
 Order by revenue descending.

Q10.
 For each country, show the number of distinct customers and total revenue (sum of their orders).
 Columns: country, customer_count, total_revenue.

Q11.
 Compute order count and average order amount by payment_method.
 Columns: payment_method, order_count, avg_amount.

Q12.
 Return customers who have at least one order and all their orders use payment_method = 'credit_card'.
 Columns: customer_id, customer_name.

Q13.
 Find customers who have placed more than 2 orders.
 Columns: customer_id, customer_name, order_count.

Q14.
 Group revenue by calendar month (e.g. 2024-03, 2024-04).
 Columns: year_month, total_revenue, order_count.

Q15.
 For each customer, compute the number of days since their previous order.
 Columns: customer_id, order_id, order_date, prev_order_date, days_since_prev.

Q16.
 Compute each customer’s total spend and their percentage of overall revenue.
 Columns: customer_id, customer_name, total_spent, pct_of_revenue.

Q17.
 For each customer, return first_order_date, last_order_date, and order_count.

Q18.
 Return customers who have orders in both March 2024 and April 2024.
 Columns: customer_id, customer_name.

Q19.
 For each customer, find the single order where they spent the most (highest total_amount).
 Columns: customer_id, product_id, product_name, top_spend_amount.

Q20.
 Compare customers.total_purchases vs actual sum of orders.total_amount.
 Return customers where they don’t match.
 Columns: customer_id, customer_name, total_purchases, total_spent.

B. Window / Analytic Function–Heavy (Q21–Q40)
Q21.
 Rank customers by total spend using RANK() (1 = highest spender).
 Columns: customer_id, customer_name, total_spent, spend_rank.

Q22.
 Within each country, use DENSE_RANK() to rank customers by total spend (1 = highest within that country).
 Columns: country, customer_id, customer_name, total_spent, country_rank.

Q23.
 For each customer, return at most 2 orders with the highest total_amount using ROW_NUMBER().
 Columns: customer_id, order_id, order_date, total_amount.

Q24.
 For each customer, show each order and how much its total_amount differs from their previous order’s total_amount (using LAG).
 Columns: customer_id, order_id, order_date, total_amount, prev_amount, diff_from_prev.

Q25.
 For each customer, compute days to the next order (using LEAD).
 Columns: customer_id, order_id, order_date, next_order_date, days_to_next_order.

Q26.
 For each order, show the first product_name that customer ever bought (using FIRST_VALUE).
 Columns: customer_id, order_id, order_date, product_name, first_product_for_customer.

Q27.
 Flag each order as 'FIRST', 'LAST', or NULL depending on whether it’s the customer’s first, last, or neither order (using FIRST_VALUE / LAST_VALUE + CASE).
 Columns: customer_id, order_id, order_date, total_amount, position_flag.

Q28.
 For each order, compute cumulative spend per country ordered by order_date (join customers + orders and use SUM() OVER(PARTITION BY country ...)).
 Columns: country, customer_id, order_id, order_date, total_amount, running_country_revenue.

Q29.
 For each order, compute what percentage of that customer’s total spend this order represents.
 Columns: customer_id, order_id, total_amount, customer_total, pct_of_customer_spend.

Q30.
 Find customers whose largest single order is more than 50% of their total spend (using window SUM and MAX over PARTITION BY customer_id).
 Columns: customer_id.

Q31.
 Return the N most recent orders per customer (use ROW_NUMBER ordered by order_date DESC and filter on rn <= N; practice with N = 2).
 Columns: customer_id, order_id, order_date, total_amount.

Q32.
 For each order, compare total_amount with average order amount for that customer, and label as 'above_avg' or 'below_or_equal' using CASE and AVG() OVER (PARTITION BY customer_id).
 Columns: customer_id, order_id, total_amount, avg_for_customer, size_vs_avg.

Q33.
 For each order, show how many orders that customer has with the same order_status (using COUNT(*) OVER (PARTITION BY customer_id, order_status)).
 Columns: customer_id, order_id, order_status, same_status_count_for_customer.

Q34.
 Identify orders where the total_amount is strictly greater than the previous order’s total_amount for that customer (use LAG + WHERE).
 Return all such “increasing” orders.

Q35.
 For each customer, find their 2nd highest order amount (if it exists), using DENSE_RANK() over total_amount DESC.
 Columns: customer_id, second_highest_amount.

Q36.
 For each year_month (like 2024-03) and customer, find the highest total_amount order they made that month, using RANK over (customer_id, year_month) and filter to rank = 1.
 Columns: customer_id, year_month, order_id, total_amount.

Q37.
 For each order, compute:
total delivered revenue per customer (sum only where order_status = 'delivered'), and


total revenue per customer (all statuses)


using window SUM(CASE WHEN...) OVER (PARTITION BY customer_id).
 Columns: customer_id, order_id, order_status, total_amount, delivered_revenue_per_customer, total_revenue_per_customer.

Q38.
 Compare each order’s total_amount to the global average order amount across all orders (no partition in AVG() OVER).
 Label as 'above_global_avg' or 'below_or_equal_global_avg'.
 Columns: order_id, customer_id, total_amount, global_avg_order_amount, vs_global_avg.

Q39.
 For each country, rank orders by time (earliest order in that country = rank 1) using RANK() OVER (PARTITION BY country ORDER BY order_date).
 Columns: country, customer_id, order_id, order_date, order_time_rank_in_country.

Q40.
 Find customers whose two most recent orders are both greater than that customer’s average order amount.
 Use CTEs + ROW_NUMBER for recency + AVG per customer, and a HAVING with COUNT(*) FILTER logic.
 Columns: customer_id.

🎯 Part 2 – Mock Interview Set (10 Questions)
If you want to simulate a real interview round, focus on these 10 first. Try to solve on your own without looking back:
Mock Q1. (From Q6)
 Segment each customer as low, medium, or high spender using CASE based on total spend thresholds.
Mock Q2. (From Q7)
 Return each customer’s most recent order row using a window function and a CTE.
Mock Q3. (From Q11)
 Find order count and average order amount by payment_method.
Mock Q4. (From Q16)
 Find each customer’s total spend and their percentage of overall revenue across all customers.
Mock Q5. (From Q20)
 Return customers where customers.total_purchases does not equal the sum of orders.total_amount. Classic “data reconciliation” problem.
Mock Q6. (From Q23)
 For each customer, return at most 2 orders with highest total_amount using ROW_NUMBER().
Mock Q7. (From Q29)
 For each order, compute what percentage of that customer’s total spend this order represents.
Mock Q8. (From Q32)
 For each order, compare total_amount to the average order amount for that customer and label 'above_avg' vs 'below_or_equal'.
Mock Q9. (From Q35)
 For each customer, find the second highest order amount (if any).
Mock Q10. (From Q40)
 Find customers whose two most recent orders are both greater than that customer’s average order amount.
Schema reminder (in schema ecom):
ecom.customers(
  customer_id INT PK,
  customer_name VARCHAR,
  email VARCHAR,
  registration_date DATE,
  customer_type VARCHAR,
  country VARCHAR,
  total_purchases NUMERIC,
  last_purchase_date DATE
);

ecom.orders(
  order_id INT PK,
  customer_id INT FK,
  order_date TIMESTAMP,
  product_id INT,
  product_name VARCHAR,
  quantity INT,
  unit_price NUMERIC,
  total_amount NUMERIC,
  payment_method VARCHAR,
  order_status VARCHAR
);

I’m assuming the same 8 customers and 14 orders we used earlier.

Q41. Customers who never placed an order (anti-join)
Question: Return customers with no orders.
SQL:
SELECT
    c.customer_id,
    c.customer_name,
    c.email,
    c.country
FROM ecom.customers c
LEFT JOIN ecom.orders o
    ON o.customer_id = c.customer_id
WHERE o.customer_id IS NULL
ORDER BY c.customer_id;

Expected output:
-- No rows (empty result)

All 8 customers have at least one order in our sample.

Q42. Customers with orders but zero total_purchases
Question: Customers who have at least one order and total_purchases = 0.
SQL:
SELECT
    c.customer_id,
    c.customer_name,
    c.total_purchases,
    COUNT(o.order_id) AS order_count
FROM ecom.customers c
JOIN ecom.orders o
  ON o.customer_id = c.customer_id
WHERE c.total_purchases = 0
GROUP BY c.customer_id, c.customer_name, c.total_purchases
ORDER BY c.customer_id;

Expected output:
customer_id | customer_name | total_purchases | order_count
----------- | ------------- | --------------- | -----------
5           | Ethan Lee     |          0.00   |     1


Q43. Distinct product count per customer (>=3)
Question: For each customer, count distinct products, return only those with ≥3.
SQL:
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(DISTINCT o.product_id) AS distinct_product_count
FROM ecom.customers c
JOIN ecom.orders o
  ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(DISTINCT o.product_id) >= 3
ORDER BY c.customer_id;

Expected output:
customer_id | customer_name | distinct_product_count
----------- | ------------- | ----------------------
1           | Alice Johnson | 3
2           | Bob Smith     | 3


Q44. High average order amount (HAVING)
Question: Customers with AVG(total_amount) > 200.
SQL:
SELECT
    c.customer_id,
    c.customer_name,
    AVG(o.total_amount) AS avg_order_amount
FROM ecom.customers c
JOIN ecom.orders o
  ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING AVG(o.total_amount) > 200
ORDER BY c.customer_id;

Expected output:
customer_id | customer_name | avg_order_amount
----------- | ------------- | ----------------
4           | Diana Lopez   |       810.00
6           | Fatima Khan   |       220.75
8           | Hiro Tanaka   |      1250.00


Q45. Orders larger than customer’s own average (correlated subquery)
SQL:
SELECT
    o.order_id,
    o.customer_id,
    o.order_date,
    o.total_amount
FROM ecom.orders o
WHERE o.total_amount >
      (
        SELECT AVG(o2.total_amount)
        FROM ecom.orders o2
        WHERE o2.customer_id = o.customer_id
      )
ORDER BY o.customer_id, o.order_id;

Expected output:
order_id | customer_id | order_date           | total_amount
-------- | ----------- | -------------------- | -----------
2        | 1           | 2024-03-10 14:30:00  |     45.00
4        | 2           | 2024-03-20 11:00:00  |    300.00
8        | 4           | 2024-03-22 19:00:00  |   1500.00
13       | 8           | 2024-04-10 12:00:00  |   2000.00


Q46. Last order amount per customer (scalar subqueries)
SQL:
SELECT
    c.customer_id,
    c.customer_name,
    /* latest order_date for that customer */
    (
      SELECT o.order_date
      FROM ecom.orders o
      WHERE o.customer_id = c.customer_id
      ORDER BY o.order_date DESC
      LIMIT 1
    ) AS last_order_date,
    /* amount of that latest order */
    (
      SELECT o2.total_amount
      FROM ecom.orders o2
      WHERE o2.customer_id = c.customer_id
      ORDER BY o2.order_date DESC
      LIMIT 1
    ) AS last_order_amount
FROM ecom.customers c
ORDER BY c.customer_id;

Expected output:
customer_id | customer_name | last_order_date       | last_order_amount
----------- | ------------- | --------------------- | -----------------
1           | Alice Johnson | 2024-03-15 09:00:00   |     20.00
2           | Bob Smith     | 2024-04-01 13:20:00   |     80.50
3           | Charlie Singh | 2024-03-18 08:30:00   |     25.00
4           | Diana Lopez   | 2024-03-30 10:10:00   |    120.00
5           | Ethan Lee     | 2024-04-02 09:45:00   |     30.00
6           | Fatima Khan   | 2024-03-29 15:00:00   |    220.75
7           | George Brown  | 2024-04-02 20:00:00   |     50.00
8           | Hiro Tanaka   | 2024-04-15 18:30:00   |    500.00


Q47. total_purchases within ±10% of actual order sum
SQL:
WITH order_sums AS (
    SELECT
        customer_id,
        SUM(total_amount) AS sum_orders
    FROM ecom.orders
    GROUP BY customer_id
)
SELECT
    c.customer_id,
    c.customer_name,
    c.total_purchases,
    os.sum_orders,
    100.0 * (c.total_purchases - os.sum_orders) / os.sum_orders
        AS pct_difference
FROM ecom.customers c
JOIN order_sums os
  ON os.customer_id = c.customer_id
WHERE ABS(100.0 * (c.total_purchases - os.sum_orders) / os.sum_orders) <= 10
ORDER BY c.customer_id;

Expected output:
customer_id | customer_name | total_purchases | sum_orders | pct_difference
----------- | ------------- | --------------- | ---------- | --------------
7           | George Brown  |        50.00    |    50.00   |      0.00

Only George’s total_purchases matches his order sum closely enough.

Q48. Most popular product by distinct customers
SQL:
WITH product_counts AS (
    SELECT
        product_id,
        product_name,
        COUNT(DISTINCT customer_id) AS customer_count
    FROM ecom.orders
    GROUP BY product_id, product_name
),
max_count AS (
    SELECT MAX(customer_count) AS max_customer_count
    FROM product_counts
)
SELECT
    p.product_id,
    p.product_name,
    p.customer_count
FROM product_counts p
JOIN max_count m
  ON p.customer_count = m.max_customer_count
ORDER BY p.product_id;

Expected output:
product_id | product_name    | customer_count
---------- | --------------- | --------------
101        | Wireless Mouse  | 3


Q49. Pivot-style status counts per customer (SUM(CASE))
SQL:
SELECT
    c.customer_id,
    c.customer_name,
    SUM(CASE WHEN o.order_status = 'pending'   THEN 1 ELSE 0 END) AS pending_count,
    SUM(CASE WHEN o.order_status = 'paid'      THEN 1 ELSE 0 END) AS paid_count,
    SUM(CASE WHEN o.order_status = 'shipped'   THEN 1 ELSE 0 END) AS shipped_count,
    SUM(CASE WHEN o.order_status = 'delivered' THEN 1 ELSE 0 END) AS delivered_count
FROM ecom.customers c
LEFT JOIN ecom.orders o
  ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY c.customer_id;

Expected output:
customer_id | customer_name | pending_count | paid_count | shipped_count | delivered_count
----------- | ------------- | ------------- | ---------- | ------------- | ----------------
1           | Alice Johnson |      0        |     0      |      1        |       2
2           | Bob Smith     |      1        |     1      |      0        |       1
3           | Charlie Singh |      0        |     0      |      0        |       1
4           | Diana Lopez   |      0        |     0      |      0        |       2
5           | Ethan Lee     |      0        |     1      |      0        |       0
6           | Fatima Khan   |      0        |     0      |      1        |       0
7           | George Brown  |      1        |     0      |      0        |       0
8           | Hiro Tanaka   |      0        |     1      |      0        |       1


Q50. Customers with multiple orders on the same day
SQL:
SELECT
    c.customer_id,
    c.customer_name,
    DATE(o.order_date) AS order_date_only,
    COUNT(*) AS order_count_on_date
FROM ecom.customers c
JOIN ecom.orders o
  ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name, DATE(o.order_date)
HAVING COUNT(*) > 1
ORDER BY c.customer_id, order_date_only;

Expected output:
-- No rows (empty result)

In this dataset, no customer has >1 order on the same calendar date.

Q51. Most recent row per order_id (status history pattern)
SQL (window function version):
SELECT *
FROM (
    SELECT
        o.order_id,
        o.customer_id,
        o.order_date,
        o.order_status,
        o.total_amount,
        ROW_NUMBER() OVER (
            PARTITION BY o.order_id
            ORDER BY o.order_date DESC
        ) AS rn
    FROM ecom.orders o
) t
WHERE rn = 1
ORDER BY order_id;

Expected output: (here each order_id only has one row, so all 14 appear)
order_id | customer_id | order_date           | order_status | total_amount
-------- | ----------- | -------------------- | ------------ | -----------
1        | 1           | 2024-03-01 10:15:00  | delivered    |     25.00
2        | 1           | 2024-03-10 14:30:00  | delivered    |     45.00
3        | 1           | 2024-03-15 09:00:00  | shipped      |     20.00
4        | 2           | 2024-03-20 11:00:00  | paid         |    300.00
5        | 2           | 2024-03-25 16:45:00  | delivered    |     40.00
6        | 2           | 2024-04-01 13:20:00  | pending      |     80.50
7        | 3           | 2024-03-18 08:30:00  | delivered    |     25.00
8        | 4           | 2024-03-22 19:00:00  | delivered    |   1500.00
9        | 4           | 2024-03-30 10:10:00  | delivered    |    120.00
10       | 5           | 2024-04-02 09:45:00  | paid         |     30.00
11       | 6           | 2024-03-29 15:00:00  | shipped      |    220.75
12       | 7           | 2024-04-02 20:00:00  | pending      |     50.00
13       | 8           | 2024-04-10 12:00:00  | delivered    |   2000.00
14       | 8           | 2024-04-15 18:30:00  | paid         |    500.00


Q52. Daily revenue + moving 3-day average
SQL (two-step with CTE):
WITH daily AS (
    SELECT
        DATE(order_date) AS order_date_only,
        SUM(total_amount) AS daily_revenue
    FROM ecom.orders
    GROUP BY DATE(order_date)
)
SELECT
    order_date_only,
    daily_revenue,
    AVG(daily_revenue) OVER (
        ORDER BY order_date_only
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_3_day_avg
FROM daily
ORDER BY order_date_only;

Expected output (rounded to 2 decimals):
order_date_only | daily_revenue | moving_3_day_avg
--------------- | ------------- | ----------------
2024-03-01      |     25.00     |     25.00
2024-03-10      |     45.00     |     35.00
2024-03-15      |     20.00     |     30.00
2024-03-18      |     25.00     |     30.00
2024-03-20      |    300.00     |    115.00
2024-03-22      |   1500.00     |    608.33
2024-03-25      |     40.00     |    613.33
2024-03-29      |    220.75     |    586.92
2024-03-30      |    120.00     |    126.92
2024-04-01      |     80.50     |    140.42
2024-04-02      |     80.00     |     93.50
2024-04-10      |   2000.00     |    720.17
2024-04-15      |    500.00     |    860.00


Q53. High-value customers and top product (multi-CTE)
SQL:
WITH customer_totals AS (
    SELECT
        customer_id,
        SUM(total_amount) AS total_spent
    FROM ecom.orders
    GROUP BY customer_id
),
high_value AS (
    SELECT *
    FROM customer_totals
    WHERE total_spent > 1000
),
product_spend AS (
    SELECT
        o.customer_id,
        o.product_id,
        o.product_name,
        SUM(o.total_amount) AS product_spend
    FROM ecom.orders o
    JOIN high_value h
      ON h.customer_id = o.customer_id
    GROUP BY o.customer_id, o.product_id, o.product_name
),
top_product AS (
    SELECT *
    FROM (
        SELECT
            customer_id,
            product_id,
            product_name,
            product_spend,
            ROW_NUMBER() OVER (
                PARTITION BY customer_id
                ORDER BY product_spend DESC
            ) AS rn
        FROM product_spend
    ) t
    WHERE rn = 1
)
SELECT
    c.customer_id,
    cu.customer_name,
    c.total_spent,
    t.product_name AS top_product_name,
    t.product_spend AS top_product_spend
FROM high_value c
JOIN top_product t
  ON t.customer_id = c.customer_id
JOIN ecom.customers cu
  ON cu.customer_id = c.customer_id
ORDER BY c.customer_id;

Expected output:
customer_id | customer_name | total_spent | top_product_name | top_product_spend
----------- | ------------- | ----------- | ---------------- | -----------------
4           | Diana Lopez   |   1620.00   | Gaming Laptop    |   1500.00
8           | Hiro Tanaka   |   2500.00   | 4K TV            |   2000.00


Q54. Customers who only ever used PayPal (set logic)
SQL (EXCEPT pattern):
WITH paypal_customers AS (
    SELECT DISTINCT customer_id
    FROM ecom.orders
    WHERE payment_method = 'paypal'
),
non_paypal_customers AS (
    SELECT DISTINCT customer_id
    FROM ecom.orders
    WHERE payment_method <> 'paypal'
)
SELECT
    c.customer_id,
    c.customer_name
FROM ecom.customers c
JOIN paypal_customers p
  ON p.customer_id = c.customer_id
WHERE c.customer_id NOT IN (SELECT customer_id FROM non_paypal_customers)
ORDER BY c.customer_id;

Expected output:
customer_id | customer_name
----------- | -------------
5           | Ethan Lee


Q55. Customers sharing duplicate emails
SQL:
WITH email_counts AS (
    SELECT
        email,
        COUNT(*) AS cnt
    FROM ecom.customers
    GROUP BY email
    HAVING COUNT(*) > 1
)
SELECT
    c.email,
    c.customer_id,
    c.customer_name
FROM ecom.customers c
JOIN email_counts e
  ON e.email = c.email
ORDER BY c.email, c.customer_id;

Expected output:
-- No rows (empty result)

All emails are unique in this sample.

Q56. Email domains with ≥2 customers
SQL:
WITH domains AS (
    SELECT
        SUBSTRING(email FROM POSITION('@' IN email) + 1) AS email_domain
    FROM ecom.customers
),
domain_counts AS (
    SELECT
        email_domain,
        COUNT(*) AS customer_count
    FROM domains
    GROUP BY email_domain
)
SELECT
    email_domain,
    customer_count
FROM domain_counts
WHERE customer_count >= 2
ORDER BY email_domain;

Expected output:
email_domain | customer_count
------------ | --------------
example.com  | 8


Q57. Orders within 30 days of registration + cumulative spend
SQL:
WITH joined AS (
    SELECT
        o.customer_id,
        o.order_id,
        o.order_date,
        o.total_amount,
        c.registration_date,
        (DATE(o.order_date) - c.registration_date) AS days_since_registration
    FROM ecom.orders o
    JOIN ecom.customers c
      ON c.customer_id = o.customer_id
),
within_30 AS (
    SELECT *
    FROM joined
    WHERE days_since_registration BETWEEN 0 AND 30
)
SELECT
    customer_id,
    order_id,
    order_date,
    days_since_registration,
    total_amount,
    SUM(total_amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_30_day_spend
FROM within_30
ORDER BY customer_id, order_date;

Expected output:
customer_id | order_id | order_date           | days_since_registration | total_amount | cumulative_30_day_spend
----------- | -------- | -------------------- | ----------------------- | ------------ | -----------------------
3           | 7        | 2024-03-18 08:30:00  | 27                      |     25.00    |       25.00
4           | 8        | 2024-03-22 19:00:00  | 21                      |   1500.00    |     1500.00
4           | 9        | 2024-03-30 10:10:00  | 29                      |    120.00    |     1620.00
5           | 10       | 2024-04-02 09:45:00  | 18                      |     30.00    |       30.00
6           | 11       | 2024-03-29 15:00:00  | 9                       |    220.75    |      220.75
7           | 12       | 2024-04-02 20:00:00  | 1                       |     50.00    |       50.00
8           | 13       | 2024-04-10 12:00:00  | 5                       |   2000.00    |     2000.00
8           | 14       | 2024-04-15 18:30:00  | 10                      |    500.00    |     2500.00

(Alice and Bob’s first orders were more than 30 days after registration, so they don’t show up.)

Q58. Customers with >60-day inactivity gaps
SQL:
WITH ordered AS (
    SELECT
        o.customer_id,
        o.order_id,
        o.order_date,
        LAG(o.order_date) OVER (
            PARTITION BY o.customer_id
            ORDER BY o.order_date
        ) AS prev_order_date
    FROM ecom.orders o
),
gaps AS (
    SELECT
        customer_id,
        EXTRACT(DAY FROM (order_date - prev_order_date)) AS gap_days
    FROM ordered
    WHERE prev_order_date IS NOT NULL
),
max_gaps AS (
    SELECT
        customer_id,
        MAX(gap_days) AS max_gap_days
    FROM gaps
    GROUP BY customer_id
)
SELECT
    c.customer_id,
    c.customer_name,
    m.max_gap_days
FROM max_gaps m
JOIN ecom.customers c
  ON c.customer_id = m.customer_id
WHERE m.max_gap_days > 60
ORDER BY c.customer_id;

Expected output:
-- No rows (empty result)

All gaps between consecutive orders are under 10 days in this dataset.

Q59. Median order amount per customer (customers with ≥3 orders)
SQL (one possible pattern):
WITH ordered_amounts AS (
    SELECT
        o.customer_id,
        o.total_amount,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY o.total_amount
        ) AS rn_asc,
        COUNT(*) OVER (
            PARTITION BY o.customer_id
        ) AS cnt
    FROM ecom.orders o
),
medians AS (
    SELECT
        customer_id,
        total_amount AS median_order_amount
    FROM ordered_amounts
    WHERE cnt >= 3
      AND rn_asc = (cnt + 1) / 2  -- works for odd cnt
)
SELECT
    m.customer_id,
    c.customer_name,
    m.median_order_amount
FROM medians m
JOIN ecom.customers c
  ON c.customer_id = m.customer_id
ORDER BY m.customer_id;

(Note: this version is tuned for odd counts; here both eligible customers have exactly 3 orders.)
Expected output:
customer_id | customer_name | median_order_amount
----------- | ------------- | -------------------
1           | Alice Johnson |     25.00
2           | Bob Smith     |     80.50


Q60. Churn-like flag: active vs churned (60 days)
Assume CURRENT_DATE = '2024-05-01'
 “Last 60 days” ⇒ from 2024-03-02 onward.
SQL (Postgres-style):
WITH last_orders AS (
    SELECT
        customer_id,
        MAX(DATE(order_date)) AS last_order_date
    FROM ecom.orders
    GROUP BY customer_id
),
flags AS (
    SELECT
        c.customer_id,
        c.customer_name,
        l.last_order_date,
        CASE
            WHEN l.last_order_date >= (DATE '2024-05-01' - INTERVAL '60 days')
            THEN 'active'
            ELSE 'churned'
        END AS status_flag
    FROM ecom.customers c
    LEFT JOIN last_orders l
      ON l.customer_id = c.customer_id
)
SELECT *
FROM flags
ORDER BY customer_id;

Expected output:
All 8 have recent orders (on or after 2024-03-02):
customer_id | customer_name | last_order_date | status_flag
----------- | ------------- | --------------- | -----------
1           | Alice Johnson | 2024-03-15      | active
2           | Bob Smith     | 2024-04-01      | active
3           | Charlie Singh | 2024-03-18      | active
4           | Diana Lopez   | 2024-03-30      | active
5           | Ethan Lee     | 2024-04-02      | active
6           | Fatima Khan   | 2024-03-29      | active
7           | George Brown  | 2024-04-02      | active
8           | Hiro Tanaka   | 2024-04-15      | active


If you want, next step we can:

