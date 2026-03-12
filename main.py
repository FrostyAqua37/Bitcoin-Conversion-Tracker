import requests
from bs4 import BeautifulSoup

conversion_values = dict()

content = requests.get('https://bitcoinlive.org/')
soup = BeautifulSoup(content.text,'html.parser')

a = soup.find_all('ul', {'class': 'cur-list'})
b = []
for i in a:
    b.append(i.get_text())

