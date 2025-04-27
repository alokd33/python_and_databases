--I'll provide you with several free online platforms where you can create and execute PostgreSQL commands:
--DB Fiddle
--URL: https://www.db-fiddle.com/
--Features:
--Free to use
--Supports PostgreSQL
--Easy to share queries
--No registration required
--Can create and modify tables
--Supports multiple database versions
--SQL Fiddle
--URL: http://sqlfiddle.com/
--Features:
--Free to use
--Supports PostgreSQL
--Simple interface
--No registration required
--Can create schema and run queries
--Rextester
--URL: https://rextester.com/
--Features:
--Free to use
--Supports PostgreSQL
--Can save and share code
--No registration required
--Good for testing queries
--OneCompiler
--URL: https://onecompiler.com/postgresql
--Features:
--Free to use
--Supports PostgreSQL
--Modern interface
--No registration required
--Can save and share code
--JDoodle
--URL: https://www.jdoodle.com/execute-postgresql-online/
--Features:
--Free to use
--Supports PostgreSQL
--Simple interface
--No registration required
--Can save and share code
--Here's a quick example of how to use DB Fiddle (one of the most user-friendly options):
--Go to https://www.db-fiddle.com/
--Select "PostgreSQL" from the database dropdown
--In the left panel (Schema), paste this code to create sample tables:
--Apply to parser.py
--;
--Click "Build Schema"
--In the right panel (Query), you can now run queries like:
--Apply to parser.py
--;
--Click "Run" to execute the query
--Benefits of using these online platforms:
--No installation required
--Instant access to PostgreSQL
--Can test queries without affecting production data
--Easy to share queries with others
--Good for learning and practice
--Can create and modify tables
--Support for multiple PostgreSQL versions
--Tips for using these platforms:
--Always start with creating your tables and inserting sample data
--Use the "Build Schema" button after creating tables
--Save your work if the platform supports it
--Use comments to document your queries
--Test queries in small chunks
--Use the "Format" button if available to make your SQL more readable
--Would you like me to:
--Provide more specific examples for any of these platforms?
--Show how to create more complex tables and queries?
--Explain how to save and share your work?
--Demonstrate specific PostgreSQL features on these platforms?


- =============================================
-- POSTGRESQL COMPREHENSIVE CHEAT SHEET
-- =============================================

-- 1. Create Sample Tables
-- ======================
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    registration_date DATE,
    customer_type VARCHAR(50),
    country VARCHAR(50),
    total_purchases DECIMAL(10,2),
    last_purchase_date DATE
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    order_date TIMESTAMP,
    product_id INTEGER,
    product_name VARCHAR(100),
    quantity INTEGER,
    unit_price DECIMAL(10,2),
    total_amount DECIMAL(10,2),
    payment_method VARCHAR(50),
    order_status VARCHAR(50)
);

-- 2. Insert Sample Data
-- ===================
INSERT INTO customers (customer_name, email, registration_date, customer_type, country, total_purchases, last_purchase_date)
VALUES
    ('John Doe', 'john@example.com', '2020-01-01', 'Premium', 'USA', 1500.00, '2023-01-15'),
    ('Jane Smith', 'jane@example.com', '2020-02-15', 'Regular', 'UK', 800.00, '2023-02-20'),
    ('Bob Johnson', 'bob@example.com', '2020-03-10', 'Premium', 'Canada', 2000.00, '2023-03-05'),
    ('Alice Brown', 'alice@example.com', '2020-04-20', 'Regular', 'Australia', 1200.00, '2023-04-10'),
    ('Charlie Wilson', 'charlie@example.com', '2020-05-05', 'Premium', 'USA', 3000.00, '2023-05-15');

--INSERT INTO orders (customer_id, order_date, product_id, product_name, quantity, unit_price, total_amount, payment_method, order_status)
--VALUES
--    (1, '2023-01-15 10:30:00', 101, 'Laptop', 1, 1000.00, 1000.00, 'Credit Card', 'Completed'),
--    (1, '2023-02-01 14:20:00', 102, 'Mouse', 2, 50.00, 100.00, 'PayPal', 'Completed'),
--    (2, '2023-02-20 09:15:00', 103, 'Keyboard', 1, 100.00, 100.00, 'Credit Card', 'Completed'),
--    (3, '2023-03-05 11:45:00', 104, 'Monitor', 2, 300.00, 600.00, 'Bank Transfer', 'Completed'),
--    (4, '2023-04-10 16:30:00', 105, 'Headphones', 1, 150.00, 150.00, 'Credit Card', 'Completed'),
--    (5, '2023-05-15 13:20:00', 106, 'Tablet', 1, 500.00, 500.00, 'PayPal', 'Completed');

--Updated data for ranking to see good results
INSERT INTO orders (customer_id, order_date, product_id, product_name, quantity, unit_price, total_amount, payment_method, order_status)
VALUES
    (1, '2023-01-15 10:30:00', 101, 'Laptop', 1, 1000.00, 1000.00, 'Credit Card', 'Completed'),
    (1, '2023-02-01 14:20:00', 102, 'Mouse', 2, 50.00, 100.00, 'PayPal', 'Completed'),
    (2, '2023-02-20 09:15:00', 103, 'Keyboard', 1, 100.00, 100.00, 'Credit Card', 'Completed'),
    (3, '2023-03-05 11:45:00', 104, 'Monitor', 2, 300.00, 600.00, 'Bank Transfer', 'Completed'),
    (4, '2023-04-10 16:30:00', 105, 'Headphones', 4, 150.00, 600.00, 'Credit Card', 'Completed'),
    (5, '2023-05-15 13:20:00', 106, 'Tablet', 1, 500.00, 500.00, 'PayPal', 'Completed');




