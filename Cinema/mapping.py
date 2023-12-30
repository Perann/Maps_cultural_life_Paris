import folium
import pandas as pd 
from folium.plugins import MarkerCluster
import webbrowser
from datetime import datetime


#Converting String in datetime object
def HourConversion(string):                                           
    return datetime.strptime(string, '%H:%M') 


#This is the function that does and print the Map 
def MovieMapping(data,MinHour,MaxHour):
    
    HeureDebut = datetime.strptime(MinHour, "%Hh%M")                            #Converting String in datetime object
    HeureFin = datetime.strptime(MaxHour, "%Hh%M")
    
    
    data['time'] = data['heure'].apply(lambda x: HourConversion(x))             #Filtering the Data with the times given
    AdjustedData = data[data['time']>= HeureDebut]
    AdjustedData = AdjustedData[AdjustedData['time'] <= HeureFin]
    
    MovieMap = folium.Map(location=[48.8566, 2.3522], zoom_start=12)            #Initializing the Map
    GeoVisited = {}

    for index, row in AdjustedData.iterrows():                                  #Adding each marker, if we previously had a marker at that spot
                                                                                #we create a cluster to print all the movie played in one                                                                                      #cinema
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
    
    MovieMap.save("Maps_cultural_life_Paris/Outputs/Maps/MovieMap.html")                            #Saving the Map
    

    html_file_path = 'Maps_cultural_life_Paris\Outputs\Maps\MovieMapToday.html'                          #Opening the Map on your default browser 
    webbrowser.open_new(html_file_path)

if __name__ == '__main__':
    program = pd.read_csv('Maps_cultural_life_Paris/Outputs/DataSets/DataCinema.csv')
    MovieMapping(program,'17h30','20h00')
