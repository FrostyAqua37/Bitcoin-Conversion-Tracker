import requests
from bs4 import BeautifulSoup
import re

conversion_values = dict()

content = requests.get('https://bitcoinlive.org/')
soup = BeautifulSoup(content.text,'html.parser')
currency = []

def remove_tags(raw_html:str) -> str:
    pattern = re.compile('<.*?>')
    return re.sub(pattern, '', raw_html)

#All bitcoin exchange rate between currencies.
for il in soup.find_all('ul', class_ = 'cur-list'):
    currency.append(il.find_all('span'))


for country in currency:
    print(remove_tags(str(country)).strip())



