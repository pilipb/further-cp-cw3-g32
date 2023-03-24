'''
This file contains the functions that are used to check whether a sudoku board has been correctly solved,
and the functions required to solve a sudoku board using recursion and random solving.

'''

# imports
import random
import copy
import time
from possible_values import possible_values_combined
from hint import find_filled

def quick_fill(grid, n_rows, n_cols):
	'''
	If there are squares with only one possible value, fill them in and return the grid
	
	Parameters:
	--------------
	grid: list
		A list of lists representing a sudoku board
	n_rows: int
		The number of rows in each square
	n_cols: int
		The number of columns in each square

	Returns:
	--------------
    grid: list
	  	A grid with the (some) squares filled in
	
    '''
    # initialise the list of squares that have been filled in
	filled_in = []
	
	for row_index,row in enumerate(grid):
		for col_index,col in enumerate(row):
			if grid[row_index][col_index] == 0:
				possible_values = list(possible_values_combined(grid, n_rows, n_cols, row_index, col_index))
				if possible_values != None and len(possible_values) == 1:
					grid[row_index][col_index] = possible_values[0]


	return grid


def check_section(section, n):
	'''
    This function is used to check whether a section of a sudoku board has been correctly solved

    Parameters:
    --------------
    section: list
        A list of integers representing a row, column or square of a sudoku board
    n: int
        The maximum integer considered in this board
	
    Returns:
    --------------
    True (correct solution) or False (incorrect solution)
	
    '''


	if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n+1)]):
		return True
	return False

