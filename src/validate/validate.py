import pandas as pd


def validate_data(df):

    errors = {}

    errors["missing_invoice_no"] = df["InvoiceNo"].isna().sum()
    errors["missing_stock_code"] = df["StockCode"].isna().sum()
    errors["zero_quantity"] = (df["Quantity"] == 0).sum()
    errors["negative_unit_price"] = (df["UnitPrice"] < 0).sum()

    # تحويل التاريخ إلى datetime قبل التحقق منه
    invoice_dates = pd.to_datetime(
        df["InvoiceDate"],
        errors="coerce"
    )

    errors["invalid_invoice_date"] = invoice_dates.isna().sum()

    return errors


def create_quality_report(results):

    report = pd.DataFrame(
        list(results.items()),
        columns=["rule", "invalid_count"]
    )

    report["status"] = report["invalid_count"].apply(
        lambda x: "PASS" if x == 0 else "FAIL"
    )

    report_path = "./reports/quality_report.csv"

    report.to_csv(
        report_path,
        index=False
    )

    print("\n=== QUALITY REPORT ===")
    print(report)

    print("\nQuality report saved to:")
    print(report_path)


if __name__ == "__main__":

    file_path = "./data/processed/online_retail_processed.csv"

    df = pd.read_csv(file_path)

    print("=== PROCESSED DATA CHECK ===")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    results = validate_data(df)

    print("\n=== VALIDATION RESULTS ===")

    for rule, count in results.items():
        print(f"{rule}: {count}")

    create_quality_report(results)