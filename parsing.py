from bs4 import BeautifulSoup
import lxml
import requests

url = 'http://quotes.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

length = len(quotes)

for index in range(length):
    print(quotes[index].text)
    print(f'\t\t\t{authors[index].text}')
    t = tags[index].find_all('a', class_='tag')
    for item in t:
        print(f'\t\t\t#{item.text}')
# print(soup)