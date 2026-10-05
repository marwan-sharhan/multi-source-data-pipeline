import sqlite3

connection = sqlite3.connect("data/processed/ecommerce.db")

query = """
SELECT
    o.customer_id,
    COUNT(DISTINCT o.invoice_no) AS number_of_orders,
    SUM(oi.quantity) AS total_items,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_spent,
    ROUND(
        SUM(oi.quantity * oi.unit_price)
        / COUNT(DISTINCT o.invoice_no),
        2
    ) AS average_order_value
FROM orders o
JOIN order_items oi
    ON o.invoice_no = oi.invoice_no
WHERE o.customer_id IS NOT NULL
GROUP BY o.customer_id;
"""

cursor = connection.cursor()
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

connection.close()