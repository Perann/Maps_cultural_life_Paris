The main problem with the csv file DataTheatre is that the data are uncleaned: the adress cannot be used to create a map, prices are either in a range or unique or unkwon, and the same goes for the dates.
This section aims at cleaning those data and create a final data base that will be used to generate our final map for theatres


1- First and the more difficult part was to clean the column 'dates' in which we had a text under the format "Du DD/MM/YYYY au DD/MM/YYYY" or "Le DD/MM/YYYY". Our code 'Dates_triees" translate this text in two dates saved in two columns "date début" et "date fin" that stock the beginn e   b e g i nd of the show, we saved this in a new csv file name "datatheatre_dates"


2- We took the "datatheatre_dates" csv file, clean the column 'prix' to create a final column named 'prix moyen' in wich you have an idea of the price you will have to pay to attend the play. We used the code named "PrixMoyen" and saved this information in a new csv file named 'DataTheatre_dates_prix'


3- From this new csv file, we ended in tranlating addresses in coordinates. The final csv file with cleaned columns is named "dataTheatre_base_final". You will also find this base in the section Outputs/database.


To run the different codes, you will need to use the following modules: 
import pandas as pd
import re
import dateparser
import requests