from Sudoku import Sudoku
from grids import grids
from flag_identifier import input_collection
from file_input import file_input_main
import sys
import numpy as np
from profile_docs import profile_grids


"""
grid_storage = {}
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
        flag_dict, flag_value = input_collection(sys.argv[1:])

    # If not, print the error and exit
    except ValueError as e:
        print("Error: ",e)
        sys.exit()

    # If the file flag is enabled, run the file input function and exit
    if flag_dict['-file'] == True:
        # Run seperate file input function and exit
        file_input_main(flag_value['-file'][0], flag_value['-file'][1],  flag_dict['-hint'], flag_value['-hint'],flag_dict['-explain'], flag_dict['-profile'])
        return 
    
    ##### IF THERE IS NO FILE INPUT #####
    # The grids from grids.py are run automatically

    # Initialise the grid storage dictionary to store the Sudoku class instances
    grid_storage = {}
    # Initialise the solve metrics dictionary to store the profiling metrics if profiling is enabled
    solve_metrics = {}

    # Iterate through the grids and initialise the Sudoku class for each grid, storing the instance in the grid storage dictionary
    for index, grid in enumerate(grids):
        idx = int(index) + 1
        grid_storage[ f'Grid {idx}'] = Sudoku(grid = grid[0], 
                                                   n_rows = grid[1], 
                                                   n_cols = grid[2], 
                                                   hint_flag = flag_dict['-hint'], 
                                                   hint_number = flag_value['-hint'], 
                                                   profile_flag= flag_dict['-profile'],
                                                   explain_flag= flag_dict['-explain'])
        

    # Iterate through the grid storage dictionary and solve each grid using the wavefront and recursion methods
    for instance in grid_storage:

        # Solve the grid
        grid_storage[instance].wavefront_solve()
        grid_storage[instance].recursion_solve()
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



        # If the profile flag is enabled, store the profiling metrics in the solve metrics dictionary
        if flag_dict['-profile'] == True:
            print('\nRunning profiling simulations...\n')
            grid_storage[instance].profile()
            
            # extract the metrics
            solve_metrics[instance] = [(grid_storage[instance].n_rows, grid_storage[instance].n_cols), 
                                       (grid_storage[instance].avg_time_recursion, grid_storage[instance].avg_time_wavefront, grid_storage[instance].avg_time_overall), 
                                       grid_storage[instance].zero_counter, 
                                       grid_storage[instance].iterations,
                                       ]
            
        # If the explain flag is enabled, print the explanation of the solution (either hints or full solution)
        if flag_dict['-explain'] == True:
            grid_storage[instance].explain_class()
            
    # If the profile flag is enabled, print the profiling metrics
    if flag_dict['-profile'] == True:
        # Print the profiling metrics
        profile_grids(solve_metrics)   



if __name__ == "__main__":
    main()