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

def convertir_en_datetime(date_str):
    """
    Prend en argument une date selon le format de la database et le convertit en un tuple date et une heure exploitables en format datetime

    """
    liste = date_str.split()
    liste.remove(':')
    
    mois_fr_to_en = {
        'Janvier': 'January',
        'Février': 'February',
        'Mars': 'March',
        'Avril': 'April',
        'Mai': 'May',
        'Juin': 'June',
        'Juillet': 'July',
        'Août': 'August',
        'Septembre': 'September',
        'Octobre': 'October',
        'Novembre': 'November',
        'Décembre': 'December'
    }

 
    jour, jour_numero, mois_fr, heure = liste


    mois_en = mois_fr_to_en[mois_fr]

    date_str = f'{jour_numero} {mois_en} 2023 {heure}'
    date_time_obj = datetime.strptime(date_str, '%d %B %Y %Hh%M')
    return date_time_obj.date(), date_time_obj.time()


