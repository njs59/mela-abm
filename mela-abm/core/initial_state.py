import numpy as np
import random

from cell import Cell
from domain import Domain

avaliable_spaces = Domain.create_uniform_2D_grid(0, 10, 11, 0, 10, 11)
num_space = np.shape(avaliable_spaces)
# print('Domain', avaliable_spaces)
print('Number of spaces', num_space[1])

initial_number_cells = 117

cell_list = []
for i in range(initial_number_cells):
    # creating list
    chance_of_invasive = 0.5
    new_cell = Cell(False,[0,0])
    avaliable_spaces, selected_location = new_cell.set_initial_location(avaliable_spaces)
    phenotype = new_cell.set_initial_phenotype(chance_of_invasive)
    # appending instances to list
    cell_list.append(Cell(phenotype, selected_location))
    
    # print('Domain', avaliable_spaces)
    print('Selected Location', selected_location)

print('Domain', avaliable_spaces)
print('Cells', cell_list)

# for i in range(initial_number_cells):
#     print('Cell ',Cell(i).__repr__())