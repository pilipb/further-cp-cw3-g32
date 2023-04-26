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

print(possible_values_grid(test_grid, 2, 3, 0, 0))
