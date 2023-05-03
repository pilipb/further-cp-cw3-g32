from possible_values import possible_values_combined
import copy
import numpy as np
import random


#### CURRENTLY UNUSED FUNCTIONS ####

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
	


###### CLASS CONTAINS ALL FUNCTIONS ######

class SudokuGrid():
	# instances of grid at a certain point in the solution tree
	def __init__(self, grid, n_rows, n_cols, chosen_move = None):
		'''
		The SudokuGrid Class will store the problem / solution to the grid at each step of the solving process. The object will store an original
		grid which is the grid from the previous step. The work_grid working grid will be the grid AFTER the chosen move has been implemented. 
		If the grid is solved then that attribute will be set to true.

		Parameters:
		-------------
		grid: list of lists
			the input grid from the previous iteration
		n_rows: int
			number of rows
		n_cols: int
			number of columns
		chosen_move: tuple (default None)
			the chosen move should be given as a tuple of form ((row_idx, col_idx), value)

		Methods:
		-------------

		
		'''

		self.original_grid = grid
		self.work_grid = copy.deepcopy(grid)
		self.n_rows = n_rows
		self.n_cols = n_cols
		self.n = n_rows * n_cols
		self.chosen_move = chosen_move # input chosen
		self.solved = False



	def update_grid(self, chosen_move = None):
		"""
		Parameters:
		--------------
		grid: list
			A list of lists representing a sudoku board (empty squares are represented as 0)
		n_rows: int
			The number of rows in each square
		n_cols: int
			The number of columns in each square
		row: int
			The row index of the cell to be filled
		column: int
			The column index of the cell to be filled
		chosen_move: tuple
			Location and value of move in form: ((i,j), val)

		Returns:
		--------------
		updates working grid

		"""
		if chosen_move:
			self.chosen_move = chosen_move
			(r,c) = self.chosen_move[0]
			value = self.chosen_move[1]
			# insert chosen move
			self.work_grid[r][c] = value
			self.original_grid[r][c] = value
			
		
		#creating a list of lists of lists for the possible values in each square
		for row in range(self.n): 
			for col in range(self.n):

				# find an empty spot (0)
				if self.work_grid[row][col] == 0:
					
					# find the possible values
					possible_values = possible_values_combined(self.work_grid, self.n_rows, self.n_cols, row, col)

					# if there is only one possible value for a square, replace with the value in the working grid
					if len(possible_values) == 1:
						self.work_grid[row][col] = int(possible_values[0])
						self.original_grid[row][col] = int(possible_values[0])
					else:
						self.work_grid[row][col] = possible_values


	
	def next_step(self):
		'''
		This function will check the grid after the update for:
		1) any empty squares with no possible values (return 'None')
		2) if the sudoku is solved (set self.solved to True)
		3) If neither of these, we move down the solution tree and return the next step

		'''
		lists = False
		for row in range(self.n):
			for col in range(self.n):
				# if any lists in grid have length 0 return None
				if isinstance(self.work_grid[row][col], list) and len(self.work_grid[row][col]) == 0:
					return False
				if isinstance(self.work_grid[row][col], list):
					lists = True

		if not lists:
			self.solved = True
			return 'solved'
		# if not None and it isnt the solution, we choose the next step
		self.next_move = self.find_shortest_list()
		
		return self.next_move
	
	
		
	def find_shortest_list(self):
		'''
		Find the shortest list in the grid and return the index of the list and the length of the list
		Parameters:
		--------------
		
		Returns:
		--------------
		index: tuple
			The index of the shortest list in the grid
		'''

		# create a tuple containing the indices and length of all lists in the grid
		list_lengths = []
		for row in range(self.n):
			for col in range(self.n):
				value = self.work_grid[row][col]

				# if theres a list at that position, store the list 
				if isinstance(value, list):
					list_lengths.append(((row,col), value))

		if len(list_lengths) == 0:
			return False

		# sort the list of tuples by the length of the list
		list_lengths.sort(key=lambda x: len(x[1]))

		# find the index of the shortest list with a random choice from the list
		possible_values = list_lengths[0][1] 

		# return the indeces and the choice as a tuple
		return (list_lengths[0][0], possible_values)
	

	def remove_move(self, move):
		'''
		Remove move takes a certain move and removes it from the working grid (so it cant be considered again)

		Parameters:
		-------------
		move: tuple
			Tuple in form ((row,col),val) for the last move taken by the propagation algorithm

		Returns:
		-------------
		None:
			Updates the work_grid
		
		'''
		if move == False:
			return 'dead end'
		else:
			(r,c) = move[0]
			value = move[1]

			print('removing', value, 'from', (r,c))

			self.work_grid[r][c].remove(value)




		# if len(self.work_grid[r][c]) == 1:
		# 	self.work_grid[r][c] = int(self.work_grid[r][c][0])




	def pprint(self):
		'''
		Prints the working grid as a sudoku board

		Parameters:
		--------------
		grid: list
			A list of lists representing a sudoku board

		Returns:
		--------------
		None
			Prints the grid as a sudoku board


		'''
		print('\nPretty Print:\n')
		for row in range(self.n):
			if row % self.n_rows == 0 and row != 0:
				print('---------------------------------')
			for col in range(self.n):
				if col % self.n_cols == 0 and col != 0:
					print('| ', end='')
				print(self.work_grid[row][col], end=' ')
			print('\n')
	





