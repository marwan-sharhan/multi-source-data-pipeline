import pandas as pd


def transform_data(df):

    # 1. Convert InvoiceDate to datetime
    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"],
        errors="coerce"
    )

    # 2. Remove exact duplicate rows
    df = df.drop_duplicates()

    # 3. Classify transaction types
    df["TransactionType"] = "SALE"

    df.loc[
        df["InvoiceNo"].astype(str).str.startswith("C") &
        (df["Quantity"] < 0),
        "TransactionType"
    ] = "CANCELLATION"

    df.loc[
        ~df["InvoiceNo"].astype(str).str.startswith("C") &
        (df["Quantity"] < 0),
        "TransactionType"
    ] = "ANOMALY"

    print("\n=== MISSING VALUES AFTER DUPLICATES ===")
    print(df.isnull().sum())

    print("\n=== MISSING DESCRIPTION SAMPLE ===")
    print(
        df[df["Description"].isna()][
            ["InvoiceNo", "StockCode", "Quantity", "UnitPrice", "CustomerID"]
        ].head(20)
    )

    print("\n=== MISSING CUSTOMER ID BY TRANSACTION TYPE ===")

    print(
        df.groupby("TransactionType")["CustomerID"]
        .apply(lambda x: x.isna().sum())
    )

    # 4. Separate invalid UnitPrice rows
    invalid_price = df[df["UnitPrice"] < 0].copy()

    # Add rejection reason
    invalid_price["rejection_reason"] = "negative_unit_price"

    valid_data = df[df["UnitPrice"] >= 0].copy()

    # Save processed data
    processed_path = "./data/processed/online_retail_processed.csv"
    valid_data.to_csv(processed_path, index=False)

    # Save quarantine data
    quarantine_path = "./data/quarantine/online_retail_quarantine.csv"
    invalid_price.to_csv(quarantine_path, index=False)

    print("\n=== FILES SAVED ===")
    print("Processed:", processed_path)
    print("Quarantine:", quarantine_path)

    valid_data["PriceStatus"] = "NORMAL"

    valid_data.loc[
        valid_data["UnitPrice"] == 0,
        "PriceStatus"
    ] = "ZERO_PRICE"

    print("\n=== PRICE STATUS ===")
    print(valid_data["PriceStatus"].value_counts())

    print("\n=== ZERO PRICE BY TRANSACTION TYPE ===")

    print(
        valid_data[valid_data["UnitPrice"] == 0]["TransactionType"]
        .value_counts()
    )

    print("\n=== TRANSACTION TYPES ===")
    print(valid_data["TransactionType"].value_counts())

    print("\n=== QUARANTINE DATA ===")
    print(invalid_price)

    return valid_data, invalid_price


if __name__ == "__main__":

    file_path = "./data/raw/online_retail.csv"

    df = pd.read_csv(file_path)

    valid_data, invalid_price = transform_data(df)

    print("=== TRANSFORM RESULT ===")
    print("Original rows:", len(df))
    print("Valid rows:", len(valid_data))
    print("Invalid price rows:", len(invalid_price))