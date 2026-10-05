import sqlite3


database_path = "./data/processed/ecommerce.db"


connection = sqlite3.connect(database_path)

cursor = connection.cursor()


# تفعيل فحص العلاقات
cursor.execute("PRAGMA foreign_keys = ON")


print("=== FOREIGN KEY CHECK ===")


# order_items التي تشير إلى Invoice غير موجودة
cursor.execute("""
    SELECT COUNT(*)
    FROM order_items oi
    LEFT JOIN orders o
        ON oi.invoice_no = o.invoice_no
    WHERE o.invoice_no IS NULL
""")

missing_orders = cursor.fetchone()[0]


# order_items التي تشير إلى Product غير موجود
cursor.execute("""
    SELECT COUNT(*)
    FROM order_items oi
    LEFT JOIN products p
        ON oi.stock_code = p.stock_code
    WHERE p.stock_code IS NULL
""")

missing_products = cursor.fetchone()[0]


# Orders التي تشير إلى Customer غير موجود
cursor.execute("""
    SELECT COUNT(*)
    FROM orders o
    LEFT JOIN customers c
        ON o.customer_id = c.customer_id
    WHERE o.customer_id IS NOT NULL
      AND c.customer_id IS NULL
""")

missing_customers = cursor.fetchone()[0]


print("Order items without order:", missing_orders)
print("Order items without product:", missing_products)
print("Orders without customer:", missing_customers)


connection.close()