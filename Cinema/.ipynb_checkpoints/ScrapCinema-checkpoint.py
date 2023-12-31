from urllib import request
import bs4
import pandas as pd
import lxml
import numpy as np
import requests
import unidecode
from UnitScrap import UnitScrapCinema


#Defining a Header to Datascrap (The site doesn't allow python request)
HeadersDefault = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}


def ScrapCinema(url,day,HEADERS = HeadersDefault):

    r = requests.get(url, headers=HEADERS)                #Getting the links of all pages to scrap
    soup = bs4.BeautifulSoup(r.content, 'lxml')
    LinksCinema = {}
    list = soup.find_all('a', class_ = 'SEOajust')
    for html in list[:-4]:
        name = html.find('h3').text
        name = name.upper()
        name = unidecode.unidecode(name)
        name = name.replace('-',' ')
        link = html.get('href')
        LinksCinema[name] = link

    dfList = []                                                  #Concatenate each Dataframe from pages
    for name_cinema in LinksCinema.keys():
        dfList.append(pd.DataFrame(UnitScrapCinema(LinksCinema[name_cinema],day, name_cinema)))

    DataCinema = pd.concat(dfList, axis=0, ignore_index=True)    #Creating an only DataFrame

    ref = pd.read_csv('Ressources\Data\ListeCinema.csv', sep = ';')          #Merging with an opendata list to get the coordinates

    ref.rename(columns={'nom': 'etablissement'}, inplace=True)
    merged_df = pd.merge(DataCinema, ref, on ='etablissement', how='left')
    columns_to_drop = ['ndeg_auto','dep','region_administrative','code_insee','situation_geographique','ecrans','fauteuils','tranche_d_entrees','proprietaire','programmateur','categorie_art_et_essai','label_art_et_essai','genre','multiplexe','population_de_la_commune_2015','unite_urbaine_2010','population_unite_urbaine_2015','semaines_d_activite_2020','seances_2020','entrees_2020','entrees_2019','evolution_entrees_2020_2019','art_et_essai','nombre_de_films_programmes_2020','nombre_de_films_inedits_2020','nombre_de_films_en_semaine_1_2020','pdm_en_entrees_des_films_francais_2020','pdm_en_entrees_des_films_americains_2020','pdm_en_entrees_des_films_europeens_2020','pdm_en_entrees_des_autres_films_2020','films_art_et_essai_2020','part_des_seances_de_films_art_et_essai_2020','pdm_en_entrees_des_films_art_et_essai_2020']
    merged_df.drop(columns = columns_to_drop, axis = 1, inplace= True)
    merged_df = merged_df.dropna()
    merged_df.to_csv('Outputs/DataSets/DataCinema.csv', index=False)
    return merged_df


if __name__ == '__main__':
    url = 'https://www.cinefil.com/seances-cinema/paris'
    ScrapCinema(url,'28/12')