-- 3. Basic SQL Functions
-- ====================
-- String Functions
SELECT
    customer_name,
    UPPER(customer_name) as upper_name,
    LOWER(customer_name) as lower_name,
    LENGTH(customer_name) as name_length,
    SUBSTRING(customer_name, 1, 3) as first_three,
    CONCAT(customer_name, ' (', country, ')') as full_info,
    REPLACE(customer_name, ' ', '_') as name_with_underscore
FROM customers;

-- Date Functions
SELECT
    order_date,
    EXTRACT(YEAR FROM order_date) as order_year,
    EXTRACT(MONTH FROM order_date) as order_month,
    DATE_TRUNC('month', order_date) as month_start,
    order_date + INTERVAL '1 day' as next_day,
    AGE(order_date) as order_age
FROM orders;

-- Numeric Functions
SELECT
    total_amount,
    ROUND(total_amount, 1) as rounded_amount,
    CEIL(total_amount) as ceiling_amount,
    FLOOR(total_amount) as floor_amount,
    ABS(total_amount) as absolute_amount,
    POWER(total_amount, 2) as squared_amount
FROM orders;

-- 4. Aggregate Functions
-- ====================
SELECT
    COUNT(*) as total_orders,
    SUM(total_amount) as total_revenue,
    AVG(total_amount) as average_order,
    MIN(total_amount) as min_order,
    MAX(total_amount) as max_order,
    STDDEV(total_amount) as std_dev_amount
FROM orders;

-- 5. Window Functions
-- =================
-- ROW_NUMBER
SELECT
    customer_name,
    total_amount,
    ROW_NUMBER() OVER (ORDER BY total_amount DESC) as rank
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

-- RANK and DENSE_RANK
SELECT
    customer_name,
    total_amount,
    ROW_NUMBER() OVER (ORDER BY total_amount DESC) as rank,
    RANK() OVER (ORDER BY total_amount DESC) as rank,
    DENSE_RANK() OVER (ORDER BY total_amount DESC) as dense_rank
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

-- LEAD and LAG
SELECT
    customer_name,
    order_date,
    total_amount,
    LEAD(total_amount) OVER (PARTITION BY c.customer_id ORDER BY order_date) as next_order_amount,
    LAG(total_amount) OVER (PARTITION BY c.customer_id ORDER BY order_date) as previous_order_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

-- 6. Advanced Analytics
-- ===================
-- Running Total
SELECT
    customer_name,
    order_date,
    total_amount,
    SUM(total_amount) OVER (PARTITION BY c.customer_id ORDER BY order_date) as running_total
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

-- Moving Average
SELECT
    customer_name,
    order_date,
    total_amount,
    AVG(total_amount) OVER (
        PARTITION BY c.customer_id
        ORDER BY order_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) as moving_avg
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

-- 7. Joins
-- =======
-- INNER JOIN
SELECT
    c.customer_name,
    o.order_date,
    o.total_amount
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;

-- LEFT JOIN
SELECT
    c.customer_name,
    o.order_date,
    o.total_amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- RIGHT JOIN
SELECT
    c.customer_name,
    o.order_date,
    o.total_amount
FROM customers c
RIGHT JOIN orders o ON c.customer_id = o.customer_id;

-- FULL OUTER JOIN
SELECT
    c.customer_name,
    o.order_date,
    o.total_amount
FROM customers c
FULL OUTER JOIN orders o ON c.customer_id = o.customer_id;

-- 8. Common Table Expressions (CTEs)
-- ================================
WITH customer_stats AS (
    SELECT
        customer_id,
        COUNT(*) as order_count,
        SUM(total_amount) as total_spent
    FROM orders
    GROUP BY customer_id
)
SELECT
    c.customer_name,
    cs.order_count,
    cs.total_spent
FROM customers c
JOIN customer_stats cs ON c.customer_id = cs.customer_id;

-- 9. Recursive CTEs
-- ================
WITH RECURSIVE date_series AS (
    SELECT DATE '2023-01-01' as date
    UNION ALL
    SELECT date + 1
    FROM date_series
    WHERE date < '2023-01-31'
)
SELECT date
FROM date_series;

-- 10. Pivot Operations
-- ==================
SELECT
    customer_type,
    COUNT(*) FILTER (WHERE payment_method = 'Credit Card') as credit_card_orders,
    COUNT(*) FILTER (WHERE payment_method = 'PayPal') as paypal_orders,
    COUNT(*) FILTER (WHERE payment_method = 'Bank Transfer') as bank_transfer_orders
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY customer_type;


SELECT DISTINCT
    customer_type,
    SUM(CASE WHEN payment_method = 'Credit Card' THEN 1 ELSE 0 END) OVER (PARTITION BY customer_type) AS credit_card_orders,
    SUM(CASE WHEN payment_method = 'PayPal' THEN 1 ELSE 0 END) OVER (PARTITION BY customer_type) AS paypal_orders,
    SUM(CASE WHEN payment_method = 'Bank Transfer' THEN 1 ELSE 0 END) OVER (PARTITION BY customer_type) AS bank_transfer_orders
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

