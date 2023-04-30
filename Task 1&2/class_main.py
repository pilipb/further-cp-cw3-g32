from Sudoku import Sudoku
from grids import grids
from flag_identifier import input_checker, read_flags
from file_input import file_input_main
import sys
import numpy as np
from profile import profile
"""
grid_stroage = {}
for index, grid in enumerate(grids):
    grid_stroage[f'Grid {index + 1}'] = Sudoku(grid[0], grid[1], grid[2], hint_flag = True, hint_number = 3)

for instance in grid_stroage:
    grid_stroage[instance].recursion()
    grid_stroage[instance].hint_class()
    print('Grid',grid_stroage[instance].grid)
    print('Hint Grid',grid_stroage[instance].hint_grid)
"""



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
    
    if flag_dict['-file'] == True:
        # Run seperate file input function and exit
        file_input_main(flag_value['-file'][0], flag_value['-file'][1],  flag_dict['-hint'], flag_value['-hint'],flag_dict['-explain'], flag_dict['-profile'])
        return 
    # If not, pull the grids from grids.py and intialise the Sudoku class for each grid and store in a dictionary
    # Initialise the grid storage dictionary to store the Sudoku class instances
    grid_storage = {}
    # Initialise the solve metrics dictionary to store the profiling metrics if profiling is enabled
    solve_metrics = {}
    # Iterate through the grids and initialise the Sudoku class for each grid, storing the instance in the grid storage dictionary
    for index, grid in enumerate(grids):
        grid_storage[f'Grid {index + 1}'] = Sudoku(grid = grid[0], 
                                                   n_rows = grid[1], 
                                                   n_cols = grid[2], 
                                                   hint_flag = flag_dict['-hint'], 
                                                   hint_number = flag_value['-hint'], 
                                                   profile_flag= flag_dict['-profile'],
                                                   explain_flag= flag_dict['-explain'])
    # Iterate through the grid storage dictionary and:
    for instance in grid_storage:
        # Solve the grid
        grid_storage[instance].solve()
        output_grid = grid_storage[instance].grid
        # If the hint flag is enabled, generate the hint grid and return it
        if flag_dict['-hint'] == True:
            grid_storage[instance].hint_class()
            output_grid = grid_storage[instance].hint_grid
            # This is just a little printed message outside of the explain method so
            # There is a little explanation of what the hint grid is
            if flag_dict['-explain'] == False:
                print('Hint Grid')
                print(f'({flag_value["-hint"]} hints requested)')
        # Print the appropriate grid
        print(instance)
        print(np.array(output_grid))
        # If the explain flag is enabled, print the explanation of the solution (either hints or full solution)
        if flag_dict['-explain'] == True:
            grid_storage[instance].explain_class()
        # If the profile flag is enabled, store the profiling metrics in the solve metrics dictionary
        if flag_dict['-profile'] == True:
            solve_metrics[instance] = [(grid_storage[instance].n_rows, grid_storage[instance].n_cols), 
                                       (grid_storage[instance].time_taken), 
                                       grid_storage[instance].zero_counter, 
                                       grid_storage[instance].iterations]
    # If the profile flag is enabled, print the profiling metrics
    if flag_dict['-profile'] == True:
        # Print the profiling metrics
        profile(solve_metrics)   

if __name__ == "__main__":
    main()