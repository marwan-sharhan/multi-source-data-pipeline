import sqlite3


database_path = "./data/processed/ecommerce.db"


connection = sqlite3.connect(database_path)

cursor = connection.cursor()


cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name
""")


tables = cursor.fetchall()


print("=== DATABASE TABLES ===")

for table in tables:
    print(table[0])


connection.close()