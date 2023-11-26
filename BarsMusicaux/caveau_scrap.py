from urllib import request
import re
import bs4
import numpy as np
import lxml
import pandas as pd


def get_days(string):                                                                 #Fonction pour tranfsormer les dates au bon format
    figures = re.findall(r'\d+', string)
    if 'au' in string:
        days = np.arange(int(figures[0]),int(figures[1])+1)
    elif 'et' in string:
        days = np.array([int(figures[0]),int(figures[1])])
    else:
        days = np.array([int(figures[0])])
    return days


def get_caveau_datas():
    url = "http://www.caveaudelahuchette.fr/"                                        #Récupération des liens des pages
    site = request.urlopen(url).read()
    page = bs4.BeautifulSoup(site, 'lxml')
    div = page.find_all('ul')
    menu = div[1]                                                                    #On récupère le code html du menu principal
    items = menu.find_all('li',class_= re.compile("concert", flags=re.IGNORECASE))   #On utilise regex pour récupérer tous les lignes qui contiennet le terme "concert"
    liens ={}
    for item in items:
        liens[str(item.get('class')[0].split('_')[1])] = url + item.a.get('href')
                                                                                  #On a récupéré les liens de la programmation pour chaques mois
    
    df_list = []
    for month in liens.keys():
        url = liens[month]                                                          #We go through each link we have
        site = request.urlopen(url).read()
        page = bs4.BeautifulSoup(site, 'lxml')
        balise_p = [p for p in page.find_all('p') if p.text.strip()]

        horaires =(balise_p[1].text.split()[7][:5], balise_p[1].text.split()[24][:5])     #Récupération des heures de concert sous le format (heure en semaine, heure le week-end)

        programmation = balise_p[2].get_text(separator = '%', strip = True).split('%')
    
        information = ['nom', 'date','heure','prix','etablissement','adresse','arrondissement']
        D ={key:[] for key in information}
        for concert in programmation:
            carac = concert.split(' : ')
            days = get_days(carac[0])
            for day in days:
                D['date'].append( str(day) + ' ' + month)
                D['nom'].append(carac[1])

        D['prix'] = [14]*len(D['nom'])
        D['etablissement'] = ['Caveau de la Huchette']*len(D['nom'])
        D['heure'] =['21h30']*len(D['nom'])
        D['adresse'] = ['5 rue de la Huchette']*len(D['nom'])
        D['arrondissement'] = ['5']*len(D['nom'])
        df_list.append(pd.DataFrame(D))
    
    return pd.concat(df_list, ignore_index= True)

if __name__ == '__main__':
    print(get_caveau_datas())