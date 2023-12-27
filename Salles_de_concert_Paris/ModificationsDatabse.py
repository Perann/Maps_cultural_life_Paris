import pandas as pd
import Fonctions as fct 



df = pd.read_csv('DataMusiqueClassique.csv')

df['adresse'] = df['adresse'] + 'Paris, France'
df['coordonnees'] = df['adresse'].apply(fct.obtenir_coordonnees_adresse) 

df = df.dropna(subset=['coordonnees']).reset_index(drop=True)

df.to_csv('DataMusiqueClassique_v2.csv')


