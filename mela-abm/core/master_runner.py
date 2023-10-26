'''
Main script to run
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import initial_state
import event_selector
import parameters

## Parameters to change
# global x_min, x_max, y_min, y_max
# x_min = 0
# x_max = 10
# y_min = 0
# y_max = 10
x_min = parameters.x_min
x_max = parameters.x_max
y_min = parameters.y_min
y_max = parameters.y_max

initial_number_cells = 5
timesteps = 5000

## Initialise

cells_current, grid_2D = initial_state.initialise_2D(initial_number_cells, x_min,x_max,y_min,y_max)

## Loop over event selector for each cell at each timestep

# cells_current = pd.read_csv('initial_2D.csv')  

cols = ['Phenotype', 'Location']

# Declare a list that is to be converted into a column
count_row = cells_current.shape[0]

timestep_current = 0

current_time = np.full((count_row,1), timestep_current)
 
# Using 'Address' as the column name
# and equating it to the list
cells_current['Time'] = current_time

cells_current

cell_output = cells_current


## Main loop
for i in range (timesteps):
    timestep_current += 1

    ## Shuffle the dataframe in order to get random order to cycle over cells
    if i == 0:
        cells_current = cells_current.sample(frac = 1)
    else:
        cells_current = cells_after.sample(frac = 1)

    cells_to_loop = cells_current.shape[0]

    cells_current['new_col'] = range(1, cells_to_loop + 1)
    ## Apply changes calls here
    
    # Event selector
    for j in range(cells_to_loop):

        # Remove cell of interest before event
        cell_to_compare = cells_current.iloc[0,:]
        list_for_step = cells_current.drop(cells_current[cells_current.new_col==j+1].index)
        post_event, grid_2D_after = event_selector.event_selector(cell_to_compare, list_for_step, grid_2D)
        post_event_row_ongoing = post_event.shape[0]

        cells_current = pd.concat([list_for_step, post_event])

    cells_new = cells_current
    count_new_row = cells_current.shape[0]
    current_time = np.full((count_new_row,1), timestep_current)
    cells_new['Time'] = current_time
    # cell_output.concat(cells_current)
    cells_after = pd.DataFrame(cells_new, columns=cols)

    cells_current = cells_after

    if timestep_current % 100 == 0:
        cell_output = pd.concat([cell_output, cells_new])
        plt.imshow(grid_2D_after, interpolation='none')
        plt.show()




# cell_output.append(cells_current)

cell_output.to_csv('output_2D.csv', index=True, header=True)
plt.imshow(grid_2D_after, interpolation='none')
plt.show()
