from urllib import request
import bs4
import pandas as pd
import lxml
import numpy as np


url = 'https://www.cinefil.com/seances-cinema/paris'

import requests
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
r = requests.get(url, headers=HEADERS)
soup = bs4.BeautifulSoup(r.content, 'lxml')
LinksCinema = {}
list = soup.find_all('a', class_ = 'SEOajust')
for html in list[:-4]:
    name = html.find('h3').text
    link = html.get('href')
    LinksCinema[name] = link

print(LinksCinema)