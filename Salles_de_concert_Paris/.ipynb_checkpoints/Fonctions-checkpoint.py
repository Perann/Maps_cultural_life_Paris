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


