import pandas as pd


file_path = "./data/processed/online_retail_processed.csv"

df = pd.read_csv(file_path)


print("=== UNIQUE VALUES ===")

print("Unique invoices:", df["InvoiceNo"].nunique())
print("Unique products:", df["StockCode"].nunique())
print("Unique customers:", df["CustomerID"].nunique())


print("\n=== ITEMS PER INVOICE ===")

items_per_invoice = (
    df.groupby("InvoiceNo")["StockCode"]
    .nunique()
)

print(items_per_invoice.describe())


print("\n=== CUSTOMERS PER INVOICE ===")

customers_per_invoice = (
    df.groupby("InvoiceNo")["CustomerID"]
    .nunique()
)

print(customers_per_invoice.describe())