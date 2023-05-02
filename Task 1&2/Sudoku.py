# Let's integrage code from Task 1 and Task 2 into a class called Sudoku:
from modules import *
from hint import *
from explain import explain
import copy
import time
import numpy as np
class Sudoku():
    def __init__(self, grid, n_rows, n_cols, hint_flag, hint_number,profile_flag,explain_flag):
        self.grid = grid
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n = n_rows * n_cols
        # Make a copy of the original grid 
        # Just assigning it to grid will make it a reference to the original grid
        # This means that if we change the grid, we will also change the original_grid
        self.original_grid = copy.deepcopy(grid)
        self.hint_grid = copy.deepcopy(grid)
        self.hint_flag = hint_flag
        self.hint_number = hint_number
        self.profile_flag = profile_flag
        self.explain_flag = explain_flag
        self.solved = False
        self.filled_in = None
        self.time_taken = None
        self.solve_method = None
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

    def recursion(self):
        """
        This method runs the recursive_solve function from modules.py
        If it manages to solve the grid, it sets the solved flag to True
        """ 
        # Call the recursive_solve function from modules.py to solve the grid
        self.grid, self.iterations = recursive_solve(self.grid, self.n_rows, self.n_cols, self.iterations)
        # Check if the grid is solved, if it is, set the solved flag to True
        self.solved = check_solution(self.grid, self.n_rows, self.n_cols)

    def solve(self):
        """
        This method combines the quick_solve and recursion methods to form the solve method
        """
        # Start the timer
        start = time.time()
        # Attempt to solve the grid using the quick_solve method
        self.quick_solve()
        if self.solved:
            self.solve_method = "Quick Solve"
            self.filled_in = find_filled(self.original_grid, self.grid)
        # If the grid is not solved, attempt to solve it using the recursion method
        else:
            self.recursion()
            self.solve_method = "Recursion"
            if self.solved:
                # If the grid is solved, get the filled in grid instructions
                self.filled_in = find_filled(self.original_grid, self.grid)
            else:
                raise Exception("No solution exists for this grid: " + str(np.array(self.grid)))
        # At this point, the grid should be solved so we can stop the timer 
        # If it isnt solved, a solution does not exist
        end = time.time()
        self.time_taken = end - start

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
        self.hint_grid, self.hints, self.hint_number = make_hint(self.hint_grid, self.filled_in, self.hint_number)






"""

grid9 = [[9,0,0,5,0,4,0,1,0],
         [4,0,0,0,0,9,6,0,3],
         [8,1,6,2,7,0,0,0,0],
         [0,0,5,6,8,0,7,0,0],
         [1,0,0,0,3,0,4,5,2],
         [0,9,7,0,0,2,0,0,1],
         [6,3,0,7,0,0,5,9,0],
         [0,0,9,1,4,0,3,0,0],
         [5,2,0,0,0,6,0,8,7]]


def main():
    instance = Sudoku(grid9, 3, 3,hint_flag = True, hint_number = 5)
    quicksolve,grid = instance.quick_solve()
    if quicksolve:
        print("Quick solve worked")
    else:
        print("Moving to recursion")
        grid, iterations = instance.recursion()
        print("Recursion took {} iterations".format(iterations))
    print(grid)
    instance.hint_class()
    instance.explain_class()
    print(np.array(instance.hint_grid))









if __name__ == "__main__":
    main()



"""
















        