class SudokuSolver():
	# manage instances from the SudokuGrid class and solve the sudoku puzzle
	def __init__(self, grid, n_rows, n_cols):
		'''
		The solver will take a sudoku puzzle and solve it using the wavefront propagation algorithm

		1. make the possible values grid
		2. replace any lists of len 1 with the value in the list
		3. check if its solved and check if any cells have no possible values
		4. if not solved, pick a random cell with the smallest number of possible values and randomly fill in one of the possible values
		5. update the possible values grid with the new possible values
		6. repeat from step 3

		Steps 1-3 are done in the __init__ method, the rest are done in the wavefront_update method:
		eventually should implement a while loop that will stop when the grid is solved or when there are no more possible values for a cell

		Parameters:
		--------------
		sudoku_obj: class
			An instance of the SudokuGrid class containing the sudoku board and the possible values for each cell


		'''

		self.grid = grid
		self.n_rows = n_rows
		self.n_cols = n_cols
		self.init_instance = SudokuGrid(grid, n_rows, n_cols)
		self.init_instance.update_grid()
		self.first_move = self.init_instance.next_step()

		self.frontier = [self.first_move]
		
		# self.frontier = [self.init_instance] # will store each grid object at each stage of the solution
		self.solved = False

	def wavefront_uno(self):
		'''
		Using this as structure

		def wavefront_solver(grid,n_rows,n_cols):
			combo = n_rows*n_cols
			grid_solve = copy.deepcopy(grid)
			visited = []
		
			while find_empty(grid_solve) != None :
				low_row, low_col, pos = solving_index(grid_solve, n_rows, n_cols)
				if len(pos) > 0:
					grid_solve[low_row][low_col] = pos[0]
					visited.append([low_row,low_col,pos])
				else:
					while(len(visited[-1][2]) == 1):
						row = visited[-1][0]
						col = visited[-1][1]
						grid_solve[row][col] = 0
						del visited[-1]
					del visited[-1][2][0]
					row = visited[-1][0]
					col = visited[-1][1]
					grid_solve[row][col] = visited[-1][2][0]
		'''

		# while the last grid is not solved
		while not self.solved:

			# start keeping track of moves in frontier in form ((row,col),list of possible values)
			move = self.frontier[-1]
			print('move', move)

			# put the move into the grid
			self.init_instance.update_grid(chosen_move = move)
			next_move = self.init_instance.next_step()

			# if the next move is solved, then we are done
			if next_move == 'solved':
				self.solved = True
				print('solved')
				self.init_instance.pprint()
				return self.init_instance.work_grid
			
			elif next_move == False: # the previous move has lead to a dead end
				
				self.frontier.pop()
				self.init_instance.work_grid = copy.deepcopy(self.init_instance.original_grid)
				self.init_instance.update_grid()
				self.init_instance.pprint()
				continue




		

	# def wavefront_solve(self):
	# 	'''
	# 	After initialisation, loop through the creating next step, and testing step until either solved or None at which point refer back to frontier


		# while the last grid is not solved
		while not self.solved:
			next_instance = SudokuGrid(self.frontier[-1].original_grid, self.n_rows, self.n_cols, chosen_move = self.frontier[-1].next_step())
			next_instance.update_grid()
			next_move = next_instance.next_step()
			print('Next working grid', next_instance.work_grid)
			print('next_move', next_move)

			# if the next move is solved, then we are done
			if next_move == 'solved':
				self.solved = True
				print('solved')
				return next_instance

			# catch when there is empty lists
			elif next_move == False:
				print('in none')
				# we need to backtrack until we find a move that is not a dead end
				instance_number = len(self.frontier)

				# back track until we find a move that is not a dead end
				for _ in range(instance_number):
					# print('\n Length of frontier', len(self.frontier))

					# the move we need to remove is the next move of the previous working object
					del_move = self.frontier[-1].next_step()

					# look at the next move of the previous working object and remove it from the possible values
					local_next_move = self.frontier[-1].remove_move(del_move)

					print('Updated working grid', self.frontier[-1].work_grid)

					# if the next move is a dead end, remove the working object from the frontier and continue
					print('Local next move', local_next_move)

					if local_next_move == 'dead end':
						self.frontier.pop()
						self.frontier[-1].remove_move(self.frontier[-1].next_step())
						self.frontier[-1].update_grid()
						
						print('length of frontier', len(self.frontier))
						print('in the dead end if statement')

					else:
						# the move has been removed, so we need to update the working object
						next_instance = SudokuGrid(self.frontier[-1].original_grid, self.n_rows, self.n_cols, chosen_move = self.frontier[-1].next_step())

						break
			else:
				# as normal: update the working object with the next move and create a new working object
				print('in else (move valid)', next_move)
				self.frontier.append(next_instance)
				print('new length of frontier', len(self.frontier))
				print('------------------')


	def wavefront_solve_3(self):
		"""Take 3"""
		




	# def wavefront_solve_2(self):
	# 	'''
	# 	After initialisation, loop through the creating next step, and testing step until either solved or None at which point refer back to frontier

		
	# 	'''
	# 	# our working object is the last element in the frontier (its already been updated and the next move has been chosen)
	# 	# while find_empty(grid_solve) != None :

	# 	working_obj = self.frontier[-1]

	# 	while working_obj.shortest_list():

	# 		work_r, work_c = working_obj.shortest_list()[0]
	# 		work_list = working_obj.shortest_list()[1]

	# 		if len(work_list) > 0:

	# 			# try the first value in the list
	# 			working_obj.work_grid[work_r][work_c] = work_list[0]
	# 			working_obj.update_grid()
	# 			step = working_obj.next_step()
        
	# 		else:
	# 			while(len(work_list))
		
	# 	low_row, low_col, pos = solving_index(grid_solve, n_rows, n_cols)
    #     if len(pos) > 0:
    #         grid_solve[low_row][low_col] = pos[0]
    #         visited.append([low_row,low_col,pos])
    #     else:
    #         while(len(visited[-1][2]) == 1):
    #             row = visited[-1][0]
    #             col = visited[-1][1]
    #             grid_solve[row][col] = 0
    #             del visited[-1]
    #         del visited[-1][2][0]
    #         row = visited[-1][0]
    #         col = visited[-1][1]
    #         grid_solve[row][col] = visited[-1][2][0]



######## TESTING ########

if __name__ == '__main__':


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
	#grid_ex = SudokuGrid(test_grid_1, 3, 3)

	# import it into the solver class
	solver = SudokuSolver(grid6, 2, 3)

	# solve using wavefront propagation
	solved_obj = solver.wavefront_uno()

	# print the solved grid
	print('Solved grid: ')
	solved_obj.pprint()



	



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
