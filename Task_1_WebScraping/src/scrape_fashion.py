import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

print("Starting scraper...")

URL = "https://www.scrapingcourse.com/ecommerce/"
response = requests.get(URL)

print("Website status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("li", class_="product")
print("Products found:", len(products))

data = []

for product in products:
    name = product.find("h2").text.strip()
    price = product.find("span", class_="price").text.strip()
    link = product.find("a")["href"]
    image = product.find("img")["src"]

    data.append({
        "product_name": name,
        "category": "Fashion",
        "price": price,
        "product_url": link,
        "image_url": image
    })

df = pd.DataFrame(data)

# 🔥 Force directory creation
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

FILE_PATH = os.path.join(DATA_DIR, "fashion_products.csv")
df.to_csv(FILE_PATH, index=False)

print("CSV saved at:", FILE_PATH)
print("Task 1 completed successfully.")
