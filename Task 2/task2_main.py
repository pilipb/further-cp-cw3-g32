import copy
import time
import sys
from modules import * 
from grids import grids
from flag_identifier import input_checker, read_flags
from hint import hint_
from flag_functions import explain, profile, file, hint
from file_input import file_input

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
        file_input(input_file, output_file, flag_dict['-explain'], 3,3)
        sys.exit()
        # This will simply solve the grid in the file and write the solution to the output file,
        # if the -explain flag is set to True, it will print the explanation of how the program solves the grid
        # This will ignore all other flags. 
    
    # If the -file flag is not set, we will solve the grids in the grids.py file



    
    



if __name__ == "__main__":
    print(main())


