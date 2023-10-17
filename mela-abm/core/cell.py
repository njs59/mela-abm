#
# Cell Class
#

import numpy as np
import random


class Cell:
    """Class to represent each cell in a simulation.

    Parameters
    ----------

    Attributes
    ----------
    phenotype:
    phenotype of the cell

    location:
    location of the cell
    """

    def __init__(self, phenotype, location):
        """Constructor Method.

        Parameters
        ----------
        phenotype: Boolean
        True for invasive false for proliferative

        location:
        coordinates for cell location
        """

        self.phenotype = phenotype
        self.location = location

        # self.set_initial_phenotype(self.chance_of_invasive)

        
    def __repr__(self):
        """Returns a string representation of Cell.

        Returns
        -------
        str
            String representation of cell

        """
        return f"Cell, Phenotype = {self.phenotype}, Location = {self.location}."

    def set_initial_phenotype(self, chance_of_invasive):
        """Set Cell's initial phenotype

        Parameters
        ----------
        chance_of_invasion : float (between 0 and 1)
            Chance of a cell being invasive 

        """
        if chance_of_invasive > 1 or chance_of_invasive < 0:
            print('Chance for cell phenotype must be between 0 and 1')

        else:
            r = random.random() 
            if r < chance_of_invasive:
                self.phenotype = "Invasive"
            else:
                self.phenotype = "Proliferative"

        return self.phenotype


    def set_initial_location(self, avaliable_spaces):
        """Gives an initial location to the cell from a 
        list of avaliable positions

        Parameters
        ----------
        avaliable_spaces : numpy array
            List of avaliable spaces for a cell

        Returns
        --------
        avaliable_spaces: numpy array
            List of avaliable spaces after cell has been assigned a location

        """

        # Select random number between 0 and 1 to give rndom location
        r = random.random()
        # print('Avaliable spaces', avaliable_spaces)
        num_space = np.shape(avaliable_spaces)
        spaces = num_space[0]
        chance_of_loc = 1/num_space[0]
        r_compare = chance_of_loc
        cell_loc = 0
        for j in range(spaces):
            if r < r_compare:
                # Cell location found
                selected_location = avaliable_spaces[[cell_loc],:]
                avaliable_spaces = np.delete(avaliable_spaces, cell_loc, 0)
                break

            else:
                r_compare += chance_of_loc
                cell_loc += 1

        # print('Avaliable spaces after', avaliable_spaces)

        return avaliable_spaces, selected_location