-- 11. Time Series Analysis
-- ======================
SELECT
    DATE_TRUNC('month', order_date) as month,
    COUNT(*) as order_count,
    SUM(total_amount) as monthly_revenue,
    LAG(SUM(total_amount)) OVER (ORDER BY DATE_TRUNC('month', order_date)) as previous_month_revenue,
    (SUM(total_amount) - LAG(SUM(total_amount)) OVER (ORDER BY DATE_TRUNC('month', order_date))) /
    LAG(SUM(total_amount)) OVER (ORDER BY DATE_TRUNC('month', order_date)) * 100 as growth_percentage
FROM orders
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;

-- 12. Advanced Analytics Functions
-- =============================
-- Percentile
SELECT
    customer_type,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY total_amount) as median_amount,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY total_amount) as p75_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY customer_type;

-- First/Last Value
SELECT
    customer_name,
    order_date,
    total_amount,
    FIRST_VALUE(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date) as first_order_amount,
    LAST_VALUE(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as last_order_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

-- 13. Merge Operations
-- ==================
-- UPSERT (INSERT ... ON CONFLICT)
INSERT INTO customers (customer_id, customer_name, email)
VALUES (6, 'New Customer', 'new@example.com')
ON CONFLICT (customer_id)
DO UPDATE SET
    customer_name = EXCLUDED.customer_name,
    email = EXCLUDED.email;

-- 14. Advanced Joins
-- ================
-- Self Join
SELECT
    a.customer_name as customer1,
    b.customer_name as customer2,
    a.country
FROM customers a
JOIN customers b ON a.country = b.country AND a.customer_id < b.customer_id;

-- Cross Join
SELECT
    c.customer_name,
    p.product_name
FROM customers c
CROSS JOIN (SELECT DISTINCT product_name FROM orders) p;

-- 15. Advanced Filtering
-- ====================
-- Using HAVING
SELECT
    customer_type,
    COUNT(*) as order_count,
    SUM(total_amount) as total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY customer_type
HAVING SUM(total_amount) > 1000;

-- Using EXISTS
SELECT customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
    AND o.total_amount > 500
);

-- 16. Advanced Date Operations
-- =========================
SELECT
    customer_name,
    order_date,
    EXTRACT(DOW FROM order_date) as day_of_week,
    EXTRACT(DOY FROM order_date) as day_of_year,
    DATE_PART('quarter', order_date) as quarter,
    DATE_TRUNC('quarter', order_date) as quarter_start
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

-- =============================================
-- ADDITIONAL POSTGRESQL FUNCTIONS & OPERATIONS
-- =============================================

-- 1. Advanced String Functions
-- ==========================
SELECT
    customer_name,
    -- String manipulation
    TRIM(customer_name) as trimmed_name,
    LTRIM(customer_name) as left_trimmed,
    RTRIM(customer_name) as right_trimmed,
    -- Pattern matching
    REGEXP_REPLACE(customer_name, '[aeiou]', '*', 'g') as vowels_replaced,
    REGEXP_MATCHES(customer_name, '^[A-Z]') as starts_with_capital,
    -- String formatting
    FORMAT('Customer: %s, Email: %s', customer_name, email) as formatted_info,
    -- String position and length
    POSITION(' ' IN customer_name) as space_position,
    CHAR_LENGTH(customer_name) as char_length,
    OCTET_LENGTH(customer_name) as byte_length
FROM customers;

-- 2. Advanced Date/Time Functions
-- =============================
SELECT
    order_date,
    -- Time zone operations
    order_date AT TIME ZONE 'UTC' as utc_time,
    order_date AT TIME ZONE 'America/New_York' as ny_time,
    -- Interval operations
    order_date + INTERVAL '1 month' as next_month,
    order_date - INTERVAL '1 week' as last_week,
    -- Date parts
    DATE_PART('epoch', order_date) as unix_timestamp,
    TO_CHAR(order_date, 'YYYY-MM-DD HH24:MI:SS') as formatted_date,
    -- Date arithmetic
    AGE(order_date, registration_date) as customer_age,
    -- Date validation
    order_date IS NOT NULL as is_valid_date
FROM orders;

-- 3. Advanced Numeric Functions
-- ===========================
SELECT
    total_amount,
    -- Mathematical functions
    MOD(total_amount, 100) as remainder,
    SQRT(total_amount) as square_root,
    LOG(10, total_amount) as logarithm,
    -- Rounding functions
    TRUNC(total_amount, 2) as truncated,
    ROUND(total_amount, -2) as rounded_to_hundreds,
    -- Sign and absolute
    SIGN(total_amount) as sign,
    ABS(total_amount) as absolute_value,
    -- Random numbers
    RANDOM() * total_amount as random_amount
FROM orders;

-- 4. Array Functions
-- ================
-- Create array columns
ALTER TABLE customers ADD COLUMN tags TEXT[];
ALTER TABLE orders ADD COLUMN related_products INTEGER[];

-- Array operations
SELECT
    customer_name,
    -- Array creation
    ARRAY[1, 2, 3] as numbers,
    ARRAY_AGG(product_id) as all_products,
    -- Array access
    tags[1] as first_tag,
    -- Array functions
    ARRAY_LENGTH(tags, 1) as tag_count,
    ARRAY_POSITION(tags, 'premium') as premium_position,
    -- Array modification
    ARRAY_APPEND(tags, 'new_tag') as updated_tags,
    ARRAY_REMOVE(tags, 'old_tag') as cleaned_tags
