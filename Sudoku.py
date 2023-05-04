# Let's integrage code from Task 1 and Task 2 into a class called Sudoku:
from modules import *
from hint import *
from explain import explain
import copy
import time
import numpy as np
from modules import check_solution
from grids import grids
import time


class Sudoku():
    def __init__(self, grid, n_rows, n_cols, hint_flag, hint_number, profile_flag, explain_flag, solve_method = None):

        '''
        The sudoku class is used to solve a sudoku puzzle using the chosen method

        Parameters
        -------------
        grid: list
            The grid to be solved
        n_rows: int
            The number of rows in the grid
        n_cols: int
            The number of columns in the grid
        hint_flag: bool
            Whether or not to use hints
        hint_number: int
            The number of hints to use
        profile_flag: bool
            Whether or not to use profiling
        explain_flag: bool
            Whether or not to use the explain function
        solve_method: str
            The method to use to solve the puzzle
            'quick' - quick_solve
            'recursion' - recursion_solve
            'wavefront' - wavefront_solve
            'overall' - overall_solve


        Returns
        -------------
        None

        
        Examples
        -------------
        # create a solvable 4x4 grid
        >>> grid =  [[1, 0, 0, 2],
                    [0, 0, 1, 0],
                    [0, 1, 0, 4],
                    [0, 0, 0, 1]]
        >>> n_rows = 2
        >>> n_cols = 2
        >>> hint_flag = False
        >>> hint_number = 1
        >>> profile_flag = False
        >>> explain_flag = False
        >>> solve_method = 'overall'
        >>> sudoku = Sudoku(grid, n_rows, n_cols, hint_flag, hint_number, profile_flag, explain_flag)
        >>> sudoku.solve_sudoku(solve_method)
        >>> print(sudoku.grid)
        
        '''

        self.grid = grid
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n = n_rows * n_cols
        # Make a copy of the original grid 
        # Just assigning it to grid will make it a reference to the original grid
        # This means that if we change the grid, we will also change the original_grid
        self.original_grid = copy.deepcopy(grid)

        self.calc_zeros()
        
        self.recursive_grid = copy.deepcopy(grid)
        self.wavefront_grid = copy.deepcopy(grid)
        self.overall_grid = copy.deepcopy(grid)
        self.hint_grid = copy.deepcopy(grid)

        
        self.hint_flag = hint_flag
        self.hint_number = hint_number
        self.profile_flag = profile_flag
        self.explain_flag = explain_flag
        self.solve_method = solve_method
        self.solved = False
        self.filled_in = None

        # Profiling variables
        self.time_taken_recursion = None
        self.time_taken_wavefront = None
        self.time_taken_quick = None
        self.time_taken_overall = None

        self.avg_time_recursion = None
        self.avg_time_wavefront = None
        self.avg_time_quick = None
        self.avg_time_overall = None

        self.iterations = 0
        self.hints = None

    def calc_zeros(self):
        zero_counter  = sum([row.count(0) for row in self.original_grid])
        self.zero_counter = zero_counter

    
    def solve_sudoku(self, solve_method):

        '''
        This method will automatically solve the sudoku puzzle using the chosen method

        Parameters
        -------------
        self: object
            The object that the method is being called from


        Returns
        -------------
        None

        '''
        # set the solve method attribute
        self.solve_method = solve_method

        if solve_method == 'quick':
            self.quick_solve()
        elif solve_method == 'recursion':
            self.recursion_solve()
        elif solve_method == 'wavefront':
            self.wavefront_solve()
        elif solve_method == 'overall':
            self.overall_solve()
        else:
            raise ValueError('Please enter a valid solve method on initialisation of class')
        

    def quick_solve(self):
        """
        This method runs the quick_fill function from modules.py
        If it manages to solve the grid, it sets the solved flag to True
        """
        # Keep filling in the grid until it stops changing
        timein = time.time()
        while True:
            self.old_grid = self.grid
            self.grid = quick_fill(self.grid, self.n_rows, self.n_cols)
            if self.grid == self.old_grid:
                break
        # Check if the grid is solved, if it is, set the solved flag to True
        if check_solution(self.grid, self.n_rows, self.n_cols):
            self.solved = True

        self.time_taken_quick = time.time() - timein

    def recursion_solve(self):
        """
        This method runs the recursive_solve function from modules.py
        If it manages to solve the grid, it sets the solved flag to True
        """ 
        # Call the recursive_solve function from modules.py to solve the grid
        timein = time.time()
        self.recursive_grid, self.iterations = recursive_solve(self.recursive_grid, self.n_rows, self.n_cols, self.iterations)
        
        # Check if the grid is solved, if it is, set the solved flag to True
        self.solved = check_solution(self.recursive_grid, self.n_rows, self.n_cols)

        if self.solved:
            # set recursive grid to grid
            self.grid = self.recursive_grid

        self.time_taken_recursion = time.time() - timein


    def overall_solve(self):
        """
        This method combines the quick_solve and recursion methods to form the solve method

        """
        # Attempt to solve the grid using the quick_solve method
        timein = time.time()
        self.quick_solve()
        if self.solved:
            self.filled_in = find_filled(self.original_grid, self.grid)
        # If the grid is not solved, attempt to solve it using the recursion method
        else:
            self.recursion_solve()
            if self.solved:
                # If the grid is solved, get the filled in grid instructions
                self.filled_in = find_filled(self.original_grid, self.grid)
            else:
                raise Exception("No solution exists for this grid: " + str(np.array(self.grid)))
            
        self.time_taken_overall = time.time() - timein

    def explain_class(self):
        """
        This runs the explain function from explain.py, but only if the grid has been solved.
        This method should only be run after a solve attempt has been made anyway, so this should be fine.
        It will only be run anyways if the -explain flag is set to True 
        """
        # Get the hints if they have not already been made (So the explain function knows what instructions to use)
        if self.hint_flag:    
            explain(self.hints, self.hint_flag, self.profile_flag, self.avg_time_recursion, self.avg_time_wavefront, self.avg_time_overall)
        else:
            # If the hints are not being used, just use the filled in grid
            explain(self.filled_in, self.hint_flag, self.profile_flag, self.avg_time_recursion, self.avg_time_wavefront, self.avg_time_overall)


    def hint_class(self):
        """
        This runs the hint function from hint.py, but only if the grid has been solved.
        This method should only be run after a solve attempt has been made anyway, so this should be fine.
        It will only be run anyways if the -hint flag is set to True
        """
        # Call the hint function from hint.py to create the hint grid and hit instructions
        self.hint_grid, self.hints, self.hint_number = make_hint(self.hint_grid, self.filled_in, self.hint_number)


    def wavefront_solve(self):
        '''
        The wavefront solver is a method of solving sudoku puzzles that is based on the wavefront algorithm.

        When called the wavefront solver will attempt to solve the sudoku puzzle by filling in the cells that have only one possible value.
        If the wavefront solver cannot solve the puzzle by filling in the cells with only one possible value, it will then attempt to 
        fill in the cells with the least possible values.

        Parameters
        -------------
        self : object
            The object that the method is being called from


        Returns
        -------------
        None

        Updates document
        
        
        
        '''
        start = time.time()
        work_grid = self.wavefront_grid
        frontier = []
    
        while not self.solved:

            lists = []

            # loop through the grid and find the cells with only one possible value
            for row in range(self.n):
                for col in range(self.n):
                    possible_vals = possible_values_combined(work_grid, self.n_rows, self.n_cols, row, col)
                    if isinstance(possible_vals , list):
                        lists.append([row,col,possible_vals])
                    
            # sort the list of cells with only one possible value by the number of possible values
            lists.sort(key=lambda x: len(x[2]))

            # if the possible values list is > 0, put in the first value and add it to the frontier list
            if len(lists[0][2]) > 0:

                # extract the row and column of the cell that is being filled in
                row = lists[0][0]
                col = lists[0][1]

                # fill in the cell
                work_grid[row][col] = lists[0][2][0]

                # add the cell to the frontier list
                frontier.append(lists[0])

            # if there are no possible values, backtrack
            else: 

                # backtrack until the last cell has more than one possible value
                while len(frontier[-1][2]) == 1:

                    row = frontier[-1][0]
                    col = frontier[-1][1]

                    # replace the last changed cell with 0 and remove it from the frontier list
                    work_grid[row][col] = 0
                    frontier.pop()

                # remove the last possible value from the last cell in the frontier list
                del frontier[-1][2][0]

                # add the last cell in the frontier list to the grid
                row = frontier[-1][0]
                col = frontier[-1][1]
                work_grid[row][col] = frontier[-1][2][0]



            if check_solution(work_grid, self.n_rows, self.n_cols):
                # set self.grid to the solved grid, for the purpose of the profile method
                self.grid = work_grid
                self.wavefront_grid = work_grid
                self.solved = True
                self.filled_in = find_filled(self.original_grid, self.grid)
                break

        end = time.time()
        self.time_taken_wavefront = end - start


    def profile(self):
        ''' 
        This method is used to profile the code. It will run the solve method 100 times and then print the average time taken to solve the grid.
        This method is only called if the -profile flag is set to True.

        Each time each method is run, its self.time_taken_method variable is updated. Storing this value after each run can help find the average run time
        of each method.

        The method will be tested for all the grids in grids.py with each method and grid combination being tested 100 times. The average time taken for each
        method will be stored in a dictionary. This dictionary will then be used to create a pandas dataframe which will be printed to the console.


        Parameters
        -------------
        self : object
            The object that the method is being called from


        Returns
        -------------
        None

        Updates document

        '''
        import pandas as pd
        import matplotlib.pyplot as plt

        # Create a dict to store the methods that are being profiled
        methods = [ 'recursion', 'wavefront', 'overall']

        # loop through the methods
        for method in methods:

            # Create a list to store the times taken for each method
            times = []

            # loop through the method 25 times
            for _ in range(25):

                # run the method
                self.solve_sudoku(method)

                # extract the time taken from the self.time_taken_'method' variable
                val = getattr(self, 'time_taken_' + method)

                # append the time taken to the times list
                if val is None or val == 0:
                    times.append(0)
                else:
                    times.append(val)

            # average the times for each method for that grid
            average_time = sum(times)/len(times)
            # append the average time to the average times list
            if method == 'recursion':
                recursion_times = average_time
            elif method == 'wavefront':
                wavefront_times = average_time
            elif method == 'overall':
                overall_times = average_time
            
        # store as avg_time attributes
        self.avg_time_recursion = recursion_times
        self.avg_time_wavefront = wavefront_times
        self.avg_time_overall = overall_times





