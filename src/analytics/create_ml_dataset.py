import sqlite3
import pandas as pd


database_path = "data/processed/ecommerce.db"
output_path = "data/processed/ml_customers.csv"


connection = sqlite3.connect(database_path)

query = """
SELECT
    o.customer_id,

    COUNT(DISTINCT o.invoice_no) AS number_of_orders,

    SUM(oi.quantity) AS total_items,

    ROUND(
        SUM(oi.quantity * oi.unit_price),
        2
    ) AS total_spent,

    ROUND(
        SUM(oi.quantity * oi.unit_price)
        / COUNT(DISTINCT o.invoice_no),
        2
    ) AS average_order_value

FROM orders o
JOIN order_items oi
    ON o.invoice_no = oi.invoice_no
WHERE o.customer_id IS NOT NULL
  AND o.transaction_type = 'SALE'
GROUP BY o.customer_id;
"""

df = pd.read_sql(query, connection)

connection.close()

df.to_csv(output_path, index=False)

print("ML dataset created successfully")
print("Customers:", len(df))
print("Columns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())