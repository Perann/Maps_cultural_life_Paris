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
ref_pages =[]
for a in beacon_a:
    ref_pages.append(int(a.get('data-page')))
n = len(ref_pages)
start_page, end_page = ref_pages[0], ref_pages[n-1]         #On a récupéré le numéro de la première et de
                                                            #la dernière page
links = {}
links[1] = 'https://www.offi.fr/theatre/pieces-de-theatre.html?criterion_sch_ville=75'
for p in range(start_page+1, end_page):
    links[p] = 'https://www.offi.fr/theatre/pieces-de-theatre.html?npage='+ str(p) +'&criterion_sch_ville=75'

#le dictionnaire links contient les liens de chacune des pages, 
# on va maintenant boucler sur les pages pour datascrapper chaque spectacle

for link in links.values():
    url = link
    site = request.urlopen(url).read()
    page = bs4.BeautifulSoup(site, 'lxml')
    information = page.find_all('div', class_ = "mini-fiche-details d-flex has-padding-20")
    print(information)



