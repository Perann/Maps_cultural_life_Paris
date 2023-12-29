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
    # Dictionnaire pour mapper les noms des jours de la semaine en français aux numéros de jours
    jours_fr_to_num = {
        'lundi': 1, 'mardi': 2, 'mercredi': 3, 'jeudi': 4,
        'vendredi': 5, 'samedi': 6, 'dimanche': 0,
        'lun': 1, 'mar': 2, 'mer': 3, 'jeu': 4,
        'ven': 5, 'sam': 6, 'dim': 0
    }

    # Dictionnaire pour mapper les noms des mois en français aux numéros de mois
    mois_fr_to_num = {
        'Janvier': 1, 'Février': 2, 'Mars': 3, 'Avril': 4,
        'Mai': 5, 'Juin': 6, 'Juillet': 7, 'Août': 8,
        'Septembre': 9, 'Octobre': 10, 'Novembre': 11, 'Décembre': 12
    }

    # Séparation de la chaîne en composants
    jour, jour_num, mois, heure_str = date_str.split()

    # Conversion du jour de la semaine en français (en minuscules)
    jour_fr = jour.lower()

    jour_num = ''.join(char for char in jour_num if char.isdigit())

    # Conversion du mois en numéro
    mois_num = mois_fr_to_num.get(mois.capitalize(), 1)

    # Détermination de l'année en fonction du mois
    annee = 2023 if mois_num == 12 else 2024

    # Création de la chaîne au format ISO 8601
    iso_date_str = f"{jours_fr_to_num[jour_fr]} {jour_num} {mois_num:02d} {heure_str} {annee}"

    # Analyse de la chaîne pour créer un objet datetime
    date_obj = datetime.strptime(iso_date_str, "%w %d %m %Hh%M %Y")

    return date_obj
















