import requests
from bs4 import BeautifulSoup

URL = 'https://www.bundesgesundheitsministerium.de/coronavirus/chronik-coronavirus.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')


for div in soup.findAll('div', attrs={'class': None}):
    if " 2021" in div.text or " 2020" in div.text:
        print(div.text)