def get_squares(grid, n_rows, n_cols):
	
    '''
    This function is used to get the squares of a sudoku board

    Parameters:
    --------------
    grid: list
        A list of lists representing a sudoku board
    n_rows: int
        The number of rows in each square
    n_cols: int
        The number of columns in each square
	
    Returns:
    --------------
    squares: list
        A list of lists representing the squares of the sudoku board

    '''
    squares = []
    
    for i in range(n_cols):
        rows = (i*n_rows, (i+1)*n_rows)
        for j in range(n_rows):
            cols = (j*n_cols, (j+1)*n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square +=line
            squares.append(square)


    return squares


def check_solution(grid, n_rows, n_cols):
	'''
	This function is used to check whether a sudoku board has been correctly solved

	Parameters:
	--------------
	grid: list  
        A list of lists representing a sudoku board
	n_rows: int
        The number of rows in each square
    n_cols: int
        The number of columns in each square
	
	Returns:
	--------------
	True (correct solution) or False (incorrect solution)
	
	'''
	n = n_rows*n_cols

	for row in grid:
		if check_section(row, n) == False:
			return False

	for i in range(n_rows**2):
		column = []
		for row in grid:
			column.append(row[i])

		if check_section(column, n) == False:
			return False

	squares = get_squares(grid, n_rows, n_cols)
	for square in squares:
		if check_section(square, n) == False:
			return False

	return True


def find_empty(grid,n_rows,n_cols):
	'''
	This function returns the index (i, j) to the first zero element in a sudoku grid
	If no such element is found, it returns None

	Parameters:
	--------------
	grid: list
        A list of lists representing a sudoku board
	
    Returns:
    --------------
    (i, j): tuple
        (i, j) or None

	'''
	# Initialize the minimum number of available values to the length of the grid - this is the maximum possible value for this variable
	min_available = len(grid)
	# Iterate through the grid, when a zero is found, check how many possible values it has
    # If it has fewer than the current minimum, update the minimum and the index of the minimum
	for i in range(len(grid)):
		row = grid[i]
		for j in range(len(row)):
			if grid[i][j] == 0:
				available = len(possible_values_combined(grid, n_rows, n_cols, i, j))
				if available < min_available:
					min_available = available
					min_index = (i,j)
	if min_available == len(grid):
		return None
	return min_index



def recursive_solve(grid, n_rows, n_cols, iterations):
	'''
	This function uses recursion to exhaustively search all possible solutions to a grid
	until the solution is found

	Parameters:
	--------------
	grid: list
        A list of lists representing a sudoku board 
	n_rows: int
        The number of rows in each square
    n_cols: int
        The number of columns in each square
	
	Returns:
	--------------
	ans: list or None
	    A solved grid (as a nested list), or None if no solution is found
	
	'''

	#Find an empty place in the grid
	empty = find_empty(grid,n_rows,n_cols)

	#If there's no empty places left, check if we've found a solution
	if not empty:
		#If the solution is correct, return it.
		if check_solution(grid, n_rows, n_cols):
			return grid, iterations
		else:
			#If the solution is incorrect, return None
			return None, iterations
	else:
		row, col = empty 

	#Loop through possible values
	for i in possible_values_combined(grid, n_rows, n_cols, row, col):

			#Place the value into the grid
			grid[row][col] = i
			#Recursively solve the grid
			ans, iterations = recursive_solve(grid, n_rows, n_cols, iterations+1)
			#If we've found a solution, return it
			if ans:
				return ans, iterations

			#If we couldn't find a solution, that must mean this value is incorrect.
			#Reset the grid for the next iteration of the loop
			grid[row][col] = 0 

	#If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
	return None, iterations

def random_solve(grid, n_rows, n_cols, max_tries=50000):
	'''
	This function uses random trial and error to solve a Sudoku grid

	Parameters:
	--------------
	grid: list
        A list of lists representing a sudoku board
	n_rows: int
        The number of rows in each square
    n_cols: int
        The number of columns in each square
	max_tries: int
        The maximum number of random trials to try before giving up
	
	Returns:
	--------------
	grid: list
        A solved grid (as a nested list)
	
	'''

	for i in range(max_tries):
		possible_solution = fill_board_randomly(grid, n_rows, n_cols)
		if check_solution(possible_solution, n_rows, n_cols):
			return possible_solution

	return grid

def fill_board_randomly(grid, n_rows, n_cols):
	'''
	This function will fill an unsolved Sudoku grid with random numbers

	Parameters:
	--------------
	grid: list
        A list of lists representing a sudoku board
	n_rows: int
        The number of rows in each square
    n_cols: int
        The number of columns in each square
	
	Returns:
	--------------
	filled_grid: list
        A grid with random numbers filled in
	

	'''
	n = n_rows*n_cols
	#Make a copy of the original grid
	filled_grid = copy.deepcopy(grid)

	#Loop through the rows
	for i in range(len(grid)):
		#Loop through the columns
		for j in range(len(grid[0])):
			#If we find a zero, fill it in with a random integer
			if grid[i][j] == 0:
				filled_grid[i][j] = random.randint(1, n)

	return filled_grid 

def solve(grid, n_rows, n_cols):

	'''
	Solve function for Sudoku coursework.
	Comment out one of the lines below to either use the random or recursive solver
	
	Parameters:
	--------------
	grid: list
        A list of lists representing a sudoku board
	n_rows: int
        The number of rows in each square
    n_cols: int
        The number of columns in each square
	
	Returns:
	--------------
	grid: list
        A solved grid (as a nested list)
	filled_in: list
		A list of the filled in values and their indices [value, row, column]
	
	'''
	iterations = 1
	# intialise the list of filled in values
	filled_in = []

	# initialise a copy of the grid for comparison
	original_grid = copy.deepcopy(grid)

	while True:
		old_grid = grid 
		grid  = quick_fill(grid, n_rows, n_cols)
		if grid == old_grid:
			break

	if check_solution(grid, n_rows, n_cols):
		print("Quick fill solution found")

	else:
		print("Quick solution not found, recursive solver starting")
		grid, iterations = recursive_solve(grid, n_rows, n_cols, iterations)

	print(grid)
	print("Number of iterations: ", iterations)
	filled_in = find_filled(original_grid, grid)

	return grid, filled_in, iterations

