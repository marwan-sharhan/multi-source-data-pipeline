import sqlite3


database_path = "./data/processed/ecommerce.db"
schema_path = "./sql/schema.sql"


connection = sqlite3.connect(database_path)

print("SQLite database connected successfully")


with open(schema_path, "r", encoding="utf-8") as file:
    schema = file.read()


connection.executescript(schema)

connection.commit()

print("Database schema created successfully")


connection.close()

print("SQLite connection closed")