FROM customers;

-- 5. JSON Functions
-- ===============
-- Create JSON columns
ALTER TABLE customers ADD COLUMN preferences JSONB;
ALTER TABLE orders ADD COLUMN metadata JSONB;

-- JSON operations
SELECT
    customer_name,
    -- JSON creation
    JSON_BUILD_OBJECT('name', customer_name, 'email', email) as customer_json,
    -- JSON access
    preferences->>'theme' as theme_preference,
    -- JSON modification
    JSONB_SET(preferences, '{notifications}', 'true') as updated_preferences,
    -- JSON aggregation
    JSON_AGG(JSON_BUILD_OBJECT('product', product_name, 'amount', total_amount)) as order_history
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.preferences;

-- 6. Full Text Search
-- =================
-- Create text search columns
ALTER TABLE products ADD COLUMN search_vector TSVECTOR;

-- Text search operations
SELECT
    product_name,
    -- Text search functions
    TO_TSVECTOR('english', product_name) as search_vector,
    TS_RANK(TO_TSVECTOR('english', product_name),
            TO_TSQUERY('english', 'laptop & computer')) as relevance
FROM orders;

-- 7. Advanced Window Functions
-- =========================
SELECT
    customer_name,
    order_date,
    total_amount,
    -- Advanced window functions
    FIRST_VALUE(total_amount) OVER w as first_order,
    LAST_VALUE(total_amount) OVER w as last_order,
    NTH_VALUE(total_amount, 2) OVER w as second_order,
    NTILE(4) OVER (ORDER BY total_amount) as quartile,
    -- Frame specifications
    SUM(total_amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) as three_order_sum
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WINDOW w AS (PARTITION BY customer_id ORDER BY order_date);

-- 8. Advanced Aggregation
-- =====================
SELECT
    customer_type,
    -- Statistical functions
    CORR(total_amount, quantity) as amount_quantity_correlation,
    REGR_SLOPE(total_amount, quantity) as amount_per_quantity,
    -- Advanced aggregates
    STRING_AGG(product_name, ', ' ORDER BY order_date) as product_history,
    ARRAY_AGG(DISTINCT product_id) as unique_products,
    -- Grouping sets
    GROUPING(customer_type) as is_grouped
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY GROUPING SETS ((customer_type), ());

-- 9. Advanced Joins
-- ===============
-- Lateral joins
SELECT
    c.customer_name,
    o.order_date,
    o.total_amount
FROM customers c
CROSS JOIN LATERAL (
    SELECT *
    FROM orders
    WHERE customer_id = c.customer_id
    ORDER BY order_date DESC
    LIMIT 3
) o;

-- Natural joins
SELECT *
FROM customers
NATURAL JOIN orders;

-- 10. Advanced Filtering
-- ====================
-- Using ANY/ALL
SELECT customer_name
FROM customers
WHERE customer_id = ANY(
    SELECT customer_id
    FROM orders
    WHERE total_amount > 1000
);

-- Using IN with subquery
SELECT product_name
FROM orders
WHERE customer_id IN (
    SELECT customer_id
    FROM customers
    WHERE customer_type = 'Premium'
);

-- 11. Advanced Data Types
-- =====================
-- Create custom types
CREATE TYPE address AS (
    street TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT
);

-- Use custom types
ALTER TABLE customers ADD COLUMN shipping_address address;

-- 12. Advanced Constraints
-- ======================
-- Add constraints
ALTER TABLE orders
ADD CONSTRAINT check_amount
CHECK (total_amount >= 0),
ADD CONSTRAINT check_quantity
CHECK (quantity > 0);

-- 13. Advanced Indexing
-- ===================
-- Create indexes
CREATE INDEX idx_customer_name ON customers (customer_name);
CREATE INDEX idx_order_date ON orders (order_date);
CREATE INDEX idx_search ON orders USING GIN (to_tsvector('english', product_name));

-- 14. Advanced Security
-- ===================
-- Create roles
CREATE ROLE analyst;
GRANT SELECT ON customers TO analyst;
GRANT SELECT ON orders TO analyst;

-- Create views
CREATE VIEW customer_orders AS
SELECT c.*, o.order_date, o.total_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

-- 15. Advanced Performance
-- ======================
-- Analyze tables
ANALYZE customers;
ANALYZE orders;

-- Vacuum tables
VACUUM FULL customers;
VACUUM FULL orders;

-- 16. Advanced Backup
-- =================
-- Backup commands
-- pg_dump -U username -d database_name -f backup.sql
-- pg_restore -U username -d database_name backup.sql

-- 17. Advanced Monitoring
-- =====================
-- View table statistics
SELECT
    schemaname,
    tablename,
    n_live_tup,
    n_dead_tup
FROM pg_stat_user_tables;

-- View index statistics
SELECT
    schemaname,
    tablename,
    indexname,
    idx_scan,
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes;



-- =============================================
-- ADDITIONAL POSTGRESQL FUNCTIONS & OPERATIONS
-- =============================================

-- 1. Advanced Table Operations
-- ==========================
-- Create temporary tables
CREATE TEMPORARY TABLE temp_orders AS
SELECT * FROM orders WHERE order_date > CURRENT_DATE - INTERVAL '30 days';

