import bs4
import requests

HEADERS_IOS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    
r = requests.get('https://www.cinefil.com/cinema/ugc-cine-cite-les-halles-paris/programmation', headers= HEADERS_IOS)
soup = bs4.BeautifulSoup(r.content,'lxml')

Database = {}
Database['nom']  = []
Database['heure'] = []
Database['date'] = []
Database['etablissement'] =[]
Database['adresse'] = []
Database['prix'] = []

InfoFilm = soup.find_all('div', class_ = 'fiche-film')


for info in InfoFilm:
    title = info.find('div', class_ = 'fiche-infos').find('a').text
    Database['nom'].append(title)
    sceances = info.find('div', class_ = 'horaires').find_all('div')[2]
    times = sceances.find_all('div', class_ = 'h4')
    for time in times:
        Database['heure'].append(time.text)
        Database['nom'].append(title)
print(Database)


