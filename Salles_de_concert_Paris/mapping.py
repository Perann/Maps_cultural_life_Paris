import folium
import os
import pandas as pd
from datetime import datetime

data = pd.read_csv('/home/onyxia/work/Maps_cultural_life_Paris/Outputs/DataSets/DataMusiqueClassique_v2.csv', sep=';')

user_date_str = input("Veuillez entrer une date (format YYYY-MM-DD) : ")

user_date = datetime.strptime(user_date_str, '%Y-%m-%d')

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

    coordinates = [float(coord.strip('()')) for coord in row['coordonnees'].split(',')]

    popup_text = f"<b>{establishment_name}</b><br>Adresse: {address}<br>Pièce: {show_name}<br>Prix moyen: {average_price} €"

    folium.Marker(location=coordinates, popup=popup_text).add_to(my_map)

my_map.save("Classique.html")
