import sqlite3
import pandas as pd


csv_path = "./data/raw/mongodb/reviews.json"
database_path = "./data/processed/ecommerce.db"


df = pd.read_json(csv_path)

connection = sqlite3.connect(database_path)

df.to_sql(
    "reviews",
    connection,
    if_exists="append",
    index=False
)

connection.commit()
connection.close()

print("Reviews loaded successfully")
print("Reviews loaded:", len(df))