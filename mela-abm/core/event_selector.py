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


def event_selector(cell, cell_list):
    r = random.random()

    # cols = ['Name', 'Phenotype', 'Location', 'Time']
    cols = ['Phenotype', 'Location']

    chance_pro = 1.0
    chance_move = 0.0


    if r < chance_pro:
        # Proliferation will be attempted
        print('Pro')
        cell_out = proliferate.proliferation_attempt(cell, cell_list)
        
        out_needs_flip = cell_out.to_frame()
        out = out_needs_flip.T

    elif r < chance_pro + chance_move:
    # Movement will be attempted
        print('Move')
        # print(cell.shape)

        out_needs_flip = cell.to_frame()
        out = out_needs_flip.T
        
    
    else:
    # Nothing will happen to given cell

        out_needs_flip = cell.to_frame()
        out = out_needs_flip.T

    # print(out.shape)
    # print('Out', out)
    # print('Hit')
    
    return out

# event_selector(training_cell, cell_list)