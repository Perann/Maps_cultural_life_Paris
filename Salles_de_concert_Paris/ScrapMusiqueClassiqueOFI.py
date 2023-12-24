from urllib import request
import bs4
import numpy as np
import lxml
import pandas as pd

def ScrapMusiqueOFI(url): 
    site = request.urlopen(url)
    code_page = bs4.BeautifulSoup(site, 'lxml')

    ## Création du dictionnaire qui va servir à générer le dataframe

    Data = {} 
    Data['nom'] = []
    Data['etablissement'] = []
    Data['Date'] = []
    Data['adresse'] = []
    Data['commune'] = []
    Data['prix'] =[]

    ## Extraction des dates des évènements (on doit faire 2 boucles) /!\ on pourrait n'en faire qu'une avec une manip /!\

    InfoDates = code_page.find_all('div', class_ = 'has-padding-left-20 has-padding-right-20 has-padding-bottom-20')
    for info in InfoDates:
        Data['Date'].append(info.find('b').text.strip()) ### on ajoute à la liste dans le dictionnaire les dates (on trouve la première balise b, on récupère le texte et on retire les espaces)
        
    ## Extraction des autres informations

    fiches = code_page.find_all('div', class_ = 'mini-fiche-details d-flex has-padding-20')     
    for fiche in fiches:
        title = fiche.find('div', class_ = 'event-title').find('span').text ### on extrait le nom de l'évènement
        etablissement = fiche.find('div', class_ ='event-place').find('a', class_ = 'text-body')
        
        span_list = fiche.find('div', class_ = 'tags-container').find_all('span')
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

        ### ici il y a des pbs à résoudre
        
        link = etablissement.get('href')
        site_etablissement = request.urlopen(link)
        html_etablissement = bs4.BeautifulSoup(site_etablissement, 'lxml')
        adresse = html_etablissement.find('div', class_ = 'page-subtitle').text
        InfoAdresse = adresse.split(' - ')
        Data['adresse'] = InfoAdresse[0]
        Data['commune'] = InfoAdresse[1]
    
    DataPage = pd.DataFrame(Data)
    return DataPage



if __name__ == '__main__':
    url = 'https://www.offi.fr/theatre/pieces-de-theatre.html?criterion_sch_ville=75'
    df = ScrapMusiqueOFI(url)
    df.to_csv('datatest.csv')
