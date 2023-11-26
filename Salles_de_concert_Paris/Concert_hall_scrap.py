import bs4
import lxml
import pandas as pd
from urllib import request

def get_OFS_data():

    url_salles_de_concert = 'https://www.offi.fr/concerts/salles-de-concert-paris.html'  ## URL of the stripped page
    request_text = request.urlopen(url_salles_de_concert).read()   ## opens the URL
    page = bs4.BeautifulSoup(request_text, "lxml") ## We get a usable html text
    table_concert_hall = page.find('table',{'class' : 'tableau-liste'}) ## accessing the table we want to scrap
    table_body = table_concert_hall.find_all('tbody')[1] ## accessing the body of the table (there is another tbody before thee one we want to access hence the find_all)
    table_rows = table_body.find_all('tr')  ## creates a list containing all the lines 

    Dict = {}

    for row in table_rows:
        table_col = row.findAll('td')
        table_col = [cell.text.strip() for cell in table_col]
        Dict[table_col[0]] = table_col[1:]

    Data_concert_hall = pd.DataFrame.from_dict(Dict,orient='index')

    titles = []
    table_titles = table_concert_hall.find('tbody')
    cols = table_titles.findAll('th') ## there is only one line here so we access directly to the columns 
    
    for col in cols:
        titles.append(col.text.strip())

    Data_concert_hall.columns = titles[1:]

    url_salle_indiv = [] ## on recupere les URL des salles 
    for row in table_rows:
        hyp_finder = row.find('td').find('a') ## a indique un lien hypertext 
        hyperl = hyp_finder['href'] ## maniere d'acceder à l'URL
        hyperl = 'https://www.offi.fr' + hyperl ## on ajoute l'adresse generique pour permettre la recherche
        url_salle_indiv.append(hyperl)

    Address = []
    Locality = []

    for url in url_salle_indiv: ## prend du temps à tourner
        try : 
    
            request_text_salle = request.urlopen(url).read()
            page_indiv = bs4.BeautifulSoup(request_text_salle, "lxml")
            address_indiv = [page_indiv.find('span',{'itemprop' : 'streetAddress'}), page_indiv.find('span',{'itemprop' : 'addressLocality'})]
            Address.append(address_indiv[0].text.strip())
            Locality.append(address_indiv[1].text.strip())

        except Exception as e:  ### on a un probleme avec l'adesse 29 

            Address.append("61 rue du Chateau d'Eau") ## the url for this element didn' work, here is their website : https://www.etoiles.paris/contact
            Locality.append("Paris 10e")


    
    Data_concert_hall['Rue'] = Address
    Data_concert_hall['Arrondissement'] = Locality

    
    return Data_concert_hall

if __name__ == '__main__':
    get_OFS_data()


