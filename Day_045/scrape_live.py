from bs4 import BeautifulSoup
import requests as r


response = r.get("https://news.ycombinator.com/news")
content = response.text
soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())
headline_first = soup.find('span', class_="titleline").text
print(headline_first)