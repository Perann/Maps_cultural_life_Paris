from urllib import request
import re
import bs4
import numpy as np
import lxml
import pandas as pd

## accès à la page web

url_OFI_classique_Paris = 'https://www.offi.fr/concerts/programme.html?criterion_sch_ville=75&criterion_SRubrique=classique'
request_text = request.urlopen(url_OFI_classique_Paris).read() ### on ouvre la page web avec les concerts de musique classique 
page = bs4.BeautifulSoup(request_text, "lxml") ### donne du texte HTML utilisable (type bs4.BeautifulSoup)

## récupération des balises utiles 

beacon_a = page.find_all('a', class_ = 'page_numero') ### on trouve toutes les balises 'a' (balise d'hyperlien) avec la classe CCS page_numero 
start_page, end_page = int(beacon_a[0].get('data-page')), int(beacon_a[-1].get('data-page'))  ### on récupère les pages utiles avec get depuis la liste html on la transforme en int


### à ce stade on a une sorte de liste avec les numéros de page présents dans la page cad 1, 2, 3 et 43

## création du dictionnaire avec les liens 

links = {}
links[1] = 'https://www.offi.fr/concerts/programme.html?criterion_sch_ville=75&criterion_SRubrique=classique'
for p in range(start_page+1, end_page+1):
    links[p] = 'https://www.offi.fr/concerts/programme.html?npage='+ str(p) + 'criterion_sch_ville=75&criterion_SRubrique=classique'


print(links)