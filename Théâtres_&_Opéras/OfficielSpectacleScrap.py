from urllib import request
import re
import bs4
import numpy as np
import lxml
import pandas as pd

url = 'https://www.offi.fr/theatre/pieces-de-theatre.html?criterion_sch_ville=75'                                       #Récupération des liens des pages
site = request.urlopen(url).read()
page = bs4.BeautifulSoup(site, 'lxml')
beacon_a = page.find_all('a', class_ = 'page_numero')
links = {}
for a in beacon_a:
    links[a.get('data-page')] = url + a.get('href')
    
print(links)

