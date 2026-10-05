from pymongo import MongoClient
import json


def extract_mongodb():

    client = MongoClient("mongodb://localhost:27017/")

    database = client["ecommerce_source"]
    collection = database["reviews"]

    data = list(collection.find({}, {"_id": 0}))

    client.close()

    return data


if __name__ == "__main__":

    data = extract_mongodb()

    raw_path = "./data/raw/mongodb/reviews.json"

    with open(raw_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print("MongoDB data extracted successfully")
    print("Reviews:", len(data))
    print("Raw file:", raw_path)