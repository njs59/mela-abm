'''
Cell attempts to proliferate
'''

import pandas as pd
import numpy as np

from ast import literal_eval

def proliferation_attempt(cell, cell_list):
    print(cell[2])
    location = np.array(cell[2])
    location_split = location.split('.')
    print('Loc', location)
    print('Type', type(cell[2]))
    print('Type 2', location_split)
    location_1 = location + 1
    filtered_df = cell_list.loc[cell_list['loc'].str.contains('J')]

    print(filtered_df)

    return cell