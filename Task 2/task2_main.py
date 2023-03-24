import copy
import time
import sys
from modules import * 
import numpy as np
from grids import grids
from flag_identifier import input_checker, read_flags
from hint import make_hint
from explain import explain
from file_input import file_input
from profile import profile

# This is the main function, it is used to run the program.
def main():
    # Check if the input is valid - only contains valid flags and arguments
    try:
        input_checker(sys.argv[1:])
    except ValueError as e:
        print("Error: ",e)
        sys.exit()
    else:
        # Read the flags and values and return them as a dictionary 
        try:
            flag_dict, flag_value = read_flags(sys.argv[1:])
        except ValueError or FileNotFoundError as e:
            print("Error: ",e)
            sys.exit()
    print(flag_dict , flag_value)
            
    # The order of flags I'm thinking of is:
    # First look for the -file flag, if it is there, read the file and return the grid. This tells us what will be solved
    # Then look for the -explain flag, if it is there, print the explanation of the program as it solves using solve()
    # Then look for the -hint flag, if it is there, we can proivide hints based off the grid we have solved
    # Finally the -profile flag can be used to profile the program, this will be done at the end of the program once all solves have occured

    if flag_dict['-file'] == True:
        # Extract the input and output file names from the flag_value dictionary
        input_file = flag_value['-file'][0]
        output_file = flag_value['-file'][1]
        # Call the file function with the input and output file names and the -explain flag status.
        # This will solve the grid in the input file and write the solution to the output file with the explanation/hints if requested
        # It can read grids of size 4x4, 6x6, 9x9, 12x12 & 16x16 
        # (6x6 are assumed to be made up of 3x2 blocks and 12x12 are assumed to be made up of 4x3 blocks)
        file_input(input_file, output_file, flag_dict['-explain'], flag_dict['-hint'], flag_value['-hint'], flag_dict['-profile'])
        sys.exit()
        # This will simply solve the grid in the file and write the solution to the output file,
        # if the -explain flag is set to True, it will print the explanation of how the program solves the grid
        # This will ignore all other flags. 
    
    # If the -file flag is not set, we will solve the grids in the grids.py file
    # Initialise the dictionary that will store the solved grid as well as the steps taken to solve it.
    # This dictionary will also store partially completed grids if the -hint flag is set to True as well as the hint grid and instructions
    solve_metrics = {}
    for index,data in enumerate(grids):
        # Extract the grid, number of rows and number of columns from the grids.py file
        grid = data[0]
        original_grid = copy.deepcopy(grid)
        zero_counter = sum([row.count(0) for row in original_grid])
        n_rows = data[1]
        n_cols = data[2]
        # create a time stamp
        start = time.time()
        solved_grid, filled_in, iterations = solve(grid, n_rows, n_cols)
        end = time.time()
        # Print the time taken to solve the grid and the solved grid
        print(f'Time taken to solve grid {index+1}: {end-start} seconds, taking {iterations} recursive iterations')
        print(np.array(solved_grid))
        
        # Add the solved grid and the steps taken to solve it to the solved_dict dictionary
        solve_metrics[f'Grid {index+1}'] = [(n_rows, n_cols), (end-start), zero_counter, iterations]
        if flag_dict['-hint'] == True:
            hint_grid, hint_instructions, hint_number = make_hint(original_grid, filled_in, flag_value['-hint'])
        # If the -explain flag is set to True, print the inserted hints
            if flag_dict['-explain'] == True:
                explain((index+1),hint_grid,hint_instructions,flag_dict['-hint'])
        else:
        # If the -explain flag is set to True, print the steps taken to solve the grid
            if flag_dict['-explain'] == True:
                explain((index+1),hint_grid,hint_instructions,flag_dict['-hint'])
    
    if flag_dict['-profile'] == True:
        # Print the profiling metrics
        profile(solve_metrics)
 



if __name__ == "__main__":
    main()


