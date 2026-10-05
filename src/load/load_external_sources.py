import sqlite3
import pandas as pd


database_path = "data/processed/ecommerce.db"

connection = sqlite3.connect(database_path)


# PostgreSQL
postgres = pd.read_csv(
    "data/raw/postgres/products.csv"
)

postgres.to_sql(
    "postgres_products",
    connection,
    if_exists="append",
    index=False
)


# API
api = pd.read_json(
    "data/raw/api/products.json"
)

api = pd.DataFrame(api["products"].tolist())

api = api[["id", "title", "category", "price"]]
api["source"] = "api"

api.to_sql(
    "api_products",
    connection,
    if_exists="append",
    index=False
)


# Web
web = pd.read_json(
    "data/raw/web/books.json"
)

web["currency"] = "GBP"
web["source"] = "web"

web.to_sql(
    "web_books",
    connection,
    if_exists="append",
    index=False
)


connection.commit()
connection.close()


print("External sources loaded successfully")
print("PostgreSQL:", len(postgres))
print("API:", len(api))
print("Web:", len(web))