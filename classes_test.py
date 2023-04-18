import numpy as np
from possible_values import possible_values_combined


class propagationClass:
    '''
    This class will initialise a solution grid for sudoku grid inputted. It will replace all zeros in the input grid 
    with a list of possible values for that index. It will then apply the rules of sudoku to the solution grid and
    remove numbers that are not possible from the list at each index.

    Parameters
    ----------
    grid: list
        A list of lists representing the grid.
    n_rows: int
        The number of rows in the grid.
    n_cols: int
        The number of columns in the grid.

    Methods
    -------
    propagation()
        Applies the rules of sudoku to the solution grid and removes numbers that are not 
        possible from the list at each index.

    
    '''

    # constructor
    def __init__(self, grid,n_rows,n_cols):

        # the grid input will be nested list size n x m
        self.grid = grid
        self.n_rows = n_rows
        self.n_cols = n_cols 

        # the solution grid will be a numpy array size n x m 
        self.solution_grid = np.array(grid)

        # with all zeros from the input grid replaced with a list of possible values as found by possible_values.py
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    self.solution_grid[i][j] = possible_values_combined(grid, n_rows, n_cols, i, j) 

              
    # methods
    def propagation(self):
        '''
        This will look for lists of length 1 in the solution grid and replace the zero in the input grid with the
        value in the list. It will then apply the rules of sudoku to the solution grid and remove numbers that are not
        possible from the list at each index. 

        Parameters
        ----------
        Self

        
        Returns
        ----------
        solution_grid: numpy array
            An updated numpy array of the solution grid.

        '''


        pass

