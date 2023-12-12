import bs4
import requests

HEADERS_IOS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    
r = requests.get('https://www.cinefil.com/cinema/ugc-cine-cite-les-halles-paris/programmation', headers= HEADERS_IOS)
soup = bs4.BeautifulSoup(r.content,'lxml')

InfoFilm = soup.find_all('div', class_ = 'fiche-film')
print(InfoFilm[0])
    