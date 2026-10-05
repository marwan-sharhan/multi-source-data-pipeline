import sqlite3


database_path = "data/processed/ecommerce.db"

connection = sqlite3.connect(database_path)

cursor = connection.cursor()

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
""")

tables = cursor.fetchall()

print("=== SQLITE TABLES ===")

for table in tables:
    table_name = table[0]

    cursor.execute(
        f"SELECT COUNT(*) FROM {table_name}"
    )

    count = cursor.fetchone()[0]

    print(f"{table_name}: {count}")

connection.close()