import pandas as pd
from international_scrap import get_international_data
from caveau_scrap import get_caveau_datas


df_inter = get_international_data()
df_caveau = get_caveau_datas()


df_final = pd.concat([df_inter, df_caveau], ignore_index = True)

df_final.to_csv('DataBarsMusicaux.csv', index = False)
