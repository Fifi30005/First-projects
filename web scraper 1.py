import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)

with open("scraped Content.txt", "w") as file:
    file.write("")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    for i in range(len(quotes)):
        quote_text = quotes[i].text
        author_text = authors[i].text
        with open("scraped Content.txt", "a") as file:
           file.write(f"{quote_text} - {author_text}\n")


else:
    print(f"Error: {response.status_code}")