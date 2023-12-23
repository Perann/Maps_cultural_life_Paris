import folium
import pandas as pd 

program = pd.read_csv('Output\DataSets\DataCinema.csv')


# Créer une carte centrée sur une position géographique
MovieMap = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

for index, row in program.iterrows():
    lat = row['geo'].split(',')[0]
    lon = row['geo'].split(',')[1]
    content = "<h4 style='color:black;'>" + row['nom'] + "</h4>" \
            "<p style='font-size:16px;'>" + row['etablissement'] + "</p>"\
            "<p style='font-size:16px;'>" + row['adresse'] +"</p>"
    folium.Marker(location=(lat,lon), popup = content, max_width=500).add_to(MovieMap)

MovieMap.save("MovieMapToday.html")
