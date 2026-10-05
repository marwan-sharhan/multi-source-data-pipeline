import sqlite3


database_path = "data/processed/ecommerce.db"

connection = sqlite3.connect(database_path)

cursor = connection.cursor()


checks = {

    "orders_without_items": """
        SELECT COUNT(*)
        FROM orders o
        LEFT JOIN order_items oi
        ON o.invoice_no = oi.invoice_no
        WHERE oi.invoice_no IS NULL;
    """,

    "order_items_without_order": """
        SELECT COUNT(*)
        FROM order_items oi
        LEFT JOIN orders o
        ON oi.invoice_no = o.invoice_no
        WHERE o.invoice_no IS NULL;
    """,

    "order_items_without_product": """
        SELECT COUNT(*)
        FROM order_items oi
        LEFT JOIN products p
        ON oi.stock_code = p.stock_code
        WHERE p.stock_code IS NULL;
    """,

    "invalid_ratings": """
        SELECT COUNT(*)
        FROM reviews
        WHERE rating < 1 OR rating > 5;
    """
}


print("=== FINAL VALIDATION ===")

for rule, query in checks.items():

    cursor.execute(query)

    result = cursor.fetchone()[0]

    status = "PASS" if result == 0 else "FAIL"

    print(f"{rule}: {result} -> {status}")


connection.close()