-- Create unlogged tables (faster writes)
CREATE UNLOGGED TABLE fast_orders (LIKE orders);

-- Create foreign tables
CREATE FOREIGN TABLE remote_orders (
    order_id INTEGER,
    customer_id INTEGER,
    order_date TIMESTAMP
) SERVER remote_server;

-- 2. Advanced Partitioning
-- ======================
-- Create partitioned table
CREATE TABLE orders_partitioned (
    order_id INTEGER,
    customer_id INTEGER,
    order_date TIMESTAMP,
    total_amount DECIMAL(10,2)
) PARTITION BY RANGE (order_date);

-- Create partitions
CREATE TABLE orders_2023_q1 PARTITION OF orders_partitioned
    FOR VALUES FROM ('2023-01-01') TO ('2023-04-01');

CREATE TABLE orders_2023_q2 PARTITION OF orders_partitioned
    FOR VALUES FROM ('2023-04-01') TO ('2023-07-01');

-- 3. Advanced Index Types
-- =====================
-- Create different index types
CREATE INDEX idx_btree ON orders USING BTREE (order_date);
CREATE INDEX idx_hash ON orders USING HASH (customer_id);
CREATE INDEX idx_brin ON orders USING BRIN (order_date);
CREATE INDEX idx_gin ON orders USING GIN (to_tsvector('english', product_name));
CREATE INDEX idx_gist ON orders USING GIST (shipping_location);

-- 4. Advanced Materialized Views
-- ===========================
-- Create materialized view
CREATE MATERIALIZED VIEW mv_customer_stats AS
SELECT
    customer_id,
    COUNT(*) as order_count,
    SUM(total_amount) as total_spent,
    AVG(total_amount) as avg_order_value
FROM orders
GROUP BY customer_id
WITH DATA;

-- Refresh materialized view
REFRESH MATERIALIZED VIEW mv_customer_stats;

-- 5. Advanced Triggers
-- ==================
-- Create trigger function
CREATE OR REPLACE FUNCTION update_customer_stats()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        UPDATE customer_stats
        SET order_count = order_count + 1,
            total_spent = total_spent + NEW.total_amount
        WHERE customer_id = NEW.customer_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create trigger
CREATE TRIGGER trg_update_stats
AFTER INSERT ON orders
FOR EACH ROW
EXECUTE FUNCTION update_customer_stats();

-- 6. Advanced Functions
-- ===================
-- Create PL/pgSQL function
CREATE OR REPLACE FUNCTION calculate_discount(
    p_customer_id INTEGER,
    p_order_amount DECIMAL
) RETURNS DECIMAL AS $$
DECLARE
    v_discount DECIMAL;
    v_customer_type TEXT;
BEGIN
    SELECT customer_type INTO v_customer_type
    FROM customers
    WHERE customer_id = p_customer_id;

    CASE v_customer_type
        WHEN 'Premium' THEN v_discount := p_order_amount * 0.15;
        WHEN 'Regular' THEN v_discount := p_order_amount * 0.05;
        ELSE v_discount := 0;
    END CASE;

    RETURN v_discount;
END;
$$ LANGUAGE plpgsql;

-- 7. Advanced Transactions
-- =====================
-- Transaction with savepoints
BEGIN;
    INSERT INTO orders (customer_id, order_date, total_amount)
    VALUES (1, CURRENT_TIMESTAMP, 100.00);

    SAVEPOINT sp1;

    UPDATE customers
    SET total_orders = total_orders + 1
    WHERE customer_id = 1;

    ROLLBACK TO sp1;

    COMMIT;

-- 8. Advanced Locking
-- =================
-- Explicit locking
SELECT * FROM orders
WHERE customer_id = 1
FOR UPDATE;

-- Row-level locking
SELECT * FROM orders
WHERE order_date > CURRENT_DATE - INTERVAL '7 days'
FOR UPDATE SKIP LOCKED;

-- 9. Advanced Replication
-- =====================
-- Create replication slot
SELECT * FROM pg_create_physical_replication_slot('replication_slot');

-- Create publication
CREATE PUBLICATION pub_orders FOR TABLE orders;

-- Create subscription
CREATE SUBSCRIPTION sub_orders
CONNECTION 'host=primary dbname=orders'
PUBLICATION pub_orders;

-- 10. Advanced Backup and Recovery
-- =============================
-- Create base backup
-- pg_basebackup -D /backup -Ft -z -P

-- Point-in-time recovery
-- recovery_target_time = '2023-01-01 12:00:00'
-- recovery_target_inclusive = true

-- 11. Advanced Monitoring
-- =====================
-- Query performance monitoring
SELECT
    query,
    calls,
    total_time,
    mean_time,
    rows
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;

-- Table bloat monitoring
SELECT
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(relid)) as total_size,
    pg_size_pretty(pg_relation_size(relid)) as table_size,
    pg_size_pretty(pg_total_relation_size(relid) - pg_relation_size(relid)) as index_size
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;

-- 12. Advanced Security
-- ===================
-- Row-level security
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

CREATE POLICY orders_policy ON orders
    USING (customer_id = current_user_id());

-- Column-level security
GRANT SELECT (customer_id, order_date) ON orders TO analyst;
GRANT SELECT (total_amount) ON orders TO manager;

