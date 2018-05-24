import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.3gpp.org/specifications/specification-numbering')
soup = BeautifulSoup(r.content, 'lxml')
print(soup.table)
