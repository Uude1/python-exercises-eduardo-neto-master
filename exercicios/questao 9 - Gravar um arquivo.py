import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

titles = soup.find_all('h2')

with open('nytimes_titles.txt', 'w') as f:
    f.write('Lista de Títulos:\n')
    for title in titles:
        f.write(title.text.strip() + '\n')