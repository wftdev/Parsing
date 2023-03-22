import requests
from bs4 import BeautifulSoup as BSoup


def get_html(url):
	response = requests.get(url)
	return response.text
	

def get_data(html):
	soup = BSoup(html, 'lxml')
	popular_section = soup.find_all('section')[3]
	return popular_section


def main():
	url = 'https://wordpress.org/plugins/'
	print(get_data(get_html(url)))
	

if __name__ == '__main__':
	main()
	
