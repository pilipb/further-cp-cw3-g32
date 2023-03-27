def get_squares(grid, n_rows, n_cols):
	"""
    This function takes a grid and returns a list of the squares in the grid.
    ----------
    Parameters
    ----------
    grid: list
        A list of lists representing the grid.
	n_rows: int
	    The number of rows in each square.
	n_cols: int
	    The number of columns in each square.
    ----------
    Returns
    ----------
    squares: list
        A list of lists representing the squares in the grid.
	"""
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

def possible_values_column(grid, row, column):
	"""
    This function takes a grid, a row and a column and returns a list of the possible values 
    for the cell at that row and column, based off he values in that column. 
    If the cell is not empty, it returns None.
    ----------
    Parameters
    ----------
    grid: list
        A list of lists representing the grid.
	row: int
	    The index of the row.
	column: int
	    The index of the column.
    ----------
    Returns
    ----------
    possible_values: list
        A list of the possible values for the cell at that row and column based off the values in that column.
	"""
	# Initialise a list of the possible values for the cell
	possible_values = list(range(1, len(grid)+1))
	# If the cell is empty, remove the values in the column from the list of possible values
	if grid[row][column] == 0:
		for i in range(len(grid)):
			if grid[i][column] in possible_values:
				possible_values.remove(grid[i][column])
		return possible_values
	else:
		return None
		
def possible_values_row(grid, row, column):
	"""
    This function takes a grid, a row and a column and returns a list of the possible values 
    for the cell at that row and column, based off he values in that row. 
    If the cell is not empty, it returns None.
    ----------
    Parameters
    ----------
    grid: list
        A list of lists representing the grid.
	row: int
	    The index of the row.
	column: int
	    The index of the column.
    ----------
    Returns
    ----------
    possible_values: list
        A list of the possible values for the cell at that row and column based off the values in that row.
	"""
    # Initialise a list of the possible values for the cell
	possible_values = list(range(1, len(grid)+1))
	# If the cell is empty, remove the values in the row from the list of possible values
	if grid[row][column] == 0:
		for i in range(len(grid)):
			if grid[row][i] in possible_values:
				possible_values.remove(grid[row][i])
		return possible_values
	else:
		return None

def possible_values_square(grid, n_rows, n_cols, row, column):
	"""
    This function takes a grid, a row and a column and returns a list of the possible values 
    for the cell at that row and column, based off he values in that square. 
    If the cell is not empty, it returns None.
    ----------
    Parameters
    ----------
    grid: list
        A list of lists representing the grid.
	row: int
	    The index of the row.
	column: int
	    The index of the column.
    ----------
    Returns
    ----------
    possible_values: list
        A list of the possible values for the cell at that row and column based off the values in that square.
	"""
	# Initialise a list of the possible values for the cell
	possible_values = list(range(1, len(grid)+1))
	squares = get_squares(grid, n_rows, n_cols)
	if grid[row][column] == 0:
		# Find the square that the cell is in
		index = (row//n_rows)*n_rows + column//n_cols
		square = squares[index]
		# Remove the values in the square from the list of possible values
		for i in square:
			if i in possible_values:
				possible_values.remove(i)
		return possible_values
	else:
		return None

def possible_values_combined(grid, n_rows, n_cols, row, column):
	"""
    This function takes a grid, a row and a column and returns a list of the possible values
    for the cell at that row and column, based off he values in that row, column and square.
    If the cell is not empty, it returns None.
    ----------
    Parameters
    ----------
    grid: list
        A list of lists representing the grid.
	n_rows: int
        The number of rows in each square.
	n_cols: int
        The number of columns in each square.
	row: int
        The index of the row.
	column: int
        The index of the column.
    ----------
    Returns
    ----------
    possible_values: list
        A list of the possible values for the cell at that row and column based off the values in that row, column and square.
	"""
	# If the cell is empty, find the possible values for the cell based off the values in the row, column and square of the cell
	if grid[row][column] != 0:
		return None
	possible_row_values = possible_values_row(grid,row,column)
	if possible_row_values == None:
		return None
	possible_column_values = possible_values_column(grid, row, column)
	if possible_column_values == None:
		return None
	possible_square_values = possible_values_square(grid, n_rows, n_cols, row, column)
	if possible_square_values == None:
		return None
	possible_values = []
	# Find the intersection of all three lists to find the possible values for the cell
	for i in possible_row_values:
		if i in possible_column_values and i in possible_square_values:
			possible_values.append(i)
	return possible_values

test_grid = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]
