import requests
import json

def extract_api():
    url = "https://dummyjson.com/products"
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    return response.json()

if __name__ == "__main__":

    data = extract_api()
    raw_path = "./data/raw/api/products.json"
    with open(raw_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print("API data extracted successfully")
    print("Raw file:", raw_path)