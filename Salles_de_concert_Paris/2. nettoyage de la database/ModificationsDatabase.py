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

## séparation des dates ##

df['Date'] = df['Date'].apply(lambda x : x.split(',') if isinstance(x, str) else x)
df = df.explode('Date').reset_index(drop=True)
df['Date'] = df['Date'].apply(lambda x : str(x[0]) if isinstance(x, list) and len(x) > 0 else x) ### on avait une liste et on veut avoir un str 
df = df[df['Date'].str.contains(':')] ## on retire quelques cas problématiques ou on a que l'heure 

## création de dates exploitables en datetime ##

df['Date'] = df['Date'].apply(lambda x : x.replace(":",''))
df['date datetime'] = df['Date'].apply(fct.conversion_datetime)

df['heure'] = df['Date'].apply(lambda x : x[-5:])

# Sauvegarde de la base de données au format csv
df.to_csv('DataMusiqueClassique_v7.csv', index=False)

