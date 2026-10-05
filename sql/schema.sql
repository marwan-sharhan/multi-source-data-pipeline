-- =========================================
-- CUSTOMERS
-- =========================================

CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY
);


-- =========================================
-- PRODUCTS
-- =========================================

CREATE TABLE IF NOT EXISTS products (
    stock_code TEXT PRIMARY KEY,
    description TEXT
);


-- =========================================
-- ORDERS
-- =========================================

CREATE TABLE IF NOT EXISTS orders (
    invoice_no TEXT PRIMARY KEY,
    invoice_date TEXT,
    customer_id INTEGER,
    country TEXT,
    transaction_type TEXT,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);


-- =========================================
-- ORDER ITEMS
-- =========================================

CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_no TEXT NOT NULL,
    stock_code TEXT NOT NULL,
    quantity INTEGER,
    unit_price REAL,

    FOREIGN KEY (invoice_no)
        REFERENCES orders(invoice_no),

    FOREIGN KEY (stock_code)
        REFERENCES products(stock_code)
);

CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    customer_id INTEGER,
    rating INTEGER,
    review TEXT,
    source TEXT
);
CREATE TABLE IF NOT EXISTS postgres_products (
    stock_code TEXT PRIMARY KEY,
    description TEXT,
    category TEXT,
    price REAL,
    source TEXT
);

CREATE TABLE IF NOT EXISTS api_products (
    id INTEGER PRIMARY KEY,
    title TEXT,
    category TEXT,
    price REAL,
    source TEXT
);

CREATE TABLE IF NOT EXISTS web_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price REAL,
    currency TEXT,
    source TEXT
);