import requests
from bs4 import BeautifulSoup as BSoup


def get_html(url):
	response = requests.get(url)
	return response.text
	

def get_data(html):
	soup = BSoup(html, 'lxml')
	popular_section = soup.find_all('section')[3]
	plugins = popular_section.find_all('article')
	
	for plugin in plugins:
		name = plugin.find('h3')
		print(name.text)
	
	#return len(plugins)


def main():
	url = 'https://wordpress.org/plugins/'
	get_data(get_html(url))
	

if __name__ == '__main__':
	main()
	