-- 13. Advanced Data Types
-- =====================
-- Create enum type
CREATE TYPE order_status AS ENUM ('pending', 'processing', 'shipped', 'delivered');

-- Create composite type
CREATE TYPE address AS (
    street TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT
);

-- Create range type
CREATE TYPE price_range AS RANGE (subtype = numeric);

-- 14. Advanced Full Text Search
-- ===========================
-- Create text search configuration
CREATE TEXT SEARCH CONFIGURATION english_improved (COPY = english);

-- Add custom dictionary
ALTER TEXT SEARCH CONFIGURATION english_improved
    ALTER MAPPING FOR word WITH english_stem, english_ispell;

-- 15. Advanced JSON Operations
-- =========================
-- JSON path queries
SELECT
    customer_name,
    preferences->'settings'->>'theme' as theme,
    preferences->'notifications'->>'email' as email_notifications
FROM customers;

-- JSON aggregation
SELECT
    customer_id,
    jsonb_agg(
        jsonb_build_object(
            'order_id', order_id,
            'date', order_date,
            'amount', total_amount
        )
    ) as order_history
FROM orders
GROUP BY customer_id;

-- 16. Advanced Array Operations
-- ===========================
-- Array slicing
SELECT
    customer_name,
    tags[1:3] as first_three_tags,
    tags[array_length(tags, 1)-2:] as last_two_tags
FROM customers;

-- Array set operations
SELECT
    customer_name,
    array_union(tags, ARRAY['new_tag']) as updated_tags,
    array_intersect(tags, ARRAY['premium', 'vip']) as common_tags
FROM customers;

-- 17. Advanced Window Functions
-- ===========================
-- Named window definitions
SELECT
    customer_name,
    order_date,
    total_amount,
    SUM(total_amount) OVER w as running_total,
    AVG(total_amount) OVER w as running_avg,
    COUNT(*) OVER w as order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WINDOW w AS (
    PARTITION BY customer_id
    ORDER BY order_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
);

-- 18. Advanced Aggregation
-- ======================
-- Filtered aggregates
SELECT
    customer_type,
    COUNT(*) FILTER (WHERE total_amount > 1000) as large_orders,
    AVG(total_amount) FILTER (WHERE order_date > CURRENT_DATE - INTERVAL '30 days') as recent_avg
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY customer_type;

-- 19. Advanced Joins
-- ================
-- LATERAL joins with subqueries
SELECT
    c.customer_name,
    o.order_date,
    o.total_amount
FROM customers c
CROSS JOIN LATERAL (
    SELECT *
    FROM orders
    WHERE customer_id = c.customer_id
    ORDER BY order_date DESC
    LIMIT 3
) o;

-- 20. Advanced Error Handling
-- =========================
-- Error handling in functions
CREATE OR REPLACE FUNCTION safe_division(numerator DECIMAL, denominator DECIMAL)
RETURNS DECIMAL AS $$
BEGIN
    IF denominator = 0 THEN
        RAISE EXCEPTION 'Division by zero';
    END IF;
    RETURN numerator / denominator;
EXCEPTION
    WHEN division_by_zero THEN
        RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- =============================================
-- ADDITIONAL STANDARD POSTGRESQL FUNCTIONS
-- =============================================

-- 1. String Functions
-- =================
SELECT
    -- Basic string functions
    LOWER(customer_name) as lower_name,
    UPPER(customer_name) as upper_name,
    INITCAP(customer_name) as title_case,
    -- String padding
    LPAD(customer_name, 20, '*') as left_padded,
    RPAD(customer_name, 20, '*') as right_padded,
    -- String extraction
    SUBSTRING(customer_name FROM 1 FOR 3) as first_three,
    LEFT(customer_name, 3) as left_three,
    RIGHT(customer_name, 3) as right_three,
    -- String replacement
    REPLACE(customer_name, ' ', '_') as underscore_name,
    TRANSLATE(customer_name, 'aeiou', '*****') as vowels_replaced,
    -- String position
    POSITION(' ' IN customer_name) as space_pos,
    STRPOS(customer_name, ' ') as space_pos2,
    -- String length
    LENGTH(customer_name) as name_length,
    OCTET_LENGTH(customer_name) as byte_length,
    -- String concatenation
    CONCAT(customer_name, ' (', email, ')') as name_email,
    customer_name || ' (' || email || ')' as name_email2
FROM customers;

-- 2. Date/Time Functions
-- ====================
SELECT
    -- Current date/time
    CURRENT_DATE as today,
    CURRENT_TIME as current_time,
    CURRENT_TIMESTAMP as now,
    LOCALTIME as local_time,
    LOCALTIMESTAMP as local_timestamp,
    -- Date extraction
    EXTRACT(YEAR FROM order_date) as order_year,
    EXTRACT(MONTH FROM order_date) as order_month,
    EXTRACT(DAY FROM order_date) as order_day,
    EXTRACT(DOW FROM order_date) as day_of_week,
    EXTRACT(DOY FROM order_date) as day_of_year,
    -- Date formatting
    TO_CHAR(order_date, 'YYYY-MM-DD') as formatted_date,
    TO_CHAR(order_date, 'Day, Month DD, YYYY') as long_date,
    TO_CHAR(order_date, 'HH24:MI:SS') as time_only,
    -- Date arithmetic
    order_date + INTERVAL '1 day' as tomorrow,
    order_date - INTERVAL '1 month' as last_month,
    order_date + (7 || ' days')::INTERVAL as next_week,
    -- Date truncation
    DATE_TRUNC('month', order_date) as month_start,
    DATE_TRUNC('year', order_date) as year_start,
    DATE_TRUNC('hour', order_date) as hour_start,
    -- Date validation
    order_date IS NOT NULL as is_valid_date,
    order_date > CURRENT_DATE as is_future_date
