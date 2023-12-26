from urllib import request
import bs4
import numpy as np
import lxml
import pandas as pd

def PageScrap(url):
    site = request.urlopen(url)
    code_page = bs4.BeautifulSoup(site, 'lxml')
    fiches = code_page.find_all('div', class_ = 'mini-fiche-details d-flex has-padding-20')
    
    keys = ['nom','etablissement','Date','adresse','commune','prix']
    Data = {key: [] for key in keys}
   
    
    InfoDates = code_page.find_all('div', class_ = 'has-padding-left-20 has-padding-right-20 has-padding-bottom-20')
    for info in InfoDates:
        if info.find('b'):
            Data['Date'].append(info.find('b').text)
        else:
            Data['Date'].append('unknown')
        
    for info in fiches:
        title  = info.find('div', class_ = 'event-title').find('span').text
        etablissement = info.find('div', class_ ='event-place').find('a', class_ = 'text-body')
        
        span_list = info.find('div', class_ = 'tags-container').find_all('span')
        figures =[]
        for span in span_list:
            if any(char.isdigit() for char in span.text):
                figures.append(span.text)
        
        if figures != []:
            prix = figures[0]
        else:
            prix = 'unknown'

    
        Data['nom'].append(title)
        Data['etablissement'].append(etablissement.text.strip())
        Data['prix'].append(prix)
        
        link = etablissement.get('href')
        site_etablissement = request.urlopen(link)
        htmml_etablissement = bs4.BeautifulSoup(site_etablissement, 'lxml')
        adresse = htmml_etablissement.find('div', class_ = 'page-subtitle').text
        InfoAdresse = adresse.split(' - ')
        Data['adresse'].append(InfoAdresse[0])
        Data['commune'].append(InfoAdresse[1])
    
    DataPage = pd.DataFrame(Data)
    return DataPage

if __name__ == '__main__':
    url = 'https://www.offi.fr/theatre/pieces-de-theatre.html?criterion_sch_ville=75'
    df = PageScrap(url)
    df.to_csv('datatest.csv')