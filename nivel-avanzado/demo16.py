import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.python.org')
soup = BeautifulSoup(response.content, 'html.parser')

for enlace in soup.find_all('a'):
    print(enlace.get('href'))