FROM orders;

-- 3. Numeric Functions
-- ==================
SELECT
    -- Basic math
    ABS(total_amount) as absolute_value,
    CEIL(total_amount) as ceiling,
    FLOOR(total_amount) as floor,
    ROUND(total_amount, 2) as rounded,
    TRUNC(total_amount, 2) as truncated,
    -- Mathematical functions
    SQRT(total_amount) as square_root,
    POWER(total_amount, 2) as squared,
    LOG(10, total_amount) as logarithm,
    LN(total_amount) as natural_log,
    EXP(total_amount) as exponential,
    -- Trigonometric functions
    SIN(total_amount) as sine,
    COS(total_amount) as cosine,
    TAN(total_amount) as tangent,
    -- Random numbers
    RANDOM() as random_0_to_1,
    (RANDOM() * 100)::INTEGER as random_0_to_100,
    -- Sign and comparison
    SIGN(total_amount) as sign,
    GREATEST(total_amount, 100) as max_value,
    LEAST(total_amount, 1000) as min_value
FROM orders;

-- 4. Aggregate Functions
-- ====================
SELECT
    -- Basic aggregates
    COUNT(*) as total_orders,
    COUNT(DISTINCT customer_id) as unique_customers,
    SUM(total_amount) as total_revenue,
    AVG(total_amount) as average_order,
    MIN(total_amount) as min_order,
    MAX(total_amount) as max_order,
    -- Statistical aggregates
    STDDEV(total_amount) as standard_deviation,
    VARIANCE(total_amount) as variance,
    -- Advanced aggregates
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY total_amount) as median,
    PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY total_amount) as median_disc,
    MODE() WITHIN GROUP (ORDER BY total_amount) as mode,
    -- String aggregates
    STRING_AGG(product_name, ', ' ORDER BY order_date) as product_list,
    ARRAY_AGG(DISTINCT product_id) as product_ids
FROM orders;

-- 5. Window Functions
-- =================
SELECT
    customer_id,
    order_date,
    total_amount,
    -- Ranking functions
    ROW_NUMBER() OVER (ORDER BY total_amount DESC) as row_num,
    RANK() OVER (ORDER BY total_amount DESC) as rank,
    DENSE_RANK() OVER (ORDER BY total_amount DESC) as dense_rank,
    -- Value functions
    FIRST_VALUE(total_amount) OVER w as first_amount,
    LAST_VALUE(total_amount) OVER w as last_amount,
    NTH_VALUE(total_amount, 2) OVER w as second_amount,
    -- Aggregate window functions
    SUM(total_amount) OVER w as running_total,
    AVG(total_amount) OVER w as running_avg,
    COUNT(*) OVER w as running_count,
    -- Frame functions
    LAG(total_amount) OVER w as prev_amount,
    LEAD(total_amount) OVER w as next_amount,
    -- Percentile functions
    PERCENT_RANK() OVER w as percent_rank,
    CUME_DIST() OVER w as cumulative_dist
FROM orders
WINDOW w AS (PARTITION BY customer_id ORDER BY order_date);

-- 6. Conditional Functions
-- =====================
SELECT
    -- CASE expressions
    CASE
        WHEN total_amount > 1000 THEN 'High'
        WHEN total_amount > 500 THEN 'Medium'
        ELSE 'Low'
    END as order_size,
    -- COALESCE and NULLIF
    COALESCE(customer_name, 'Unknown') as safe_name,
    NULLIF(total_amount, 0) as non_zero_amount,
    -- GREATEST and LEAST
    GREATEST(total_amount, 100) as min_amount,
    LEAST(total_amount, 1000) as max_amount,
    -- Conditional aggregates
    COUNT(*) FILTER (WHERE total_amount > 1000) as large_orders,
    SUM(total_amount) FILTER (WHERE order_date > CURRENT_DATE - INTERVAL '30 days') as recent_revenue
FROM orders;

-- 7. Array Functions
-- ================
SELECT
    -- Array creation
    ARRAY[1, 2, 3] as numbers,
    ARRAY_AGG(product_id) as all_products,
    -- Array access
    tags[1] as first_tag,
    tags[array_length(tags, 1)] as last_tag,
    -- Array functions
    ARRAY_LENGTH(tags, 1) as tag_count,
    ARRAY_POSITION(tags, 'premium') as premium_pos,
    -- Array modification
    ARRAY_APPEND(tags, 'new_tag') as updated_tags,
    ARRAY_REMOVE(tags, 'old_tag') as cleaned_tags,
    -- Array operations
    ARRAY_CAT(tags, ARRAY['additional']) as combined_tags,
    ARRAY_PREPEND('first', tags) as prepended_tags,
    -- Array comparison
    tags @> ARRAY['premium'] as has_premium,
    tags && ARRAY['premium', 'vip'] as has_any
FROM customers;

