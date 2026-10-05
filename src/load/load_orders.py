import sqlite3
import pandas as pd


csv_path = "./data/processed/online_retail_processed.csv"
database_path = "./data/processed/ecommerce.db"


# قراءة البيانات المعالجة
df = pd.read_csv(csv_path)


# تحويل التاريخ
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    errors="coerce"
)


# إنشاء جدول orders من البيانات
orders = (
    df[
        [
            "InvoiceNo",
            "InvoiceDate",
            "CustomerID",
            "Country",
            "TransactionType"
        ]
    ]
    .drop_duplicates(subset=["InvoiceNo"])
    .copy()
)


# تحويل CustomerID المفقود إلى None
orders["CustomerID"] = orders["CustomerID"].where(
    orders["CustomerID"].notna(),
    None
)


# تحويل التاريخ إلى نص مناسب لـ SQLite
orders["InvoiceDate"] = orders["InvoiceDate"].dt.strftime(
    "%Y-%m-%d %H:%M:%S"
)


# إعادة تسمية الأعمدة
orders = orders.rename(
    columns={
        "InvoiceNo": "invoice_no",
        "InvoiceDate": "invoice_date",
        "CustomerID": "customer_id",
        "Country": "country",
        "TransactionType": "transaction_type"
    }
)


# الاتصال بقاعدة SQLite
connection = sqlite3.connect(database_path)


# تحميل الطلبات
orders.to_sql(
    "orders",
    connection,
    if_exists="append",
    index=False
)


connection.commit()
connection.close()


print("Orders loaded successfully")
print("Orders loaded:", len(orders))