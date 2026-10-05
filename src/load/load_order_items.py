import sqlite3
import pandas as pd


csv_path = "./data/processed/online_retail_processed.csv"
database_path = "./data/processed/ecommerce.db"


# قراءة البيانات المعالجة
df = pd.read_csv(csv_path)


# اختيار الأعمدة الخاصة بعناصر الطلب
order_items = df[
    [
        "InvoiceNo",
        "StockCode",
        "Quantity",
        "UnitPrice"
    ]
].copy()


# إعادة تسمية الأعمدة لتطابق SQLite
order_items = order_items.rename(
    columns={
        "InvoiceNo": "invoice_no",
        "StockCode": "stock_code",
        "Quantity": "quantity",
        "UnitPrice": "unit_price"
    }
)


# الاتصال بقاعدة البيانات
connection = sqlite3.connect(database_path)


# تحميل البيانات
order_items.to_sql(
    "order_items",
    connection,
    if_exists="append",
    index=False
)


connection.commit()
connection.close()


print("Order items loaded successfully")
print("Order items loaded:", len(order_items))