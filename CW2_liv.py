import copy
import time

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

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6, 2,3)]

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

# check if the value is already in the row/column
def check_line(line,n):
	for value in line:
		if value == n:
			return False 
	return True

# check if the value is already in the square
def check_square(grid,x,y,value,n_rows,n_cols):
	x = (x // n_rows)*n_rows
	y = (y // n_cols)*n_cols
	for i in range(n_rows):
		for j in range(n_cols):
			if grid[x+i][y+j] == value:
				return False
	return True

# find the co-ordinates with a free space i.e. has a 0
def find_free_space(grid, n):
	free_space = False
	# go through each row
	for row in range(n):
		# go through each column value
		for col in range(n):
			# set the co-ordinates if there is a free space
			if(grid[row][col] == 0):
				free_space = (row,col)
	return free_space

def recursive_solve(grid, n_rows, n_cols):
	# the highest value in the grid
	n = n_rows*n_cols	

	# find the co-ordinates of a free space
	free_space = find_free_space(grid, n)

	if free_space:
		# extract the co-ordinates from the free_space variable
		row_coord = free_space[0]
		col_coord = free_space[1]
		
		# extract the row and column
		row = grid[row_coord]
		col = list(zip(*grid))[col_coord]

		# try and fill the empty square
		for value in range(1,n+1):
			# for each value we try and fill in the space, check it isn't already in the column, row or square
			valid_value = check_line(row,value) and check_line(col,value) and check_square(grid,row_coord,col_coord,value,n_rows,n_cols)
			
			# if it is a valid value, fill the square and call recursive_solve again
			if(valid_value):
				# make a new grid which is a clone of the old grid, but filling the space with the value
				new_grid = [row[:] for row in grid]
				new_grid[row_coord][col_coord] = value
				final_grid = recursive_solve(new_grid,n_rows,n_cols)

				# if there are no free spaces, we are finished
				if(find_free_space(final_grid, n) == False):
					return final_grid
		return grid
	return grid


def solve(grid, n_rows, n_cols):
	'''
	Solve function for Sudoku coursework.
	Comment out one of the lines below to either use the random or recursive solver
	'''
	return recursive_solve(grid,n_rows,n_cols)


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''
def main():

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


if __name__ == "__main__":
	main()