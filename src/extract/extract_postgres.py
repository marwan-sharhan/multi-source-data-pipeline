import pandas as pd
import psycopg


def extract_postgres():

    connection = psycopg.connect(
        host="localhost",
        dbname="ecommerce_source",
        user="postgres",
        password=""
    )

    query = "SELECT * FROM products"

    df = pd.read_sql(query, connection)

    connection.close()

    return df


if __name__ == "__main__":

    df = extract_postgres()

    raw_path = "./data/raw/postgres/products.csv"

    df.to_csv(raw_path, index=False)

    print("PostgreSQL data extracted successfully")
    print("Rows:", len(df))
    print("Raw file:", raw_path)