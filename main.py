import pandas as pd

#Plotting the map of Cinema
from Cinema.mapping import MovieMapping
data = pd.read_csv('Outputs\DataSets\DataCinema.csv')
MovieMapping(data,'15h30','20h30')

#Plotting the map of Theater
