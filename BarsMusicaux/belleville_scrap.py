from urllib import request
import re
import bs4
import numpy as np
import lxml
import pandas as pd


def get_belleville_data():

    url = 'https://www.le-vieux-belleville.com/programme/'
    site = request.urlopen(url)
    code_page = bs4.BeautifulSoup(site, 'lxml')

    information = ['nom', 'date','heure','prix','etablissement','adresse','arrondissement']
    D ={key:[] for key in information}

    title_list = code_page.find_all('span', class_ = 'dp_pec_event_title_sp')
    date_list = code_page.find_all('span', class_ = 'dp_pec_date_event_time')

    for date in date_list:
        if len(date.text.split()) == 4:                                        #On exclut les conditions autres que les concerts"
            D['date'].append('' + date.text.split()[0] + date.text.split()[1] + date.text.split()[2])
            D['heure'].append(date.text.split()[3])
        
    for title in title_list:
        if title.text != "Fermeture exceptionnelle":
            D['nom'].append(title.text)

    n = len(D['nom'])
    D['prix'] = [0]*n
    D['etablissement'] = ['Le vieux belleville']*n
    D['adresse'] = ['12 rue des Envierges']*n
    D['arrondissement'] = [20]*n
    df = pd.DataFrame(D)
    return df

if __name__ == '__main__':
    get_belleville_data()