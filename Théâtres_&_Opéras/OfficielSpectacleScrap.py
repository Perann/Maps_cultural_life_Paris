#Dowloading of library
from urllib import request
import re
import bs4
import numpy as np
import lxml
import pandas as pd
import requests 
from ScrapPage import PageScrap


#Getting all the pages to scrap 
url = 'https://www.offi.fr/theatre/pieces-de-theatre.html?criterion_sch_ville=75'                                       #Récupération des liens des pages
site = request.urlopen(url).read()
page = bs4.BeautifulSoup(site, 'lxml')
beacon_a = page.find_all('a', class_ = 'page_numero')
ref_pages =[]
for a in beacon_a:
    ref_pages.append(int(a.get('data-page')))
n = len(ref_pages)
start_page, end_page = ref_pages[0], ref_pages[n-1]         
links = {}
links[1] = 'https://www.offi.fr/theatre/pieces-de-theatre.html?criterion_sch_ville=75'
for p in range(start_page+1, end_page):
    links[p] = 'https://www.offi.fr/theatre/pieces-de-theatre.html?npage='+ str(p) +'&criterion_sch_ville=75'

#Scrapping the pages
df_to_merge = []
for link in links.values():
    df_to_merge.append(PageScrap(link))
    
Data = pd.concat(df_to_merge, ignore_index= True)

Data.to_csv('DataTheatre.csv')


#Adding the adress and coordinates
#import pandas as pd
#Address = pd.read_csv('C:\\Users\\LENOVO\\Desktop\\Ou sortir à Paris\\Python_2A\\Théâtres_&_Opéras\\data_etablissements.csv')
#unnamed_column = Address.iloc[:,0]
#Address['etablissement'] = unnamed_column

#merged = pd.merge(Data, Address, on = 'etablissement', how = 'left')
#merged = merged.dropna(ignore_index = True)
#columns_to_drop = ['Unnamed: 0',"Date D'Ouverture",'Nombre De Sièges','Notes','Adresse_complete']
#merged.drop(columns = columns_to_drop, axis = 1, inplace= True)
#merged.to_csv('DataTheatre.csv')
