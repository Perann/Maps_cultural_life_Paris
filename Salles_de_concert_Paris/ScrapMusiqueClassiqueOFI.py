from urllib import request
import bs4
import numpy as np
import lxml
import pandas as pd

def ScrapMusiqueOFI(url): 
    site = request.urlopen(url)
    code_page = bs4.BeautifulSoup(site, 'lxml')

    ## Création du dictionnaire qui va servir à générer le dataframe

    keys = ['nom','etablissement','Date','adresse','commune','prix']
    Data = {key: [] for key in keys}

    InfoDates = code_page.find_all('div', class_ = 'has-padding-left-20 has-padding-right-20 has-padding-bottom-20')
    for info in InfoDates:
        Data['Date'].append(info.find('b').text.strip()) ### on ajoute à la liste dans le dictionnaire les dates (on trouve la première balise b, on récupère le texte et on retire les espaces plus tard *)
        
    ## Extraction des autres informations

    fiches = code_page.find_all('div', class_ = 'mini-fiche-details d-flex has-padding-20')     
    for fiche in fiches:
        if fiche.find('div', class_ = 'event-title'):                       ### on extrait le nom de l'évènement (qui n'est pas toujours précisé, d'ou le if)
            title = fiche.find('div', class_ = 'event-title').find('span').text
        else: 
            title = 'unknown' 
        
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
        Data['etablissement'].append(etablissement.text.strip()) ### (*) on ne strip qu'ici à cause de la ligne plus bas 
        Data['prix'].append(prix)

        
        link = etablissement.get('href') ### on récupère le lien du site web de l'établissement 
        site_etablissement = request.urlopen(link) 
        html_etablissement = bs4.BeautifulSoup(site_etablissement, 'lxml')
        adresse = html_etablissement.find('div', class_ = 'page-subtitle').text
        InfoAdresse = adresse.split(' - ')
        Data['adresse'].append(InfoAdresse[0])
        Data['commune'].append(InfoAdresse[1])
    
    print('ok')
    DataPage = pd.DataFrame(Data)
    return DataPage



if __name__ == '__main__':
    url = 'https://www.offi.fr/concerts/programme.html?criterion_sch_ville=75&criterion_SRubrique=classique'
    df = ScrapMusiqueOFI(url)
    df.to_csv('datatest.csv')
