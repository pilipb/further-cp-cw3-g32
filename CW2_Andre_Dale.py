import copy
import time
import random

#Grids 1-5 are 2x2
grid1 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]

grid2 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 0, 4],
		[3, 4, 2, 1]]

grid3 = [
		[1, 0, 4, 2],
		[4, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid4 = [
		[1, 0, 4, 2],
		[0, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid5 = [
		[1, 0, 0, 2],
		[0, 0, 1, 0],
		[0, 1, 0, 4],
		[0, 0, 0, 1]]

grid6 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''
def check_section(section, n):

	if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n+1)]):
		return True
	return False


def get_squares(grid, n_rows, n_cols):

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


	return(squares)


def check_solution(grid, n_rows, n_cols):
	'''
	This function is used to check whether a sudoku board has been correctly solved

	args: grid - representation of a suduko board as a nested list.
	returns: True (correct solution) or False (incorrect solution)
	'''
	n = n_rows*n_cols

	for row in grid:
		if check_section(row, n) == False:
			return False

	for i in range(n_rows):
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


def next_empty(grid, n_rows=2, n_cols=2):
    """
    Finds the coordinates of the next empty cell in the given grid.

    Args:
    - grid: a nested list representing the Sudoku grid
    - n_rows: the number of rows in each block of the Sudoku grid (default: 2)
    - n_cols: the number of columns in each block of the Sudoku grid (default: 2)

    Returns:
    A tuple of the form (row, col), representing the coordinates of the next empty cell in the grid.
    If there are no empty cells, returns (None, None).
    """
    
    n = n_rows * n_cols

    # Loops through all the coordinates of the grid to find the next empty cell
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 0: # If cell is empty, return its coordinates
                return row, col

    # If no empty cells are found, return None, None
    return None, None 


def guess_valid(grid, guess, row, col, n_rows = 2, n_cols = 2):
    """
    Determines whether a given guess is a valid move in the Sudoku grid at the specified position.

    Args:
    - grid: a nested list representing the Sudoku grid
    - guess: the integer value being guessed at the specified position
    - row: the row index of the position being guessed
    - col: the column index of the position being guessed
    - n_rows: the number of rows in each block of the Sudoku grid (default: 2)
    - n_cols: the number of columns in each block of the Sudoku grid (default: 2)

    Returns:
    True if the guess is a valid move, i.e., if it does not violate the Sudoku rules by repeating
    the same value in the same row, column, or subgrid; False otherwise.
    """
    
    n = n_rows * n_cols

    # Check if guess is in the existing row
    if guess in grid[row]:
        return False

    # Check column
    if guess in [grid[i][col] for i in range(n)]:
        return False

    # Identify the start of the square
    row_start = (row // n_rows) * n_rows
    col_start = (col // n_cols) * n_cols

    # Iterate over each coordinate in each square and return false if element found twice
    for x in range(row_start, row_start + n_rows):
        for y in range(col_start, col_start + n_cols):
            if grid[x][y] == guess:
                return False

    return True


def recursive_solve(grid, n_rows = 2, n_cols = 2):
    """
    This function solves a partially solved Sudoku board using backtracking.
    - grid: a nested list representing the Sudoku grid
    - n_rows: number of rows in a subgrid.
    - n_cols: number of columns in a subgrid.
    
    Returns:
    - grid: Solved Sudoku board as a nested list if there is a solution

    Raises:
    - Exception: If no valid solutions are found
    """
    # Find empty and locate it's coordinates
    row, col = next_empty(grid, n_rows, n_cols)

    # If there's no empty cells return the grid
    if row is None:  
        return grid 
    
    # If there's an empty cell trial all possible numbers
    for guess in range(1, n_rows * n_cols + 1):
        
		# Check if the guess is valid, changing the empty cell to the guess if it is valid
        if guess_valid(grid, guess, row, col, n_rows, n_cols):
            grid[row][col] = guess
            
			# Recursively call the solver
            if recursive_solve(grid, n_rows, n_cols):
                return grid
        
        # If the solution is not valid, or subsequent trials are incorrect reset the value
		# and reiterate. 
        grid[row][col] = 0

    # Raise error if no solutions to the suduko board
    raise Exception("No valid solutions")


def replace_zeros(grid):
    """
    Replaces all zeroes in a 2D grid with a random integer between 1 and 4 (inclusive).

    Args:
        grid: A 2D grid represented as a list of lists of integers.

    Returns:
        grid_copy: A new 2D grid with all zeroes replaced by random integers.
    """
    
    grid_copy = [row.copy() for row in grid]  # make a copy of the original grid

    for i in range(len(grid_copy)):
        for j in range(len(grid_copy[i])):
            if grid_copy[i][j] == 0:
                grid_copy[i][j] = random.randint(1, 4)
    
    return grid_copy
        

def random_solve(grid, n_rows = 2, n_cols = 2, max_tries = 500):
    """
    Replaces all zeroes in a 2D grid with a random integer between 1 and 4 (inclusive).

    Args:
        grid: A 2D grid represented as a list of lists of integers.

    Returns:
        grid_trial: A new 2D grid with all zeroes replaced by random integers.

	Raises:
        Exception: If no valid solutions are found after the specified number of tries.
    """

    for i in range(max_tries):
        grid_trial = replace_zeros(grid)
        if check_solution(grid_trial, n_rows, n_cols) == True:
            return grid_trial
	
    raise Exception("No valid solutions found after the number of trials")


def solve(grid, n_rows, n_cols):

	'''
	Solve function for Sudoku coursework.
	Comment out one of the lines below to either use the random or recursive solver
	'''
	
	#return random_solve(grid, n_rows, n_cols)
	return recursive_solve(grid, n_rows, n_cols)


# Print solutions
for grid in range(len(grids)):
    print(solve(grids[grid][0], grids[grid][1], grids[grid][2]))


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''
""" #def main():

	points = 0

	print("Running test script for coursework 1")
	print("====================================")
	
	for (i, (grid, n_rows, n_cols)) in enumerate(grids):
		print("Solving grid: %d" % (i+1))
		start_time = time.time()
		solution = solve(grid, n_rows, n_cols)
		elapsed_time = time.time() - start_time
		print("Solved in: %f seconds" % elapsed_time)
		print(solution)
		if check_solution(solution, n_rows, n_cols):
			print("grid %d correct" % (i+1))
			points = points + 10
		else:
			print("grid %d incorrect" % (i+1))

	print("====================================")
	print("Test script complete, Total points: %d" % points)


#if __name__ == "__main__":
	main() """
