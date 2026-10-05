import sqlite3
import pandas as pd


csv_path = "./data/processed/online_retail_processed.csv"
database_path = "./data/processed/ecommerce.db"


# قراءة البيانات المعالجة
df = pd.read_csv(csv_path)


# الاحتفاظ بالمنتجات التي لديها StockCode
products = df[
    ["StockCode", "Description"]
].copy()

products = products.dropna(
    subset=["StockCode"]
)


# إزالة المسافات الزائدة من StockCode
products["StockCode"] = (
    products["StockCode"]
    .astype(str)
    .str.strip()
)


# اختيار أول وصف غير فارغ لكل منتج
products["Description"] = (
    products["Description"]
    .fillna("")
    .astype(str)
    .str.strip()
)

products.loc[
    products["Description"] == "",
    "Description"
] = None


products = (
    products
    .drop_duplicates(
        subset=["StockCode"],
        keep="first"
    )
)


# إعادة تسمية الأعمدة لتطابق SQLite
products = products.rename(
    columns={
        "StockCode": "stock_code",
        "Description": "description"
    }
)


# الاتصال بقاعدة البيانات
connection = sqlite3.connect(database_path)


# تحميل المنتجات
products.to_sql(
    "products",
    connection,
    if_exists="append",
    index=False
)


connection.commit()
connection.close()


print("Products loaded successfully")
print("Products loaded:", len(products))