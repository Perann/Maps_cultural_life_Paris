import bs4
import requests
import pandas as pd
import unidecode 

# This function gets the data from a specific page, a header is requiered knowing that the website doen't allow python request

HEADERS_IOS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
url1 = 'https://www.cinefil.com/cinema/ugc-cine-cite-les-halles-paris/programmation'

def UnitScrapCinema(url, date, cinema,HEADERS = HEADERS_IOS):
    
    r = requests.get(url, headers= HEADERS_IOS)                     #We first open the page and parse it
    soup = bs4.BeautifulSoup(r.content,'lxml')

    Database = {}
    Database['nom'] = []
    Database['heure'] = []
    
    InfoFilm = soup.find_all('div', class_ = 'fiche-film')         #We store all the info on a dictionnary
    for info in InfoFilm:
        title = info.find('div', class_ = 'fiche-infos').find('a').text
        sceances = info.find('div', class_ = 'horaires').find_all('div')[2]
        times = sceances.find_all('div', class_ = 'h4')
        for time in times:
            Database['heure'].append(time.text)
            Database['nom'].append(title)
    
    
    Database['date'] = [date]*len(Database['nom'])                  #We complete some missing keys
    Database['etablissement'] = [cinema.upper()]*len(Database['nom'])
    Database['prix'] = ['variable']*len(Database['nom'])

    
    return Database

if __name__ == '__main__':                                          
    HEADERS_IOS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    url = 'https://www.cinefil.com/cinema/ugc-cine-cite-les-halles-paris/programmation'
    DataUgc = pd.DataFrame(UnitScrapCinema(url,'ajd','ugc chatelet'))
    print(DataUgc.head())
    