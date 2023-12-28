import pandas as pd
from datetime import datetime 
import folium
import webbrowser

def TheaterMap(data:'Pandas DataFrame',date:'YYYY-MM-DD'):

    user_date = datetime.strptime(date, '%Y-%m-%d')
    data['date début'] = pd.to_datetime(data['date début'])
    data['date fin'] = pd.to_datetime(data['date fin'])
    filtered_data = data[(data['date début'] <= user_date) & (user_date <= data['date fin'])]
    


    paris_coordinates = [48.8566, 2.3522]
    my_map = folium.Map(location=paris_coordinates, zoom_start=12)

    for index, row in filtered_data.iterrows():
        establishment_name = row['etablissement']
        address = row['adresse']
        show_name = row['nom']
        average_price = row['prix moyen']

        coordinates = [float(coord.strip('()')) for coord in row['Coordonnees'].split(',')]
        popup_text = f"<b>{establishment_name}</b><br>Adresse: {address}<br>Pièce: {show_name}<br>Prix moyen: {average_price} €"
        folium.Marker(location=coordinates, popup=popup_text).add_to(my_map)
    
    my_map.save("Outputs\Maps\Theatermap.html")
    html_file_path = 'Outputs\Maps\Theatermap.html'
    webbrowser.open(html_file_path)


#Example: Display all theater pieces played the 12th january 2024 in Paris
if __name__ == '__main__':
    DataTheater = pd.read_csv('Outputs\DataSets\DataTheatre_base_finale.csv', sep=';')
    TheaterMap(DataTheater,'2024-01-12')