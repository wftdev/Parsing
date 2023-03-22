import requests
from bs4 import BeautifulSoup as BSoup
import csv


def get_html(url):
	response = requests.get(url)
	return response.text
	

def normalize_text(text):
	splitted = text.split(' ')[0]
	result = splitted.replace(',', '')
	return result
	
	
def write_to_csv(data):
	with open('plugins.csv', 'a') as f:
		writer = csv.writer(f)	
		writer.writerow((data['name'],
						data['url'],
						data['rating']))	
	

def get_data(html):
	soup = BSoup(html, 'lxml')
	popular_section = soup.find_all('section')[3]
	plugins = popular_section.find_all('article')
	
	for plugin in plugins:
		name = plugin.find('h3').text
		url = plugin.find('h3').find('a').get('href')
		rating = plugin.find('span', class_='rating-count').find('a').text
		rating = normalize_text(rating)
		
		data = {'name': name,
				'url': url,
				'rating': rating}
				
		write_to_csv(data)
		
		


def main():
	url = 'https://wordpress.org/plugins/'
	get_data(get_html(url))
	

if __name__ == '__main__':
	main()
	
