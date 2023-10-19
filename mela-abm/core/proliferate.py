'''
Cell attempts to proliferate
'''

import pandas as pd
import numpy as np
import json 
from ast import literal_eval

def proliferation_attempt(cell, cell_list):
    print(json.loads(cell[2].replace(' ',',')))
    x, y = json.loads(cell[2].replace(' ',','))

    search_x = x 
    search_y = y 
    search_string = f"[{search_x} {search_y}]"
    ## Tests if location exists return true or false
    checker = np.isin(cell_list['Location'], search_string).any()
    
    location = np.array(cell[2])
    location_split = location.split('.')
    print('Loc', location)
    print('Type', type(cell[2]))
    print('Type 2', location_split)
    location_1 = location + 1
    filtered_df = cell_list.loc[cell_list['loc'].str.contains('J')]

    print(filtered_df)

    return cell