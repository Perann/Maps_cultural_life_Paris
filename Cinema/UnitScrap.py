import bs4
import requests
import pandas as pd

HEADERS_IOS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    
url1 = 'https://www.cinefil.com/cinema/ugc-cine-cite-les-halles-paris/programmation'

def UnitScrapCinema(url, date, cinema,HEADERS = HEADERS_IOS):
    r = requests.get(url, headers= HEADERS_IOS)
    soup = bs4.BeautifulSoup(r.content,'lxml')

    Database = {}
    Database['nom'] = []
    Database['heure'] = []

    InfoFilm = soup.find_all('div', class_ = 'fiche-film')
    for info in InfoFilm:
        title = info.find('div', class_ = 'fiche-infos').find('a').text
        sceances = info.find('div', class_ = 'horaires').find_all('div')[2]
        times = sceances.find_all('div', class_ = 'h4')
        for time in times:
            Database['heure'].append(time.text)
            Database['nom'].append(title)
    
    print(Database)
    Database['date'] = [date]*len(Database['nom'])
    Database['etablissement'] = [cinema]*len(Database['nom'])
    Database['adresse'] = ['adresse']*len(Database['nom'])  
    Database['prix'] = ['variable']*len(Database['nom'])
    

    return Database

if __name__ == '__main__':
    DataUgc = pd.DataFrame(UnitScrapCinema(url1,'ajd','ugc chatelet'))
    print(DataUgc.head())
    