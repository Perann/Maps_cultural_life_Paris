import folium
import pandas as pd 
from folium.plugins import MarkerCluster
import webbrowser
from datetime import datetime

def HourConversion(string):
    return datetime.strptime(string, '%H:%M') 

def MovieMapping(data,hour):
    
    heure_formattee = datetime.strptime(str(hour), '%H')
    data['time'] = data['heure'].apply(lambda x: HourConversion(x))
    AdjustedData = data[data['time']>= heure_formattee]
    
    MovieMap = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
    GeoVisited = {}

    for index, row in AdjustedData.iterrows():
        lat = row['geo'].split(',')[0]
        lon = row['geo'].split(',')[1]
    
        content = "<h4 style='color:black;'>" + row['nom'] + "</h4>" \
                "<p style='font-size:16px;'>" + row['etablissement'] + "</p>"\
                "<p style='font-size:16px;'>" + row['heure'] + "</p>"
        
            
        if (lat,lon) not in GeoVisited.keys():
            GeoVisited[(lat,lon)] = MarkerCluster().add_to(MovieMap)
            folium.Marker(location=(lat,lon), popup = content, max_width=500).add_to(GeoVisited[(lat,lon)])
        else:
            folium.Marker(location=(lat,lon), popup = content, max_width=500).add_to(GeoVisited[(lat,lon)])
    MovieMap.save("Outputs\Maps\MovieMapToday.html")

if __name__ == '__main__':
    program = pd.read_csv('Outputs\DataSets\DataCinema.csv')
    MovieMapping(program,17)
