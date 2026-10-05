import sqlite3


def test_database_exists():
    connection = sqlite3.connect("data/processed/ecommerce.db")

    cursor = connection.cursor()
    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table';
    """)

    tables = [row[0] for row in cursor.fetchall()]
    connection.close()

    assert "orders" in tables
    assert "order_items" in tables
    assert "products" in tables


def test_data_integrity():
    connection = sqlite3.connect("data/processed/ecommerce.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM order_items oi
        LEFT JOIN orders o
        ON oi.invoice_no = o.invoice_no
        WHERE o.invoice_no IS NULL;
    """)

    invalid_items = cursor.fetchone()[0]
    connection.close()

    assert invalid_items == 0