import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    header = soup.find('div', id='wrapper').find('header', id='header').find('h1')
    return header.text


def main():
    url = 'https://archcraft.io/'
    header1 = get_data(get_html(url))
    print(header1)


if __name__ == '__main__':
    main()