-- 8. JSON Functions
-- ===============
SELECT
    -- JSON creation
    JSON_BUILD_OBJECT(
        'name', customer_name,
        'email', email,
        'orders', JSON_AGG(
            JSON_BUILD_OBJECT(
                'id', order_id,
                'date', order_date,
                'amount', total_amount
            )
        )
    ) as customer_json,
    -- JSON access
    preferences->>'theme' as theme,
    preferences->'settings'->>'notifications' as notifications,
    -- JSON modification
    JSONB_SET(preferences, '{theme}', '"dark"') as updated_preferences,
    JSONB_INSERT(preferences, '{new_setting}', '"value"') as inserted_preferences,
    -- JSON aggregation
    JSON_AGG(
        JSON_BUILD_OBJECT(
            'product', product_name,
            'quantity', quantity
        )
    ) as order_items
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.email, c.preferences;

-- 9. Network Address Functions
-- =========================
SELECT
    -- IP address functions
    INET_ATON('192.168.1.1') as ip_to_int,
    INET_NTOA(3232235777) as int_to_ip,
    -- Network functions
    NETMASK(ip_address) as netmask,
    HOST(ip_address) as host,
    NETWORK(ip_address) as network,
    -- CIDR functions
    SET_MASKLEN(ip_address, 24) as set_mask,
    MASKLEN(ip_address) as mask_length
FROM network_logs;

-- 10. Geometric Functions
-- =====================
SELECT
    -- Point functions
    POINT(1, 2) as point,
    POINT_DISTANCE(POINT(1, 2), POINT(4, 6)) as distance,
    -- Line functions
    LINE(POINT(1, 2), POINT(4, 6)) as line,
    -- Circle functions
    CIRCLE(POINT(1, 2), 5) as circle,
    -- Box functions
    BOX(POINT(1, 2), POINT(4, 6)) as box,
    -- Polygon functions
    POLYGON(POINT(1, 2), POINT(4, 6), POINT(7, 8)) as polygon
FROM geometric_data;

-- 11. Text Search Functions
-- =======================
SELECT
    -- Text search vectors
    TO_TSVECTOR('english', product_name) as search_vector,
    TO_TSQUERY('english', 'laptop & computer') as search_query,
    -- Text search ranking
    TS_RANK(
        TO_TSVECTOR('english', product_name),
        TO_TSQUERY('english', 'laptop & computer')
    ) as relevance,
    -- Text search matching
    product_name @@ TO_TSQUERY('english', 'laptop & computer') as matches,
    -- Text search highlighting
    TS_HEADLINE(
        'english',
        product_description,
        TO_TSQUERY('english', 'laptop & computer'),
        'StartSel=<b>, StopSel=</b>'
    ) as highlighted_text
FROM products;

-- 12. XML Functions
-- ===============
SELECT
    -- XML creation
    XMLELEMENT(
        NAME "customer",
        XMLATTRIBUTES(customer_id as "id"),
        XMLELEMENT(NAME "name", customer_name),
        XMLELEMENT(NAME "email", email)
    ) as customer_xml,
    -- XML parsing
    XPATH('//name/text()', customer_xml) as names,
    -- XML validation
    XMLISVALID(customer_xml) as is_valid,
    -- XML transformation
    XSLTRANSFORM(customer_xml, xslt_document) as transformed_xml
FROM customers;

-- 13. Sequence Functions
-- ====================
SELECT
    -- Sequence functions
    NEXTVAL('order_id_seq') as next_id,
    CURRVAL('order_id_seq') as current_id,
    SETVAL('order_id_seq', 1000) as set_value,
    -- Identity functions
    IDENTITY_CURRENT('orders') as current_identity,
    -- Sequence information
    pg_sequence_last_value('order_id_seq') as last_value
FROM orders;

-- 14. System Information Functions
-- =============================
SELECT
    -- Version information
    VERSION() as postgres_version,
    -- Session information
    CURRENT_USER as current_user,
    SESSION_USER as session_user,
    CURRENT_DATABASE() as current_database,
    CURRENT_SCHEMA() as current_schema,
    -- Connection information
    INET_CLIENT_ADDR() as client_address,
    INET_CLIENT_PORT() as client_port,
    -- Transaction information
    TXID_CURRENT() as current_transaction,
    -- System time
    CLOCK_TIMESTAMP() as system_time,
    STATEMENT_TIMESTAMP() as statement_time,
    TRANSACTION_TIMESTAMP() as transaction_time
FROM pg_stat_activity
WHERE pid = pg_backend_pid();


-- Create sample tables
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    registration_date DATE,
    customer_type VARCHAR(20)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    order_date TIMESTAMP,
    total_amount DECIMAL(10,2),
    product_name VARCHAR(100)
);

-- Insert sample data
INSERT INTO customers (customer_name, email, registration_date, customer_type)
VALUES
    ('John Doe', 'john@example.com', '2023-01-01', 'Premium'),
    ('Jane Smith', 'jane@example.com', '2023-02-15', 'Regular'),
    ('Bob Johnson', 'bob@example.com', '2023-03-10', 'Premium');

INSERT INTO orders (customer_id, order_date, total_amount, product_name)
VALUES
    (1, '2023-04-01 10:00:00', 1500.00, 'Laptop'),
    (1, '2023-04-15 14:30:00', 500.00, 'Mouse'),
    (2, '2023-05-01 09:15:00', 2000.00, 'Desktop'),
    (3, '2023-05-15 11:45:00', 750.00, 'Keyboard');
