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

def proliferation_attempt(cell, grid_2D):
    # print(json.loads(cell[2].replace(' ',',')))
    # x, y = json.loads(cell["Location"].replace(' ',','))
    [x, y] = cell["Location"]
    # print('Pro')

    grid_shape = np.shape(grid_2D)
    x_min = 0
    x_max = grid_shape[0] - 1
    y_min = 0
    y_max = grid_shape[1] - 1

    ## Choose direction to attempt to proliferate, N, E, S, W
    r_direction = random.random()
    
    random_direction = int(4 * r_direction)

    if random_direction == 0:
        ## North
        # print('North')
        if y == y_min:
            ## At northern edge so proliferation fails
            out_needs_flip = cell.to_frame()
            new_cells = out_needs_flip.T
            grid_2D_new = grid_2D
            # print('N fail 1')

        else:
            ## Find target coordinates
            target_x = x
            target_y = y - 1

            ## Check if target location is populated
            if grid_2D[target_x][target_y] == 1:
                ## Target location already populated
                out_needs_flip = cell.to_frame()
                new_cells = out_needs_flip.T
                grid_2D_new = grid_2D
                # print('N fail 2')

            else:
                ## Add daughter cell to target location
                new_cells = proliferative_update(cell, target_x,target_y)
                grid_2D[target_x][target_y] = 1
                grid_2D_new = grid_2D
                # print('N success')

    elif random_direction == 1:
        ## East
        # print('East')
        if x == x_max:
            ## At eastern edge so proliferation fails
            out_needs_flip = cell.to_frame()
            new_cells = out_needs_flip.T
            grid_2D_new = grid_2D
            # print('E fail 1')

        else:
            ## Find target coordinates
            target_x = x + 1
            target_y = y

            ## Check if target location is populated
            if grid_2D[target_x][target_y] == 1:
                ## Target location already populated
                out_needs_flip = cell.to_frame()
                new_cells = out_needs_flip.T
                grid_2D_new = grid_2D
                # print('E fail 2')

            else:
                ## Add daughter cell to target location
                new_cells = proliferative_update(cell, target_x,target_y)
                grid_2D[target_x][target_y] = 1
                grid_2D_new = grid_2D
                # print('E success')

    elif random_direction == 2:
        ## South
        # print('South')
        if y == y_max:
            ## At southern edge so proliferation fails
            out_needs_flip = cell.to_frame()
            new_cells = out_needs_flip.T
            grid_2D_new = grid_2D
            # print('S fail 1')

        else:
            ## Find target coordinates
            target_x = x
            target_y = y + 1

            ## Check if target location is populated
            if grid_2D[target_x][target_y] == 1:
                ## Target location already populated
                out_needs_flip = cell.to_frame()
                new_cells = out_needs_flip.T
                grid_2D_new = grid_2D
                # print('S fail 2')

            else:
                ## Add daughter cell to target location
                new_cells = proliferative_update(cell, target_x,target_y)
                grid_2D[target_x][target_y] = 1
                grid_2D_new = grid_2D
                # print('S success')

    elif random_direction == 3:
        ## West
        # print('West')
        if x == x_min:
            ## At western edge so proliferation fails
            out_needs_flip = cell.to_frame()
            new_cells = out_needs_flip.T
            grid_2D_new = grid_2D
            # print('W fail 1')

        else:
            ## Find target coordinates
            target_x = x - 1
            target_y = y

            ## Check if target location is populated
            if grid_2D[target_x][target_y] == 1:
                ## Target location already populated
                out_needs_flip = cell.to_frame()
                new_cells = out_needs_flip.T
                grid_2D_new = grid_2D
                # print('W fail 2')

            else:
                ## Add daughter cell to target location
                new_cells = proliferative_update(cell, target_x,target_y)
                grid_2D[target_x][target_y] = 1
                grid_2D_new = grid_2D
                # print('W success')


    # location_array = np.full((1, 8), False)
    # for i in range(8):
    #     direction = i + 1
    #     cell_present = neighbours.neighbour_search_2D(x,y,direction,cell_list)
    #     location_array[0,i] = cell_present
    #     # print('Cell present', cell_present)

    # print('Loc', location_array)
    # pro_possible = np.asarray(location_array==True).nonzero()[1]
    # print(pro_possible)
    # print(len(pro_possible))

    # if len(pro_possible) == 0:
    #     # Case for no possible proliferation target sites, then nothing happens
    #     new_cells = pd.DataFrame()
    #     new_cells = new_cells.append(cell)
    # else:
    #     # Select a direction to attempt to proliferate in 
    #     attempted_direction = random.randint(1, 8)

    #     # If there is a space in that direction then proliferation occurs
    #     if attempted_direction in pro_possible:        
    #         pro_choice = random.choice(pro_possible)
    #         new_cells = proliferative_update(cell, x,y, pro_choice)

    #     # No space to proliferate so nothing happens
    #     else:
    #         new_cells = pd.DataFrame()
    #         new_cells = new_cells.append(cell)

    return new_cells, grid_2D_new


def proliferative_update(cell, target_x, target_y):
    ## Adds daughter cell of same phenotype to a defined target location
    new_cells_df = pd.DataFrame()
    # new_cells_df = new_cells_df.append(cell)
    new_cells_df = pd.concat([new_cells_df, cell])

    selected_location = [target_x, target_y]
    phenotype = cell.Phenotype
    
    cell_adding = cell

    # Line below prints over cell not a problem as output is not affected but 
    # it is annoying
    cell_adding.loc[:].at['Location']= selected_location


    # new_cells_df = new_cells_df.append(cell_adding)
    new_cells_df = pd.concat([new_cells_df, cell_adding], axis=1)

    new_cells_df_out = new_cells_df.T

    return new_cells_df_out