################ TEST CODE ################


if __name__ == '__main__':

    # Create a grid to test the class

    test_grid_1 = [
    [1, 0, 0, 2],
    [0, 0, 1, 0],
    [0, 1, 0, 4],
    [0, 0, 0, 1]]

    grid8 = [
    [0,0,0,0,0,0,0,0,1],
    [5,0,0,0,9,0,0,0,6],
    [0,0,0,4,0,0,3,8,0],
    [0,0,5,0,0,0,0,0,0],
    [0,1,0,0,2,0,7,0,0],
    [2,0,0,0,3,0,0,0,5],
    [6,9,0,0,0,8,0,0,0],
    [0,0,0,0,0,0,8,0,0],
    [0,0,7,0,0,0,0,5,0]]

    grid6 = [
    [0, 0, 6, 0, 0, 3],
    [5, 0, 0, 0, 0, 0],
    [0, 1, 3, 4, 0, 0],
    [0, 0, 0, 0, 0, 6],
    [0, 0, 1, 0, 0, 0],
    [0, 5, 0, 0, 6, 4]]

    # test profiler

    # initialise the class
    test = Sudoku(grid=grid8, n_rows=3, n_cols=3, hint_flag=False, hint_number=0, profile_flag=False, explain_flag=False)

    # run the profiler
    test.solve_sudoku('wavefront')
    test.profile()

    # print the results
    print(test.avg_time_wavefront)
   










        