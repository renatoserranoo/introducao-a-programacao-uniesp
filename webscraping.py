import requests
import csv
from bs4 import BeautifulSoup

f = csv.writer(open('N-nomes-de-artistas.csv', 'w'))
f.writerow(['Name', 'Link'])

paginas = []

for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anN' + \
        str(i) + '.htm'
    paginas.append(url)

for item in paginas:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    ultimoslinks = soup.find(class_='AlphaNav')
    ultimoslinks.decompose()

    nomeartistalista = soup.find(class_='BodyText')
    nomeartistaitens = nomeartistalista.find_all('a')

    for nomeartista in nomeartistaitens:
        names = nomeartista.contents[0]
        links = 'https://web.archive.org' + nomeartista.get('href')

        f.writerow([names, links])
