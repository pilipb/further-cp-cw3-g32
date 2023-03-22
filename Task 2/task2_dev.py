
import copy
import time
import sys
from modules import * 
from grids import grids
from flag_identifier import input_checker, read_flags
from hint import hint_


'''
This is the main function, it is used to run the program.

On run, the command line input is checked to see if it is valid, 
if it is, the flags and values are read and stored in a dictionary.

The program then runs the test script, and prints the results, whilst applying the
flag requests.

'''


def main():

	# Check if the input is valid - only contains valid flags and values
	if input_checker(sys.argv[1:]):

		# Read the flags and values
		flag_dict, flag_value = read_flags(sys.argv[1:])
		print('The dictionary of flags is: ',flag_dict ,' The values associated with flags are: ', flag_value)

	# If the input is valid, check if the flags are valid
	else: 
		ValueError("Invalid command line flag input, try again")

	points = 0

	print("Running test script for coursework 1")
	print("====================================")
	
	for (i, (grid, n_rows, n_cols)) in enumerate(grids):
		print("Solving grid: %d" % (i+1))

		# make a copy of the grid for comparison
		grid_copy = copy.deepcopy(grid)

		start_time = time.time()
		solution, filled_in = solve(grid, n_rows, n_cols)
		elapsed_time = time.time() - start_time

		print("\nSolved in: %f seconds" % elapsed_time)
		print("\nSolution grid: " , solution)

		if check_solution(solution, n_rows, n_cols):
			print("grid %d correct" % (i+1))
			points = points + 10
		else:
			print("grid %d incorrect" % (i+1))

		# check if hint is set to true
		if flag_dict["-hint"] == True:
			hint_n = flag_value["-hint"]

			hint_grid = hint_(grid_copy, filled_in, hint_n)
			print("\nHint grid: ")
			print(hint_grid)
		



	print("====================================")
	print("\nTest script complete, Total points: %d" % points)


if __name__ == "__main__":
	main()