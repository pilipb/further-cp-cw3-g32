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

	pass