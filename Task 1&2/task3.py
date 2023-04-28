from possible_values import possible_values_combined

def possible_values_grid(grid, n_rows, n_cols, row, column):
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
				possible_values = list(possible_values_combined(grid_copy, n_rows, n_cols, i, j))
				grid_copy[i][j] = possible_values
	return grid_copy


test_grid = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]

grid_copy = possible_values_grid(test_grid, 2, 3, 0, 0)

test_grid2 = [
		[1,2,3,4],
		[3,4,1,2],
		[2,3,4,1],
		[4,1,2,0]
]

#print(possible_values_grid(test_grid2, 2, 2, 0, 0))

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

#print(grid_copy)
print(empty_squares_dict(grid_copy, 2, 3))

def wavefront_propogation(grid_copy, empty_squares_dict, n_rows, n_cols):
	
	n = n_rows * n_cols

	for num_missing_values in range(2,n+1):
		pass	

	
	
	
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
	
	