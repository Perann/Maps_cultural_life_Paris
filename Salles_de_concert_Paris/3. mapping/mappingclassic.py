import pandas as pd
from datetime import datetime 
import folium
import webbrowser


def ClassicalMap(data:'Pandas DataFrame',date:'YYYY-MM-DD'):

    ## on convertit la date de l'utilisateur au format datetime 
    
    user_date = datetime.strptime(date, '%Y-%m-%d')
    data['date datetime'] = pd.to_datetime(data['date datetime'])
    
    data['date datetime'] = data['date datetime'].apply(lambda x: x.replace(hour=0, minute=0, second=0, microsecond=0))
    user_date = user_date.replace(hour=0, minute=0, second=0, microsecond=0)


    
    filtered_data = data[(data['date datetime'] == user_date)]


    paris_coordinates = [48.8566, 2.3522]
    my_map = folium.Map(location=paris_coordinates, zoom_start=12)

    for index, row in filtered_data.iterrows():
        establishment_name = row['etablissement']
        address = row['adresse']
        show_name = row['nom']
        average_price = row['prix moyen']
        time = row['heure']
        
        coordinates = [float(coord.strip('()')) for coord in row['coordonnees'].split(',')]

        popup_text = f"<b>{establishment_name}</b><br>Adresse: {address}<br>Concert: {show_name}<br>Heure: {time}<br>Prix moyen: {average_price} €"
        folium.Marker(location=coordinates, popup=popup_text).add_to(my_map)
    
    my_map.save("Outputs\Maps\Classicmap.html")
    html_file_path = 'Outputs\Maps\Classicmap.html'
    webbrowser.open(html_file_path)


#Example: Display all theater pieces played the 29th December 2023 in Paris
if __name__ == '__main__':
    DataClassical = pd.read_csv('Outputs\DataSets\DataMusiqueClassique_v8.csv', sep=',')
    ClassicalMap(DataTheater,'2023-12-29')