import requests
from bs4 import BeautifulSoup as BSoup
import csv


def get_html(url):
	response = requests.get(url)
	return response.text
	
	
def write_csv(data):
	with open('coinmarketcapdata.csv', a) as f:
		writer = csv.writer(f)
		pass


def get_data(html):
	soup = BSoup(html, 'lxml')
	table = soup.find('div', class_='sc-beb003d5-2 bkNrIb').find('table').find('tbody').find_all('tr') # find all rows 
	
	for row in table:
		cells = row.find_all('td') 
		#name = cells[2].find('a')
		href = cells[2].find('a', class_='cmc-link').get('href')
		print('https://coinmarketcap.com' + href)

def main():
	url = 'https://coinmarketcap.com/'
	get_data(get_html(url))

if __name__ == '__main__':
	main()
