import pandas as pd
ref = pd.read_csv('Python_2A\Cinema\ListeCinema(MairieDeParis).csv', sep = ';')

ref.rename(columns={'nom': 'etablissement'}, inplace=True)

print(ref.keys())
