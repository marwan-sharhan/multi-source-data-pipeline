import sqlite3
import pandas as pd

database_path = "data/processed/ecommerce.db"
output_path = "reports/quality_report.csv"

connection = sqlite3.connect(database_path)

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

results = []

for rule, query in checks.items():
    result = pd.read_sql_query(query, connection).iloc[0, 0]

    results.append({
        "rule": rule,
        "invalid_rows": result,
        "status": "PASS" if result == 0 else "FAIL"
    })

connection.close()

report = pd.DataFrame(results)
report.to_csv(output_path, index=False)

print("Quality report created successfully")
print(report)