from possible_values import possible_values_combined
import copy
import numpy as np



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





# function that will be called if there is only one possible value for a square
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
	


class SudokuSolver():

	def __init__(self, grid, n_rows, n_cols):
		'''
		1. make the possible values grid
		2. replace any lists of len 1 with the value in the list
		3. check if its solved and check if any cells have no possible values



		'''
		self.original_grid = grid 
		self.n_rows = n_rows
		self.n_cols = n_cols
		self.n = n_rows * n_cols
		self.solved = False

		self.working_grid = self.update_grid()

	
	def update_grid(self):
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

		Returns:
		--------------
		grid_copy: list
			A list of lists representing a sudoku board with the empty squares filled with a list of possible values

		"""
		grid_copy = copy.deepcopy(self.original_grid)
	
		#creating a list of lists of lists for the possible values in each square
		for row in range(self.n): 
			for col in range(self.n):
				if grid_copy[row][col] == 0:
					possible_values = possible_values_combined(grid_copy, self.n_rows, self.n_cols, row, col)

					# if there is only one possible value for a square, replace with empty list
					if len(possible_values) == 1:
						grid_copy[row][col] = possible_values[0]
					else:
						grid_copy[row][col] = possible_values

		return grid_copy

	def wavefront_update(self):
		'''
		Pick a random list in the grid (with the smallest number of possible values) and randomly fill in one 
		of the possible values then update with the new possible values
		
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
		test_grid: list
			A list of lists representing a sudoku board with the empty squares filled with a list of possible values
		
		
		'''
		# in grid_copy, find the lists with the smallest number of possible values and pick one at random 
		self.find_shortest_list()

		





	def find_shortest_list(self):
		# find the indeces of the shortest lists in the grid (with len > 1) and pick one at random
		print('\nWorking grid: ', self.working_grid)
		# create a tuple containing the indices and length of all lists in the grid
		list_lengths = []
		for row in range(self.n_rows):
			for col in range(self.n_cols):

				value = self.working_grid[row][col]
				if isinstance(value, list):

					list_lengths.append(((row,col), len(self.working_grid[row][col])))

		# sort the list of tuples by the length of the list
		list_lengths.sort(key=lambda x: x[1])
		print('\nList lengths: ', list_lengths)

		# find the index of the shortest list
		shortest_list_idx = list_lengths[0][0]

		print('\nShortest list index: ', shortest_list_idx)

	def pprint(self):
		'''
		Prints the working grid as a sudoku board

		'''

		print('\nWorking grid:')
		print('\n')
		for row in range(self.n):
			if row % self.n_rows == 0 and row != 0:
				print('---------------------------------')
			for col in range(self.n):
				if col % self.n_cols == 0 and col != 0:
					print('| ', end='')
				print(self.working_grid[row][col], end=' ')
			print('\n')




		




if __name__ == '__main__':


	test_grid_1 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]
	

	example_class = SudokuSolver(test_grid_1, 2, 3)


	example_class.update_grid()
	
	example_class.wavefront_update()

	example_class.pprint()




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
	
	
	'''
	


class WavefrontInstance():
	def __init__(self, grid, previous_step):
		self.original_grid = grid
		self.new_grid = copy.deepcopy(grid)
		self.previous_step = previous_step
		self.next_step = None
		self.feasible = True
		self.solved = False
	
	def update_grid(self):
		
		The update grid should take a grid and create the the list of lists of possible values, removing any lists of len one and
		making them part of the grid. If there are no lists the grid is solved, if there are only lists of len greater than
		one, then this step is complete


		Parameters:
		--------------
		grid: list
			A list of lists representing a sudoku board

		Returns:
		--------------
		grid: list
			A list of lists representing a sudoku board


		Method:

		1. make the possible values grid
		2. replace any lists of len 1 with the value in the list
		4. check if its solved and check if any cells have no possible values


		
		# make the possible values grid

		pass

	def wavefront_update(self):
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


	
	
	'''