import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)
last_page = False
page_number = 1

if response.status_code == 200:
    with open(f"Scraped Content.txt", "w", encoding="utf-8") as file:
        while not last_page:
            url = "https://quotes.toscrape.com/page/" + str(page_number)
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            quotes = soup.find_all("span", class_="text")
            authors = soup.find_all("small", class_="author")

            if quotes:
                for i in range(len(quotes)):
                    quote_text = quotes[i].text
                    author_text = authors[i].text
                    file.write(f"{quote_text} - {author_text}\n")
            else:
                last_page = True
                print("last page")
            page_number += 1


else:
    print(f"Error: {response.status_code}")