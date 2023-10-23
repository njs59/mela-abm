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

    def create_uniform_1D_grid(low, high):
        """Define a uniformly-spaced grid that can be used to discretize a space.

        Parameters
        ----------
        low : int
        Lower bounds for each dimension of the continuous space.
        high : int
        Upper bounds for each dimension of the continuous space.

        Returns
        -------
        grid_1D : list of array_like
        A list of arrays containing split points for each dimension.
        """
        steps = high - low + 1
        grid_1D = np.linspace(low, high, steps)

        return [grid_1D]

    def create_uniform_2D_grid(low_x, high_x, low_y, high_y):
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
        avaliable_locations : list of array_like
        A list of arrays containing split points for each dimension.

        grid_2D: array of zeros of size of grid
        """

        grid_x = range(low_x, high_x + 1)
        grid_y = range(low_y, high_y + 1)

        
        for i in grid_x:
             for j in grid_y:
                  if i==0 and j==0:
                       avaliable_locations = np.array([grid_x[i], grid_y[j]])
                  else:
                    row_to_add = [grid_x[i], grid_y[j]]
                    avaliable_locations = np.vstack([avaliable_locations, [row_to_add]])


        grid_2D = np.zeros((high_x - low_x + 1, high_y - low_y +1))

        return avaliable_locations, grid_2D

    def create_uniform_3D_grid(low_x, high_x, low_y, high_y, low_z, high_z):
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
        steps_x = high_x - low_x + 1
        steps_y = high_y - low_y + 1
        steps_z = high_z - low_z + 1

        grid_x = np.linspace(low_x, high_x, steps_x)
        grid_y = np.linspace(low_y, high_y, steps_y)
        grid_z = np.linspace(low_z, high_z, steps_z)


        
        for i in range(steps_x):
             for j in range(steps_y):
                  for k in range(steps_z):
                    if i==0 and j==0 and k==0:
                       grid_3D = np.array([grid_x[i], grid_y[j]])
                    else:
                        row_to_add = [grid_x[i], grid_y[j], grid_z[k]]
                        grid_3D = np.vstack([grid_3D, [row_to_add]])

        return grid_3D