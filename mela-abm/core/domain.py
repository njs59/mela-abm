import numpy as np


class Domain:
    def __init__():
            """Constructor method.
            Parameters
            ----------
            loc : Tuple[float, float]
                (x,y) coordinates of the place
            place_type : 'PlaceType' enum
                Categorises the place
            cell : Cell
                An instance of :class:`Cell`
            microcell : Microcell
                An instance of :class:`Microcell`

            """

    def __repr__(self):
        """Returns a string representation of Place.

        Returns
        -------
        str
            String representation of place

        """
        return ("Domain")

    def create_uniform_1D_grid(low, high, no_steps):
        """Define a uniformly-spaced grid that can be used to discretize a space.

        Parameters
        ----------
        low : float
        Lower bounds for each dimension of the continuous space.
        high : float
        Upper bounds for each dimension of the continuous space.
        no_steps : int
        Number of steps in the given dimension

        Returns
        -------
        grid_1D : list of array_like
        A list of arrays containing split points for each dimension.
        """
        grid_1D = np.linspace(low, high, no_steps)

        return [grid_1D]

    def create_uniform_2D_grid(low_x, high_x, no_steps_x, low_y, high_y, no_steps_y):
        """Define a uniformly-spaced grid that can be used to discretize a 2D space.

        Parameters
        ----------
        low_x, low_y : array_like
        Lower bounds for each dimension of the continuous space.
        high_x, high_y : array_like
        Upper bounds for each dimension of the continuous space.
        no_steps_x, no_steps_y : int
        Number of steps in the given dimension

        Returns
        -------
        grid_2D : list of array_like
        A list of arrays containing split points for each dimension.
        """
        grid_x = np.linspace(low_x, high_x, no_steps_x)
        grid_y = np.linspace(low_y, high_y, no_steps_y)

        
        for i in range(no_steps_x):
             for j in range(no_steps_y):
                  if i==0 and j==0:
                       grid_2D = np.array([grid_x[i], grid_y[j]])
                  else:
                    row_to_add = [grid_x[i], grid_y[j]]
                    grid_2D = np.vstack([grid_2D, [row_to_add]])

        return grid_2D

    def create_uniform_3D_grid(low_x, high_x, no_steps_x, low_y, high_y, no_steps_y, low_z, high_z, no_steps_z):
        """Define a uniformly-spaced grid that can be used to discretize a 2D space.

        Parameters
        ----------
        low_x, low_y, low_z : array_like
        Lower bounds for each dimension of the continuous space.
        high_x, high_y, low_z : array_like
        Upper bounds for each dimension of the continuous space.
        no_steps_x, no_steps_y, low_z : int
        Number of steps in the given dimension

        Returns
        -------
        grid_3D : list of array_like
        A list of arrays containing split points for each dimension.
        """
        grid_x = np.linspace(low_x, high_x, no_steps_x)
        grid_y = np.linspace(low_y, high_y, no_steps_y)
        grid_z = np.linspace(low_z, high_z, no_steps_z)

        grid_3D = [grid_x, grid_y, grid_z]

        return [grid_3D]