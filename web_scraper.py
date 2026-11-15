import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []

for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()

    quotes.append({
        "quote": text,
        "author": author
    })

with open("quotes.json", "w", encoding="utf-8") as file:
    json.dump(quotes, file, indent=4, ensure_ascii=False)

print("Quotes scraped successfully!")
print("Total quotes:", len(quotes))