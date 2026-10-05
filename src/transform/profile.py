import pandas as pd

def profile_data(df):
    print("==== DATA SHAPE ====")
    print(df.shape)


    print("\n==== COLUMNS ====")
    print(df.columns.tolist())


    print("\n==== DATA TYPES ====")
    print(df.dtypes)


    print("\n==== MISSING VALUES ====")
    print(df.isnull().sum())


    print("\n==== DUPLICATES ====")
    print(df.duplicated().sum())


    print("\n==== INVALID QUANTITY ====")
    print((df["Quantity"]<= 0).sum())


    print("\n==== INVALID UNIT PRICE ====")
    print((df["UnitPrice"]<= 0).sum())

    print("\n=== NEGATIVE QUANTITY ===")
    print((df["Quantity"] < 0).sum())

    print("\n=== ZERO QUANTITY ===")
    print((df["Quantity"] == 0).sum())

    print("\n=== ZERO UNIT PRICE ===")
    print((df["UnitPrice"] == 0).sum())

    print("\n=== NEGATIVE UNIT PRICE ===")
    print((df["UnitPrice"] < 0).sum())

    print("\n=== NEGATIVE QUANTITY INVOICE PREFIX ===")

    negative_quantity = df[df["Quantity"] < 0]

    print(
        negative_quantity["InvoiceNo"]
        .astype(str)
        .str[0]
        .value_counts()
    )

    print("\n=== NEGATIVE QUANTITY SAMPLE ===")

    print(
        negative_quantity[
            ["InvoiceNo", "StockCode", "Description",
            "Quantity", "InvoiceDate", "UnitPrice", "CustomerID"]
        ].head(10)
    )

    print("\n=== NEGATIVE QUANTITY WITHOUT C ===")

    negative_without_c = df[
        (df["Quantity"] < 0) &
        (~df["InvoiceNo"].astype(str).str.startswith("C"))
    ]

    print("Count:", len(negative_without_c))

    print(
        negative_without_c[
            ["InvoiceNo", "StockCode", "Description",
            "Quantity", "InvoiceDate", "UnitPrice", "CustomerID"]
        ].head(20)
    )
    print("\n=== NEGATIVE QUANTITY + ZERO PRICE ===")

    condition = (
        (df["Quantity"] < 0) &
        (df["UnitPrice"] == 0)
    )

    print("Count:", condition.sum())


    print("\n=== NEGATIVE QUANTITY + MISSING DESCRIPTION ===")

    condition = (
        (df["Quantity"] < 0) &
        (df["Description"].isna())
    )

    print("Count:", condition.sum())


    print("\n=== NEGATIVE QUANTITY + MISSING CUSTOMER ===")

    condition = (
        (df["Quantity"] < 0) &
        (df["CustomerID"].isna())
    )

    print("Count:", condition.sum())


    print("\n=== NEGATIVE QUANTITY + NO C + ZERO PRICE ===")

    condition = (
        (df["Quantity"] < 0) &
        (~df["InvoiceNo"].astype(str).str.startswith("C")) &
        (df["UnitPrice"] == 0)
    )

    print("Count:", condition.sum())


    print("\n=== ZERO PRICE WITHOUT NEGATIVE QUANTITY ===")

    condition = (
        (df["UnitPrice"] == 0) &
        (df["Quantity"] >= 0)
    )

    print("Count:", condition.sum())

    print(
        df.loc[
            condition,
            ["InvoiceNo", "StockCode", "Description",
            "Quantity", "InvoiceDate", "UnitPrice", "CustomerID"]
        ].head(20)
    )


    print("\n=== NEGATIVE UNIT PRICE ROWS ===")

    condition = df["UnitPrice"] < 0

    print(
        df.loc[
            condition,
            ["InvoiceNo", "StockCode", "Description",
            "Quantity", "InvoiceDate", "UnitPrice", "CustomerID"]
        ]
    )


    print("\n==== FIRST 5 ROWS ====")
    print(df.head())

if __name__ == "__main__":
    file_path = "./data/raw/online_retail.csv"
    df = pd.read_csv(file_path)
    profile_data(df)
