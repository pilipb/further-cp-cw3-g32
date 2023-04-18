import numpy as np
from possible_values import possible_values


class TestClass:
    # this class will initialise a solution grid for sudoku grid inputted

    # this function will initialise the solution grid
    def __init__(self, grid):
        # the grid input will be nested list size n x m
        self.grid = grid
        
        # the solution grid will be a numpy array size n x m with a list 1-9 at each index
        self.solution = np.array([[list(range(1, 10)) for i in range(len(grid[0]))] for j in range(len(grid))])

        # firstly go through the input grid and at the corresponding index in the solution grid, leave only the number that is in the input grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    self.solution[i][j] = [grid[i][j]]

        
    def attempt_solve(self):
        # the function will apply the rules of sudoku to the solution grid and remove numbers that are not possible from the list at each index

        # first rule: if a number is in a row, column or box, it cannot be in the same row, column or box
        
        # call possible_values.py to get the possible values for each index
        pass

