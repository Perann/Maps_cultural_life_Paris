import pandas as pd
from international_scrap import get_international_data
from caveau_scrap import get_caveau_datas
from belleville_scrap import get_belleville_data

df_inter = get_international_data()
df_caveau = get_caveau_datas()
df_belleville = get_belleville_data()


global_df = pd.concat([df_inter, df_caveau, df_belleville], ignore_index = True)

global_df.to_csv('DataBarsMusicaux.csv', index = False)


  