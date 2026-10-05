import sqlite3
import pandas as pd


csv_path = "./data/processed/online_retail_processed.csv"
database_path = "./data/processed/ecommerce.db"


# قراءة البيانات المعالجة
df = pd.read_csv(csv_path)


# استخراج CustomerID
customers = (
    df["CustomerID"]
    .dropna()
    .drop_duplicates()
)


# تحويل CustomerID إلى integer
customers = customers.astype(int)


# الاتصال بقاعدة SQLite
connection = sqlite3.connect(database_path)


# تحويل البيانات إلى DataFrame مناسب لجدول customers
customers_df = pd.DataFrame({
    "customer_id": customers
})


# تحميل البيانات
customers_df.to_sql(
    "customers",
    connection,
    if_exists="append",
    index=False
)


connection.commit()
connection.close()


print("Customers loaded successfully")
print("Customers loaded:", len(customers_df))