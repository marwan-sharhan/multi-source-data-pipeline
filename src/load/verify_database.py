import sqlite3


database_path = "./data/processed/ecommerce.db"


connection = sqlite3.connect(database_path)

cursor = connection.cursor()


tables = [
    "customers",
    "products",
    "orders",
    "order_items"
]


print("=== DATABASE ROW COUNTS ===")

for table in tables:

    cursor.execute(
        f"SELECT COUNT(*) FROM {table}"
    )

    count = cursor.fetchone()[0]

    print(f"{table}: {count}")


connection.close()