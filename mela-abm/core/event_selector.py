'''
Select which event out of proliferate, move or do nothing that a cell will attempt to do
'''

import pandas as pd
import random

import move
import proliferate


training_cell = "Cell, Phenotype = Proliferative, Location = [[8. 0.]]."
training_cell_list = "Cell, Phenotype = Proliferative, Location = [[8. 0.]].," +\
"Cell, Phenotype = Proliferative, Location = [[8. 1.]]."


def event_selector(cell, grid_2D):
    r = random.random()

    # cols = ['Name', 'Phenotype', 'Location', 'Time']
    cols = ['Phenotype', 'Location']

    chance_pro = 0.01
    chance_move = 0.99


    if r < chance_pro:
        # Proliferation will be attempted
        # print('Pro')
        cell_out, grid_2D_new = proliferate.proliferation_attempt(cell, grid_2D)




    elif r < chance_pro + chance_move:
    # Movement will be attempted
        # print('Move')
        cell_out, grid_2D_new = move.movement_attempt(cell, grid_2D)


        out_needs_flip = cell.to_frame()
        cell_out = out_needs_flip.T
        
    
    else:
    # Nothing will happen to given cell

        out_needs_flip = cell.to_frame()
        cell_out = out_needs_flip.T
        grid_2D_new = grid_2D

    # print(out.shape)
    # print('Out', out)
    # print('Hit')
    
    return cell_out, grid_2D_new

# event_selector(training_cell, cell_list)