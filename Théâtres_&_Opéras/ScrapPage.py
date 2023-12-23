from urllib import request
import bs4
import numpy as np
import lxml
import pandas as pd

def PageScrap(url):
    site = request.urlopen(url)
    code_page = bs4.BeautifulSoup(site, 'lxml')
    fiches = code_page.find_all('div', class_ = 'mini-fiche-details d-flex has-padding-20')
    Data = {}
    Data['nom'] = []
    Data['etablissement'] = []
    Data['Date'] = []
    Data['adresse'] = []
    Data['commune'] = []
    Data['prix'] =[]
    
    InfoDates = code_page.find_all('div', class_ = 'has-padding-left-20 has-padding-right-20 has-padding-bottom-20')
    for info in InfoDates:
        Data['Date'].append(info.find('b'))
        
    for info in fiches:
        title  = info.find('div', class_ = 'event-title').find('span').text
        etablissement = info.find('div', class_ ='event-place').find('a', class_ = 'text-body')
        prix = info.find('div', class_ = 'tags-container').find_all('span')[2].text
    
        Data['nom'].append(title)
        Data['etablissement'].append(etablissement.text.strip())
        Data['prix'].append(prix)
        
        link = etablissement.get('href')
        site_etablissement = request.urlopen(link)
        htmml_etablissement = bs4.BeautifulSoup(site_etablissement, 'lxml')
        adresse = htmml_etablissement.find('div', class_ = 'page-subtitle').text
        InfoAdresse = adresse.split(' - ')
        Data['adresse'] = InfoAdresse[0]
        Data['commune'] = InfoAdresse[1]




    
    DataPage = pd.DataFrame(Data)
    return DataPage

if __name__ == '__main__':
    url = 'https://www.offi.fr/theatre/pieces-de-theatre.html?criterion_sch_ville=75'
    df = PageScrap(url)
    df.to_csv('datatest.csv')