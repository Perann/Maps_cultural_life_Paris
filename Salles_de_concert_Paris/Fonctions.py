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


###################################################

from datetime import datetime

def convertir_en_datetime_old(date_str):
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


def convertir_en_datetime(date_str):
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

    # Utilisation d'une expression régulière pour extraire les composants de la date
    match = re.match(r'(?P<jour>1er|\d{1,2})\s(?P<mois>\w+)\s(?P<annee>\d{4})\s(?P<heure>\d{2}h\d{2})', date_str)
    
    if match:
        jour_numero = match.group('jour')
        mois_fr = match.group('mois')
        mois_en = mois_fr_to_en.get(mois_fr)
        annee = match.group('annee')
        heure = match.group('heure')
        
        date_str = f'{jour_numero} {mois_en} {annee} {heure}'
        
        # Utilisation du format flexible pour prendre en compte "1er"
        date_time_obj = datetime.strptime(date_str, '%d %B %Y %Hh%M')
        return date_time_obj.date(), date_time_obj.time()

    # Si la date ne correspond pas au format attendu, retourner None
    return None, None


#############################################


### fonction création date début date fin ###

import dateparser

def extract_dates(date_string):
    if isinstance(date_string, str):
        match = re.search(r'Du (\d+ \w+ \d+) au (\d+ \w+ \d+)', date_string)
        if match:
            start_date_str, end_date_str = match.groups()

            start_date = dateparser.parse(start_date_str)
            end_date = dateparser.parse(end_date_str)

            return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')
        else:
            matches_single_date = re.findall(r'Le (\d+ \w+ \d+)', date_string)
            if matches_single_date:
                single_date = dateparser.parse(matches_single_date[0])
                return single_date.strftime('%Y-%m-%d'), single_date.strftime('%Y-%m-%d')
            else:
                return None, None
    else:
        return None, None
