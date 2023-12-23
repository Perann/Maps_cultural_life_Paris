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
    InfoDates = code_page.find_all('div', class_ = 'has-padding-left-20 has-padding-right-20 has-padding-bottom-20')
    for info in InfoDates:
        Data['Date'].append(info.find('b'))
        
    for info in fiches:
        title  = info.find('div', class_ = 'event-title').find('span').text
        etablissement = info.find('div', class_ ='event-place').find('a').text.strip()
        Data['nom'].append(title)
        Data['etablissement'].append(etablissement)
        

    Data['prix'] = ['variable']*len(Data['nom'])
    
    DataPage = pd.DataFrame(Data)
    return DataPage

if __name__ == '__main__':
    url = 'https://www.offi.fr/theatre/pieces-de-theatre.html?criterion_sch_ville=75'
    df = PageScrap(url)
    print(df.tail())