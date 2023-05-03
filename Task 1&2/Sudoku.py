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

        self.grid = grid
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n = n_rows * n_cols
        # Make a copy of the original grid 
        # Just assigning it to grid will make it a reference to the original grid
        # This means that if we change the grid, we will also change the original_grid
        self.original_grid = copy.deepcopy(grid)
        self.work_grid = copy.deepcopy(grid)
        self.hint_grid = copy.deepcopy(grid)
        self.hint_flag = hint_flag
        self.hint_number = hint_number
        self.profile_flag = profile_flag
        self.explain_flag = explain_flag
        self.solve_method = solve_method
        self.solved = False
        self.filled_in = None
        self.time_taken = None
        self.iterations = 0
        self.hints = None
        self.zero_counter = sum([row.count(0) for row in self.grid])

    def quick_solve(self):
        """
        This methtod runs the quick_solve function from modules.py
        If it manages to solve the grid, it sets the solved flag to True (Not sure what this is for yet)
        Current grid and solved boolean are returned, but this may change
        """
        # Keep filling in the grid until it stops changing
        while True:
            self.old_grid = self.grid
            self.grid = quick_fill(self.grid, self.n_rows, self.n_cols)
            if self.grid == self.old_grid:
                break
        # Check if the grid is solved, if it is, set the solved flag to True
        if check_solution(self.grid, self.n_rows, self.n_cols):
            self.solved = True

    def recursion_solve(self):
        """
        This method runs the recursive_solve function from modules.py
        If it manages to solve the grid, it sets the solved flag to True
        """ 
        # Call the recursive_solve function from modules.py to solve the grid
        self.grid, self.iterations = recursive_solve(self.grid, self.n_rows, self.n_cols, self.iterations)
        # Check if the grid is solved, if it is, set the solved flag to True
        self.solved = check_solution(self.grid, self.n_rows, self.n_cols)


    def overall_solve(self):
        """
        This method combines the quick_solve and recursion methods to form the solve method

        """
        # Attempt to solve the grid using the quick_solve method
        self.quick_solve()
        if self.solved:
            self.solve_method = "Quick Solve"
            self.filled_in = find_filled(self.original_grid, self.grid)
        # If the grid is not solved, attempt to solve it using the recursion method
        else:
            self.recursion_solve()
            self.solve_method = "Recursion"
            if self.solved:
                # If the grid is solved, get the filled in grid instructions
                self.filled_in = find_filled(self.original_grid, self.grid)
            else:
                raise Exception("No solution exists for this grid: " + str(np.array(self.grid)))
        # At this point, the grid should be solved so we can stop the timer 
        # If it isnt solved, a solution does not exist



    def explain_class(self):
        """
        This runs the explain function from explain.py, but only if the grid has been solved.
        This method should only be run after a solve attempt has been made anyway, so this should be fine.
        It will only be run anyways if the -explain flag is set to True 
        """
        # Get the hints if they have not already been made (So the explain function knows what instructions to use)
        if self.hint_flag:
            if self.hints == None:
                self.hint_class()
            explain(self.hints, self.hint_flag, self.profile_flag, self.time_taken, self.solve_method, self.iterations)
        else:
            # If the hints are not being used, just use the filled in grid
            explain(self.filled_in, self.hint_flag, self.profile_flag, self.time_taken, self.solve_method, self.iterations)


    def hint_class(self):
        """
        This runs the hint function from hint.py, but only if the grid has been solved.
        This method should only be run after a solve attempt has been made anyway, so this should be fine.
        It will only be run anyways if the -hint flag is set to True
        """
        # Call the hint function from hint.py to create the hint grid and hit instructions
        print(self.hint_grid)
        print(self.filled_in)
        print(self.hint_number)
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
        work_grid = self.work_grid
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
                # set self.grid to the solved grid
                self.grid = work_grid
                self.solved = True
                self.filled_in = find_filled(self.original_grid, self.grid)
                break
        end = time.time()
        self.time_taken = end - start



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

    # initialise the class
    for grid in grids:
        test_wf = Sudoku(grid = grid[0], n_rows = grid[1], n_cols= grid[2], hint_flag = False, hint_number = False, profile_flag = False, explain_flag = False, solve_method = None)
        print('------------------')
        print('Wavefront Solver')
        start = time.time()
        test_wf.wavefront_solve()
        end = time.time()
        print('Correct Solution:', check_solution(test_wf.grid, test_wf.n_rows, test_wf.n_cols))
        print('Time Taken:', end - start)
        print('Recursive Solver:')
        test_r = Sudoku(grid = grid[0], n_rows = grid[1], n_cols= grid[2], hint_flag = False, hint_number = False, profile_flag = False, explain_flag = False, solve_method = 'recursive')
        start = time.time()
        test_r.recursion_solve()
        end = time.time()
        print('Correct Solution:', check_solution(test_r.grid, test_r.n_rows, test_r.n_cols))
        print('Time Taken:', end - start)
    # test.solve()

    # print the solved grid
        











        