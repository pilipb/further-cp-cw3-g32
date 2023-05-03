'''
Profiler script for the project.

This script will run through the various solver methods and time them using SnakeViz.

'''

import cProfile
import pstats
import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
import snakeviz
from task3 import SudokuSolver



# Import the solver methods
test_grid_1 = [
    [1, 0, 0, 2],
    [0, 0, 1, 0],
    [0, 1, 0, 4],
    [0, 0, 0, 1]]

grid8 = [[0,0,0,0,0,0,0,0,1],
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

# firstly make a grid
#grid_ex = SudokuGrid(test_grid_1, 2, 3)

# import it into the solver class
solver = SudokuSolver(grid6, 2, 3)

cp = cProfile.Profile()
cp.enable()

# solve using wavefront propagation
solved_obj = solver.wavefront_solve()

cp.disable()

# print the stats
cp.print_stats()

# print the solved grid
solved_obj.pprint()


