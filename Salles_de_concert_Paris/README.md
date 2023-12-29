# Scrapping of Classical music concerts 

- Here you will find how we scrapped the l'officiel des spectacles website to generate a database of all classical music concerts from December 2023 onwards.


## 1. Website scrapping 

- In the section ***1. scrap du site*** the file ***OfficielSpectaclesConcertsScrap.py*** generates a the database by scrapping pages of this link https://www.offi.fr/concerts/programme.html?criterion_sch_ville=75&criterion_SRubrique=classique
- The module ***ScrapMusiqueClassic.py*** contains the function that is used to scrap each page of the website


## 2. Database cleaning 

- In the section ***2. nettoyage de la database*** We make several changes to the database in the script ***ModificationsDatabase.py*** using the module ***Fonctions.py*** to enable us to manipulate the data more easily and create a map displaying all the concerts for a specific day.
- We first add the geo-coordinatees of the concert halls that we retrieve from the https://api-adresse.data.gouv.fr/search/
- We make minor changes to the price column to obtain an average tariff on each concert (unfoiortunately there is a lot of missing data) 
- We convert the date of the concerts to the datetime format


## 3. Mapping 

- In the ***2. mapping*** section of the ***mappingclassic.py*** file, we define a function that creates an html map displaying the location and time of concerts available on the day entered by the user
- an example of such a map is available in the file ***Classicmap_example_14.01.2023.html***