import requests
from bs4 import BeautifulSoup
import re

exchange_rates: dict[str, str] = dict()
indices: list[str] = []

def html_content(url:str) -> object:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def get_conversion_table(table:object) -> object:
    return table.find_all('div', class_ = 'col-full-flex')[2]

def get_exchange_rates(exchange_table:object) -> list[str]:
    #Finds all exchange rate between all currencies
    values = exchange_table.find_all('span', class_ = 'pull-right')
    values = [value.text.replace('\xa0', ' ') for value in values] #Removes any HTML tags and creates space between code and currency value
    return [value.split(' ')[3].strip() for value in values]

def get_currency_name(exchange_table:object) -> list[str]:
    #Finds every <a> tag in given table
    country_code = exchange_table.find_all('a', href = True)
    country_code = [code.text.strip() for code in country_code] #Removes tags and any blank spaces at each end.

    return [code.split('-')[1].strip() for code in country_code] #Splits at '-' and only returns currency name.

def remove_tags(html_content:object) -> list[str]:
    ...

def format_text(text_content:list[str]) -> list[str]:
    ...


def main():
    html_page = html_content('https://bitcoinlive.org/')
    conversion_table = get_conversion_table(html_page)
    currency_name = get_currency_name(conversion_table)


if __name__ == '__main__':
    main()

