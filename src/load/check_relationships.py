import sqlite3
import pandas as pd


csv_path = "./data/processed/online_retail_processed.csv"
database_path = "./data/processed/ecommerce.db"


df = pd.read_csv(csv_path)

connection = sqlite3.connect(database_path)


# فحص الفواتير
orders = pd.read_sql(
    "SELECT invoice_no FROM orders",
    connection
)

# فحص المنتجات
products = pd.read_sql(
    "SELECT stock_code FROM products",
    connection
)


# الفواتير الموجودة في CSV وغير موجودة في orders
missing_invoices = (
    df.loc[
        ~df["InvoiceNo"].astype(str).isin(
            orders["invoice_no"].astype(str)
        ),
        "InvoiceNo"
    ]
    .nunique()
)


# المنتجات الموجودة في CSV وغير موجودة في products
missing_products = (
    df.loc[
        ~df["StockCode"].astype(str).isin(
            products["stock_code"].astype(str)
        ),
        "StockCode"
    ]
    .nunique()
)


print("=== RELATIONSHIP CHECK ===")

print("Missing invoices:", missing_invoices)
print("Missing products:", missing_products)


connection.close()