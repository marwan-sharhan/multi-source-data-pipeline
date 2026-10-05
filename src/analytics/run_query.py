import sqlite3

database_path = "./data/processed/ecommerce.db"
sql_path = "./sql/analytics.sql"

connection = sqlite3.connect(database_path)

with open(sql_path, "r", encoding="utf-8") as file:
    query = file.read()

cursor = connection.cursor()

cursor.execute(query)

results = cursor.fetchall()

print("=== TRANSACTION SUMMARY ===")

for row in results:
    print(row)

connection.close()