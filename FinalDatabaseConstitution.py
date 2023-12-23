import pandas as pd 
DataCinema = pd.read_csv('Python_2A\Cinema\DataCinema.csv')
DataCinema['Type activite'] = ['Cinema']*DataCinema.shape[0]

DataBarsMusicaux = pd.read_csv('Python_2A\BarsMusicaux\DataBarsMusicaux.csv')
DataBarsMusicaux['Type activite'] = ['Spectacles bars musicaux']*DataBarsMusicaux.shape[0]

df_to_concat = [DataCinema,DataBarsMusicaux]

CulturalLifeProg = pd.concat(df_to_concat, ignore_index =  True )

CulturalLifeProg.to_csv('Python_2A\DayProg.csv', encoding = 'utf-8')