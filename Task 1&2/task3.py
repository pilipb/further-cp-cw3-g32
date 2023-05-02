from possible_values import possible_values_combined
import copy

def possible_values_grid(grid, n_rows, n_cols):
	"""
	Parameters:
	--------------
	grid: list
		A list of lists representing a sudoku board
	n_rows: int
		The number of rows in each square
	n_cols: int
		The number of columns in each square
	row: int
		The row index of the cell to be filled
	column: int
		The column index of the cell to be filled
	"""
	grid_copy = grid 
	n = n_rows * n_cols
 
 #creating a list of lists of lists for the possible values in each square
	for i in range(n): 
		for j in range(n):
			if grid_copy[i][j] == 0:
				possible_values = possible_values_combined(grid_copy, n_rows, n_cols, i, j)
				grid_copy[i][j] = possible_values
	return grid_copy


test_grid_1 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]
test_grid_2 = [
		[1, 0, 0, 2],
		[0, 0, 1, 0],
		[0, 1, 0, 4],
		[0, 0, 0, 1]]

test_grid_3 = [
		[1,2,3,4],
		[3,4,1,2],
		[2,3,4,1],
		[4,1,2,0]]

print('possible values grid, grid 1', possible_values_grid(test_grid_1, 2, 3))
def empty_squares_dict(grid_copy, n_rows, n_cols):
	"""
	
	Parameters:
	--------------
	grid_copy: list
		A list of lists representing a sudoku board
	n_rows: int
		The number of rows in each square
	n_cols: int
		The number of columns in each square

	Returns:
	--------------
	empty_squares: dict
		A dictionary of the empty squares in the sudoku board and the possible values for each square

	"""
	n = n_rows * n_cols
	empty_squares = {}

	for i in range(n):
		for j in range(n):
			if type(grid_copy[i][j]) == list:
				empty_squares[(i,j)] = grid_copy[i][j]

	return empty_squares
print('empty squares dict, grid 1',empty_squares_dict(test_grid_1, 2, 3))


#function that will be called if there is only one possible value for a square
def single_possible_value(grid_copy, empty_squares_dict, row, column):
	grid_copy[row][column] = empty_squares_dict[(row,column)][0]
	del empty_squares_dict[(row,column)]
	return grid_copy, empty_squares_dict


def wavefront_propagation(grid_copy, empty_squares_dict, n_rows, n_cols):
	
	n = n_rows * n_cols
	for num_missing_values in range(2,n+1):
		pass	
	
	# PLAN:
	# possible_values_grid() is a very useful function, it will be the start point for this process and will dynamically be explored
	# Each instance of the wavefront will be an instance of a class (seen below)
	# Create a list that tracks class instances of the wavefront, this list is growing and shrinking constantly
	# The list will be called wavefront_list
	# This is an iterative process
	# Each iteration consists of (current thoughts):
	# 1. Look at the current grid (where empties are represented as a list of possibles), determine which cell has the smallest number of possible values (greater than 1)
	# 2. Create a new instance of the wavefront class, with the current grid, the latest step to get to this point, update the current grid to reflect the latest step (what values are now possible)
	# 3. Update the wavefront dictionary with the new instance. If the new instance has a cell with only one possible value, then fill in that value and remove the cell from the dictionary.
	# 4. If a cell has no possible values, then the wavefront is invalid and the previous step must be undone, and the step that led to that step must be removed from previous instance as we have deemed it invalid.
	# 5. If the wavefront is valid, then the next step is to look at the next cell with the smallest number of possible values (greater than 1) and repeat the process.
	

class WavefrontInstance():
	def __init__(self, grid, previous_step):
		self.original_grid = grid
		self.new_grid = copy.deepcopy(grid)
		self.previous_step = previous_step
		self.next_step = None
		self.feasible = True
		self.solved = False
	
	def update_grid(self):
		# Based off the original grid and the previous step, update the new grid, also check if the new grid is solved, if so then self.solved = True and the ideal path 
		# can be found by tracing the previous steps back to the original grid.
		pass

	def determine_feasability(self):
		# Determine if the new grid is feasible (if any cell has no possible values, then it is not feasible (self.feasible = False))
		pass

	def determine_next_step(self):
		# if self.feasible is false, next step is to undo the previous step (self.next_step = 'revert')
		# if self.feasible is true, next step is to look at the next cell with the smallest number of possible values (greater than 1) and repeat the process.
		# This will ne in the exact same format as self.previous_step so it can be passed into the next instance of the class
		pass

	def revert(self):
		# This method is only called if the previoius step was not feasible, it takes the current self.next_step, takes it out the self.new_grid.
		# Then determine_next_step() is called again, and the process repeats.
		# This means that if the revserion process has exhausted all possible steps at this level, it will revert to the previous instance of the class and undo that step.
		# This means it is also a depth first seach like recursive process, but it is iterative and the depth should be much lower than a recursive process.
		pass


# Outside of this class we'll have a list of instances of this class, and we'll update the list as we go along.
# If we make a class and the next step is to revert, then we'll remove the last instance from the list and update the previous instance to reflect the new grid (remove that as a possible value from the previous instance)
# This can be done using the self.next_step attribute of the class instance, we reach in and remove the next step from the grid as a possible value. 
# We may have to change the previous instance before deleting the current one (not sure)





	

	
	
	
	# """
	# Parameters:
	# --------------
	# grid_copy: list
	# 	A list of lists representing a sudoku board
	# empty_squares_dict: dict
	# 	A dictionary of the empty squares in the sudoku board and the possible values for each square

	# Returns:
	# --------------
	# grid_copy: list
	# 	A list of lists representing a sudoku board
	# """
	# for key in empty_squares_dict:
	# 	row = key[0]
	# 	column = key[1]
	# 	possible_values = empty_squares_dict[key]
	# 	for value in possible_values:
	# 		if value in grid_copy[row]:
	# 			grid_copy[row].remove(value)
	# 		for i in range(len(grid_copy)):
	# 			if value in grid_copy[i][column]:
	# 				grid_copy[i][column].remove(value)
	# return grid_copy
	
	