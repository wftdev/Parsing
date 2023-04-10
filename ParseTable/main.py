import requests
from bs4 import BeautifulSoup as BSoup
import csv


def get_html(url):
    response = requests.get(url)
    return response.text


def write_csv(data):
    with open('coinmarketcapdata.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['token'],
                         data['price'],
                         'https://coinmarketcap.com' + data['url']))


def get_data(html):
    soup = BSoup(html, 'lxml')
    table = soup.find('div', class_='sc-beb003d5-2 bkNrIb').find('table').find('tbody').find_all('tr')  # find all rows

    for row in table:
        cells = row.find_all('td')
        price = cells[3].text
        href = cells[2].find('a', class_='cmc-link').get('href')

        try:
            name = cells[2].find('a', class_='cmc-link').find_all('span')[1].text
        except Exception:
            name = cells[2].find('a', class_='cmc-link').find('p', class_='sc-4984dd93-0 kKpPOn').text

        try:
            token = cells[2].find('a', class_='cmc-link').find('span', class_='crypto-symbol').text
        except AttributeError:
            token = cells[2].find('a', class_='cmc-link').find('p', class_='sc-4984dd93-0 iqdbQL coin-item-symbol').text

        # print(name + '[' + token + ']: https://coinmarketcap.com' + href + ' ' + price)
        data = {'name': name,
                'token': token,
                'price': price,
                'url': href
                }

        write_csv(data)


def main():
    url = 'https://coinmarketcap.com/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
