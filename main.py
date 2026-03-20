import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def html_content(url:str) -> object:
    page = requests.get(url)
    return BeautifulSoup(page.text, 'html.parser')

def get_conversion_table(table:object) -> object:
    return table.find_all('div', class_ = 'col-full-flex')[2]

def get_currency_values(exchange_table:object) -> list[str]:
    #Finds all exchange rate between all currencies
    values = exchange_table.find_all('span', class_ = 'pull-right')
    values = [value.text.replace('\xa0', ' ') for value in values] #Removes any HTML tags and creates space between code and currency value
    return [value.split(' ')[-2] for value in values]

def get_currency_name(exchange_table:object) -> list[str]:
    #Finds every <a> tag in given table
    country_code = exchange_table.find_all('a', href = True)
    country_code = [code.text.strip() for code in country_code] #Removes tags and any blank spaces at each end.

    return [code.split('-')[1].strip() for code in country_code] #Splits at '-' and only returns currency name.

def get_bitcoin_df(names, values) -> pd.DataFrame:
    df = pd.DataFrame(columns = ['currency_name', 'currency_value'])

    for i in range(len(names)):
        #Formats value and creates dictionary of exchange rates
        values[i] = keep_number(values[i])
        row = [names[i], values[i]]

        df.loc[i] = row

    return df


def keep_number(string:str) -> str:
    # Removing any non-numeric characters but keeps commas and dots
    return re.sub("[^0-9,.]", "", string)

def main():
    html_page = html_content('https://bitcoinlive.org/')
    conversion_table = get_conversion_table(html_page)
    currency_names = get_currency_name(conversion_table)    #List over currency names
    currency_values = get_currency_values(conversion_table) #List over currency value for 1 bitcoin.

    bitcoin_df = get_bitcoin_df(currency_names, currency_values)
    bitcoin_df.to_csv('bitcoin_df.csv', index=False)

if __name__ == '__main__':
    main()

