import pandas as pd
import json


def transform_postgres():
    df = pd.read_csv("data/raw/postgres/products.csv")

    df["source"] = "postgres"

    return df


def transform_api():
    with open("data/raw/api/products.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    df = pd.DataFrame(data["products"])

    df = df[["id", "title", "category", "price"]]

    df["source"] = "api"

    return df


def transform_web():
    with open("data/raw/web/books.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    df = pd.DataFrame(data)

    df["price"] = (
        df["price"]
        .str.replace("Â£", "", regex=False)
        .str.replace("£", "", regex=False)
        .astype(float)
    )

    df["currency"] = "GBP"
    df["source"] = "web"

    return df

def transform_mongodb():
    with open("data/raw/mongodb/reviews.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    df = pd.DataFrame(data)

    df["source"] = "mongodb"

    return df


if __name__ == "__main__":

    mongodb = transform_mongodb()

    print("\n=== MONGODB ===")
    print(mongodb.head())

    postgres = transform_postgres()
    api = transform_api()
    web = transform_web()

    print("=== POSTGRES ===")
    print(postgres.head())

    print("\n=== API ===")
    print(api.head())

    print("\n=== WEB ===")
    print(web.head())