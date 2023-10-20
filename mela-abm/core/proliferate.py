'''
Cell attempts to proliferate
'''

import pandas as pd
import numpy as np
import random
import json 
from ast import literal_eval

from cell import Cell
import neighbours

def proliferation_attempt(cell, cell_list):
    # print(json.loads(cell[2].replace(' ',',')))
    x, y = json.loads(cell[2].replace(' ',','))

    # search_x = x 
    # search_y = y 
    # search_string = f"[{search_x} {search_y}]"
    # ## Tests if location exists return true or false
    # checker = np.isin(cell_list['Location'], search_string).any()

    location_array = np.full((1, 8), False)
    for i in range(8):
        direction = i + 1
        cell_present = neighbours.neighbour_search_2D(x,y,direction,cell_list)
        location_array[0,i] = cell_present
        print('Cell present', cell_present)

    print('Loc', location_array)
    pro_possible = np.asarray(location_array==True).nonzero()[1]
    print(pro_possible)
    print(len(pro_possible))

    if len(pro_possible) == 0:
        # Case for no possible proliferation target sites, then nothing happens
        new_cells = cell
    else:
        pro_choice = random.choice(pro_possible)

        new_cells = proliferative_update(cell, x,y, pro_choice)
    # cell = cell
    hi = 1
    return new_cells


def proliferative_update(cell, x,y, pro_choice):
    new_cells_df = pd.DataFrame()
    new_cells_df = new_cells_df.append(cell)
    new_cells = []
    new_cells = cell
    
    # cell_initial_locs = np.append(cell_initial_locs, selected_location, axis=0)
    x_loc = x + 1
    y_loc = y + 1
    if pro_choice == 1:
        x_loc = x - 1
        y_loc = y + 1
    if pro_choice == 2:
        x_loc = x
        y_loc = y + 1
    if pro_choice == 3:
        x_loc = x + 1
        y_loc = y + 1
    if pro_choice == 4:
        x_loc = x + 1
        y_loc = y
    if pro_choice == 5:
        x_loc = x + 1
        y_loc = y - 1
    if pro_choice == 6:
        x_loc = x
        y_loc = y - 1
    if pro_choice == 7:
        x_loc = x - 1
        y_loc = y - 1
    if pro_choice == 8:
        x_loc = x - 1
        y_loc = y

    selected_location = [x_loc,y_loc]
    phenotype = cell.Phenotype
    
    cell_adding = cell

    # Line below prints over cell not a problem as output is not affected but 
    # it is annoying
    cell_adding.loc[:].at['Location']= selected_location


    new_cells_df = new_cells_df.append(cell_adding)
    hi = 1

    return new_cells_df