'''
Checks neighbours of desired cell to see what spaces are free
'''

import numpy as np

# import master_runner
# from master_runner import *
import parameters


def neighbour_search_2D(x, y, direction, cell_list):
    '''
    Inputs: 
    
    x , y: Integer values of location of cell

    direction: Direction to check for cell in
        1 north-west
        2 north
        3 north-east
        4 east
        5 south-east
        6 south
        7 south-west
        8 west

    cell_list: cell list to search
    '''
    x_min = parameters.x_min
    x_max = parameters.x_max
    y_min = parameters.y_min
    y_max = parameters.y_max

    edge_case = False

    if direction == 1:
        if x == x_min or y == y_max:
            edge_case = True
        else:
            search_x = x - 1
            search_y = y + 1

    if direction == 2:
        if y == y_max:
            edge_case = True
        else:
            search_x = x
            search_y = y + 1

    if direction == 3:
        if x == x_max or y == y_max:
            edge_case = True
        else:
            search_x = x + 1
            search_y = y + 1

    if direction == 4:
        if x == x_max:
            edge_case = True
        else:
            search_x = x + 1
            search_y = y 

    if direction == 5:
        if x == x_max or y == y_min:
            edge_case = True
        else:
            search_x = x + 1
            search_y = y - 1

    if direction == 6:
        if y == y_min:
            edge_case = True
        else:
            search_x = x 
            search_y = y - 1

    if direction == 7:
        if x == x_min or y == y_min:
            edge_case = True
        else:
            search_x = x - 1
            search_y = y - 1

    if direction == 8:
        if x == x_min:
            edge_case = True
        else:
            search_x = x - 1
            search_y = y
    
    

    if edge_case == True:
        cell_present = False
    else:
        search_string = f"[{search_x} {search_y}]"
        ## Tests if location exists return true or false
        cell_present = np.isin(cell_list['Location'], search_string).any()

    return cell_present