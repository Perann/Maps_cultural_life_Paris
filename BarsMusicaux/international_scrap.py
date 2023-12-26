import bs4
import lxml
import pandas as pd
import urllib
from urllib import request

def get_international_data():
    url = "https://www.linternational.fr/agenda"   
    request_text = request.urlopen(url).read()
    page = bs4.BeautifulSoup(request_text, "lxml")
    exhibitions = page.find_all('div', class_ = "Zz5cHg")
    information = ['nom', 'date','heure','prix','etablissement','adresse','arrondissement', 'geo']
    D = {key:[] for key in information}
    id_inter = 0
    for exhibition in exhibitions:                                 
        info = exhibition.img.get('alt').split(' - ')
        D['nom'].append('International#' + str(id_inter)) 
        D['date'].append(info[0])
        D['heure'].append(info[1])
        D['prix'].append(info[2])
        id_inter = id_inter + 1
    n = len(D['date'])

    p = []                                                     #On enlève le '€' des prix
    for prix in D['prix']:
        p.append(prix[:-1])
    D['prix'] = p

    D['etablissement'] = ["L'international"]*n                  #On complète les infos qu'on a pas pour pouvoir faire un data_frame
    D['adresse'] = ["5 rue Moret"]*n
    D['arrondissement'] = [11]*n
    D['geo'] = [(48.866870695130075, 2.3794315537994883)]*n
    data = pd.DataFrame(D)
    return data

if __name__ == '__main__':
    get_international_data()


