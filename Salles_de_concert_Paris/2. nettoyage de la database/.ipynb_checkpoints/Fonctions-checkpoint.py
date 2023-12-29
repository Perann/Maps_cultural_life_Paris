""" Fonctions utiles pour modifier  la database """

### importation des coordonnées depuis adresse.data.gouv.fr ###

import pandas as pd
import requests

def obtenir_coordonnees_adresse(adresse):
    """ 
    fonction qui prend en argument une adresse au format : rue, commune, France
    et qui retourne ses coordonnées dans un tuple
    """

    base_url = "https://api-adresse.data.gouv.fr/search/"
    params = {
        "q": adresse,
        "limit": 1
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get('features'):
            coordinates = data['features'][0]['geometry']['coordinates']
            return tuple(coordinates)
        else:
            return None
    else:
        print(f"Erreur lors de la requête : {response.status_code}")
        return None

### fonction de nettoyage des prix ###

import re

def clean_price(price_string):
    """
    prend en argument un string avec des prix et retourne le tuple (triplet) avec (min / none ; max / none ; le prix unique / unknown / none)
    """
    
    cleaned_price = price_string.replace(' ', '').replace('€', '')

    cleaned_price = cleaned_price.replace(',', '.')

    if '-' in cleaned_price:
        min_price, max_price = map(float, cleaned_price.split('-'))
        return min_price, max_price, None
    else:
        try:
            price_value = float(cleaned_price)
            return None, None, price_value
        except ValueError:
            return None, None, 'unknown'

### fonction de création de dates exploitables ###

from datetime import datetime

def conversion_datetime(date_str):
    """
    prend en argument un string de date sous la forme 'Mercredi 27 Janvier 18h00' et restitute un format datetime 
    gère les nombreuses exceptions de la base de données notamment les abréviations type "Dim" et les numéros de dates en format ordinal type "1er" 

    """
    ## On crée un dictionnaire qui va servir à mapper les jours de la semaine et leurs abréviations
    jours_fr_to_num = {
        'lundi': 1, 'mardi': 2, 'mercredi': 3, 'jeudi': 4,
        'vendredi': 5, 'samedi': 6, 'dimanche': 0,
        'lun': 1, 'mar': 2, 'mer': 3, 'jeu': 4,
        'ven': 5, 'sam': 6, 'dim': 0
    }

    ## idem avec les mois 
    mois_fr_to_num = {
        'Janvier': 1, 'Février': 2, 'Mars': 3, 'Avril': 4,
        'Mai': 5, 'Juin': 6, 'Juillet': 7, 'Août': 8,
        'Septembre': 9, 'Octobre': 10, 'Novembre': 11, 'Décembre': 12
    }

    ## on sépare la chaine de caractères du dataframe 
    jour, jour_num, mois, heure_str = date_str.split()

 
    jour_fr = jour.lower()
    jour_num = ''.join(char for char in jour_num if char.isdigit()) ## on gère l'exception des nombres au format ordinal 
    mois_num = mois_fr_to_num.get(mois.capitalize())

    ## ici on a besoin de rajouter l'année, on le fait à la main
    annee = 2023 if mois_num == 12 else 2024

    ## on peut désormais créer une chaîne au format ISO 8601
    iso_date_str = f"{jours_fr_to_num[jour_fr]} {jour_num} {mois_num:02d} {heure_str} {annee}"

    ## on peut dès lors la convertir en objet datetime
    date_obj = datetime.strptime(iso_date_str, "%w %d %m %Hh%M %Y")

    return date_obj


if __name__ == '__main__':
















