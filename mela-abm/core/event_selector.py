'''
Select which event out of proliferate, move or do nothing that a cell will attempt to do
'''

import random

import move
import proliferate


training_cell = "Cell, Phenotype = Proliferative, Location = [[8. 0.]]."
training_cell_list = "Cell, Phenotype = Proliferative, Location = [[8. 0.]].," +\
"Cell, Phenotype = Proliferative, Location = [[8. 1.]]."


def event_selector(cell, cell_list):
    r = random.random()

    chance_pro = 0.01
    chance_move = 0.8


    if r < chance_pro:
        # Proliferation will be attempted
        proliferation_attempt(cell, cell_list)
        print('Pro')

    elif r < chance_pro + chance_move:
    # Movement will be attempted
        print('Move')
    
    else:
    # NOting will happen to given cell


    out=1
    return out

event_selector(training_cell, cell_list)