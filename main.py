import requests
from bs4 import BeautifulSoup

exchange_rates: dict[str, str] = dict()
indices: list[str] = []

def html_content(url:str) -> object:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def get_conversion_table(table:object) -> list[str]:
    return table.find_all('span', class_ = 'pull-right')[8:]

def remove_html(content:list[str]) -> list[str]:
    new_list:list[str] = []

    for row in content:
        new_list.append(row.text.strip())

    return new_list

def get_exchange_rates(table:list[str]):
    for row in table:
        try:
            country, rate = row.split('\xa0')

            exchange_rates[country] = rate
        except:
            indices.append(row)

def main():
    html_page = html_content('https://bitcoinlive.org/')
    exchange_table = get_conversion_table(html_page)
    exchange_table = remove_html(exchange_table)
    get_exchange_rates(exchange_table)



if __name__ == '__main__':
    main()

