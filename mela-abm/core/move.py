'''
Cell attempts to move
'''

import pandas as pd
import numpy as np
import random

def movement_attempt(cell, cell_list, grid_2D):
    # print(json.loads(cell[2].replace(' ',',')))
    # x, y = json.loads(cell["Location"].replace(' ',','))
    [x, y] = cell["Location"]

    grid_shape = np.shape(grid_2D)
    x_min = 0
    x_max = grid_shape[0] - 1
    y_min = 0
    y_max = grid_shape[1] - 1

    ## Choose direction to attempt to move, N, E, S, W
    r_direction = random.random()
    
    random_direction = int(4 * r_direction)

    if random_direction == 0:
        ## North
        print('North')
        if y == y_min:
            ## At northern edge so movement fails
            out_needs_flip = cell.to_frame()
            new_cells = out_needs_flip.T
            grid_2D_new = grid_2D
            print('N fail 1')

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
                print('N fail 2')

            else:
                ## Add daughter cell to target location
                new_cells = movement_comparison(cell, target_x,target_y, grid_2D)
                grid_2D[target_x][target_y] = 1
                grid_2D[x][y] = 0
                grid_2D_new = grid_2D
                print('N success')

    elif random_direction == 1:
        ## East
        print('East')
        if x == x_max:
            ## At eastern edge so proliferation fails
            out_needs_flip = cell.to_frame()
            new_cells = out_needs_flip.T
            grid_2D_new = grid_2D
            print('E fail 1')

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
                print('E fail 2')

            else:
                ## Add daughter cell to target location
                new_cells = movement_comparison(cell, target_x,target_y, grid_2D)
                grid_2D[target_x][target_y] = 1
                grid_2D[x][y] = 0
                grid_2D_new = grid_2D
                print('E success')

    elif random_direction == 2:
        ## South
        print('South')
        if y == y_max:
            ## At southern edge so proliferation fails
            out_needs_flip = cell.to_frame()
            new_cells = out_needs_flip.T
            grid_2D_new = grid_2D
            print('S fail 1')

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
                print('S fail 2')

            else:
                ## Add daughter cell to target location
                new_cells = movement_comparison(cell, target_x,target_y, grid_2D)
                grid_2D[target_x][target_y] = 1
                grid_2D[x][y] = 0
                grid_2D_new = grid_2D
                print('S success')

    elif random_direction == 3:
        ## West
        print('West')
        if x == x_min:
            ## At western edge so proliferation fails
            out_needs_flip = cell.to_frame()
            new_cells = out_needs_flip.T
            grid_2D_new = grid_2D
            print('W fail 1')

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
                print('W fail 2')

            else:
                ## Add daughter cell to target location
                new_cells = movement_comparison(cell, target_x,target_y, grid_2D)
                grid_2D[target_x][target_y] = 1
                grid_2D[x][y] = 0
                grid_2D_new = grid_2D
                print('W success')

    return new_cells, grid_2D_new



def movement_comparison(cell, target_x, target_y, grid_2D):
    '''
    Compares current and target location for a cell and 
     places the cell in the location with more neighbours
    If both locations have the same number of neighbours
     then the cell still moves
    '''
    new_cells_df = pd.DataFrame()

    [x, y] = cell["Location"]

    neighbours_before = neighbours_value(x,y,grid_2D)
    neighbours_after = neighbours_value(target_x,target_y,grid_2D)

    if neighbours_before > neighbours_after:
       # Do nothing
        new_cells_df = new_cells_df.append(cell) 

    else:
        # move the cell
        selected_location = [target_x, target_y]
        phenotype = cell.Phenotype
        cell_adding = cell

        # Line below prints over cell not a problem as output is not affected but 
        # it is annoying
        cell_adding.loc[:].at['Location']= selected_location
        new_cells_df = new_cells_df.append(cell_adding)

    return new_cells_df


def neighbours_value(x,y, grid_2D):
    '''
    Returns current number of neighbours of a location (x,y)
    '''
    grid_shape = np.shape(grid_2D)
    x_min = 0
    x_max = grid_shape[0] - 1
    y_min = 0
    y_max = grid_shape[1] - 1

    neighbours_count = 0
    if y != y_max:
        neighbours_count += grid_2D[x][y+1]
    if x != x_max:
        neighbours_count += grid_2D[x+1][y]
    if y != 0:
        neighbours_count += grid_2D[x][y-1]
    if x != 0:
        neighbours_count += grid_2D[x-1][y]

    return neighbours_count