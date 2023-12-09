import re
import numpy as np

month_set = set('janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout','septembre', 'octobre', 'novembre', 'décembre')
month_dictionnary = {month: k for month,k  in month_set, np.arrange(1,12)}

def date_uniform(string):
    pass

