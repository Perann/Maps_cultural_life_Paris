import pandas as pd

#Plotting the map of Cinema
from Cinema.mapping import MovieMapping
data = pd.read_csv('Outputs\DataSets\DataCinema.csv')
MovieMapping(data,'18h30','21h00')

#Plotting the map of Theater
