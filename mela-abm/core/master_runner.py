'''
Main script to run
'''

import numpy as np
import pandas as pd

import initial_state

## Parameters to change
xmin = 0
xmax = 10
ymin = 0
ymax = 10
initial_number_cells = 90
timesteps = 3

## Initialise

initial_state.initialise_2D(initial_number_cells, xmin,xmax,ymin,ymax)

## Loop over event selector for each cell at each timestep

cells_current = pd.read_csv('initial_2D.csv')  

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
    cells_current = cells_current.sample(frac = 1)

    ## Apply changes calls here


    current_time = np.full((count_row,1), timestep_current)
    cells_current['Time'] = current_time
    # cell_output.concat(cells_current)
    cell_output = pd.concat([cell_output, cells_current])

# cell_output.append(cells_current)

cell_output.to_csv('output_2D.csv', index=True, header=True)