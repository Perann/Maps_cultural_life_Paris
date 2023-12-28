import pandas as pd
import Fonctions as fct 

## Ajout des coordonnées ##

df = pd.read_csv('DataMusiqueClassique.csv')

df['adresse'] = df['adresse'] + ', Paris, France'
df['coordonnees'] = df['adresse'].apply(fct.obtenir_coordonnees_adresse) 

df = df.dropna(subset=['coordonnees']).reset_index(drop=True)

df = df.drop('Unnamed: 0', axis=1)



## Création d'un prix moyen ##

cleaned_prices = df['prix'].apply(fct.clean_price)

df[['prix min', 'prix max', 'prix unique']] = pd.DataFrame(cleaned_prices.tolist(), index=df.index)

df['prix moyen'] = df.apply(lambda row: (row['prix min'] + row['prix max']) / 2
                            if pd.notnull(row['prix min']) and pd.notnull(row['prix max'])
                            else row['prix unique'], axis=1)

## Création de dates exploitables ##

Dates_usable =  df['Date'].apply(fct.convertir_en_datetime)

df[['dates datime', 'heures datetime']] = pd.DataFrame(Dates_usable.tolist(), index=df.index)

## Sauvegarde de la base de données au format csv

df.to_csv('DataMusiqueClassique_v2.csv',index = False)

