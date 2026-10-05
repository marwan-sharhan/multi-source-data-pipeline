import requests
from bs4 import BeautifulSoup
import json


def extract_web():

    url = "https://books.toscrape.com/"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    for book in soup.select("article.product_pod"):

        title = book.h3.a["title"]
        price = book.select_one(".price_color").text.strip()

        products.append({
            "title": title,
            "price": price
        })

    return products


if __name__ == "__main__":

    data = extract_web()

    raw_path = "./data/raw/web/books.json"

    with open(raw_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print("Web data extracted successfully")
    print("Products:", len(data))
    print("Raw file:", raw_path)