import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

titles = soup.find_all('h2')

print('Lista de Títulos:')
for title in titles:
    print(title.text.strip())