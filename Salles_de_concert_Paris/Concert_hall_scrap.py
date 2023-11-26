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

    return Data_concert_hall

if __name__ == '__main__':
    get_OFS_data()


