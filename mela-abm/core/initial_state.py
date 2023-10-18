import numpy as np
import pandas as pd
import random

from cell import Cell
from domain import Domain

def initialise_2D(initial_number_cells, xmin,xmax,ymin,ymax):

    avaliable_spaces = Domain.create_uniform_2D_grid(xmin, xmax, ymin, ymax)
    num_space = np.shape(avaliable_spaces)
    # print('Domain', avaliable_spaces)
    print('Number of spaces', num_space[1])

    # initial_number_cells = 117

    cols = ['Phenotype', 'Location']
    cells = pd.DataFrame(columns=cols)

    cell_list = []
    cell_initial_locs = [[0,0]]
    cell_phenotypes = []
    for i in range(initial_number_cells):
        # creating list
        chance_of_invasive = 0.5
        new_cell = Cell(False,[0,0])
        avaliable_spaces, selected_location = new_cell.set_initial_location(avaliable_spaces)
        phenotype = new_cell.set_initial_phenotype(chance_of_invasive)

        cell_phenotypes = np.append(cell_phenotypes, phenotype)
        # appending instances to list
        cell_list.append(Cell(phenotype, selected_location))
        print(selected_location)
        if i == 0:
            cell_initial_locs = selected_location
        else:
            cell_initial_locs = np.append(cell_initial_locs, selected_location, axis=0)


    list_of_tuples = list(zip(cell_phenotypes, cell_initial_locs))
    cells_after = pd.DataFrame(list_of_tuples, columns=cols)
    cells_after
    cells_after.to_csv('initial_2D.csv', index=True, header=True)
