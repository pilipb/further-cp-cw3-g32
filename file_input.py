import numpy as np 
import copy
import time 
from hint import make_hint
from possible_values import possible_values_combined
from modules import solve
from Sudoku import Sudoku

def file_input(input_file, output_file, explain, hint, hint_number, profile):
    """
    This function takes a string and returns the contents of the file as a string
    ----------
    Parameters
    ----------
    input_file: str
        A string representing the name of the file to be read
    output_file: str
        A string representing the name of the file to be written to
    explain: bool
        A boolean value indicating whether the user requested an explanation or not
    hint: bool
        A boolean value indicating whether the user requested a hint or not
    hint_number: int
        An integer representing the number of hints the user requested
    profile: bool
        A boolean value indicating whether the user requested a profile or not
    ----------
    Returns
    ----------
    file_contents: str
        A string representing the contents of the file
    """

    # open the file
    # read the file
    # return the file contents
    with open(input_file, "r", encoding='utf-8-sig') as file:
        file_contents = file.read()

    # Convert the file to a list of lists of integers, where each list is a row in the csv
    file_contents = file_contents.split("\n")

    # remove the last element in the list, as it is an empty string
    file_contents = file_contents[:-1]
    file_contents = [i.split(",") for i in file_contents]

    # Convert the list of lists to a list of lists of integers
    for i in range(len(file_contents)):
        for j in range(len(file_contents[i])):
            try:
                file_contents[i][j] = int(file_contents[i][j])
            except ValueError:
                print("Input file must only contain integers between 0 and 9")

    # Read in grid dimensions to get n_row and n_col
    try:
        n_row,n_col = grid_dimensions(file_contents)
    except ValueError as e:
        print(e)
        return None
    try :
        file_input_check(file_contents, n_row, n_col)
    except ValueError as e:
        print(e)
        return None
    
    # Solve the sudoku grid
    original = copy.deepcopy(file_contents)
    start = time.time()
    solved_grid, filled_in, iterations = solve(file_contents, n_row, n_col)
    end = time.time()
    if hint:
        solved_grid, filled_in, hint_number = make_hint(original, filled_in, hint_number)

    # Convert solved_grid to a numpy array
    solved_grid = np.array(solved_grid)

    # Export the solved grid to a csv
    np.savetxt(output_file, solved_grid, delimiter=",", fmt="%d")
    with open(output_file, "a") as file:
        if profile:
            file.write(f"\n\nThis grid was solved in {end-start} seconds, using {iterations} recursive iterations")

        # If explain is True, print the steps taken to solve the grid into the output file as a list to the side of the grid
        if explain:
            # We cannot call explain() here as it is writing to a file instead of printing to the console
            if hint:
                file.write(f"\nAbove is a partially completed grid (it contains {hint_number} hints).")
                file.write(f"\nThe following is a list of where the hints were inserted.")
            else:
                file.write(f"\nThe following is a list of where the numbers were inserted to complete the grid.")
            for insertion in filled_in:
                if insertion[0] == 8:
                    file.write("\n")
                    file.write(f"Insert an {insertion[0]} in the cell in row {insertion[1]+1} and column {insertion[2]+1}")
                else:
                    file.write("\n")
                    file.write(f"Insert a {insertion[0]} in the cell in row {insertion[1]+1} and column {insertion[2]+1}")

        

def file_input_check(file_contents, n_row, n_col):
    """
    This function evaluates the content of the file to check if it is a valid sudoku grid
    List of checks:
    - Check if grid is a square
    - Check if grid is a valid sudoku grid
    ----------
    Parameters
    ----------
    file_contents: str
        A string representing the contents of the file
    ----------
    Returns
    ----------
    None (raises an error if the file is not a valid sudoku grid)
    """
    # Check if grid is a square        
    for row in file_contents:
        if len(row) != len(file_contents):
            raise ValueError("Input file must be a square")
        
    # Check all the values in the list are integers, between 0 and 9, 
    # and that the grid is a valid sudoku grid (All empty cells have at least one possible value)
    for row_index,row in enumerate(file_contents):
        for column_index,column in enumerate(row):
            if column > n_col*n_row or column < 0:
                raise ValueError("Input file must only contain integers between 0 and 9")
            if column == 0:
                possibilites = possible_values_combined(file_contents, n_row, n_col, row_index, column_index)
                if len(possibilites) == 0:
                    raise ValueError(f"Input file must be a valid sudoku grid. Cell at row {row_index+1} and column {column_index+1} has no possible values")

    

def grid_dimensions(file_contents):
    """
    This function reads in a soduku grid and returns the dimensions of the squares in the grid
    ----------
    Parameters
    ----------
    file_contents: list
        A list of lists representing the contents of the file
    ----------
    Returns
    ----------
    n_row: int
        The number of rows in each square
    n_col: int
        The number of columns in each square
    """
    # Read in grid dimensions to get n_row and n_col
    side_length = len(file_contents)
    if side_length == 4:
        n_row = 2
        n_col = 2
    elif side_length == 9:
        n_row = 3
        n_col = 3
    elif side_length == 16:
        n_row = 4
        n_col = 4
    elif side_length == 6:
        n_row = 3
        n_col = 2
    elif side_length == 12:
        n_row = 4
        n_col = 3
    else:
        raise ValueError("Input file must be a square with side length 4, 6, 9, 12 or 16")
    return n_row, n_col

    
def file_input_extraction(input_file):
    """
    This function takes a string and returns the contents of the file as a string
    ----------
    Parameters
    ----------
    input: str
        A string representing the input from the command line
    ----------
    Returns
    ----------
    file_contents: str
        A string representing the contents of the file
    """
    # open the file
    # read the file
    # return the file contents
    with open(input_file, "r", encoding='utf-8-sig') as file:
        file_contents = file.read()

    # Convert the file to a list of lists of integers, where each list is a row in the csv
    file_contents = file_contents.split("\n")

    # remove the last element in the list, as it is an empty string
    file_contents = file_contents[:-1]
    file_contents = [i.split(",") for i in file_contents]

    # Convert the list of lists to a list of lists of integers
    for i in range(len(file_contents)):
        for j in range(len(file_contents[i])):
            try:
                file_contents[i][j] = int(file_contents[i][j])
            except ValueError:
                print("Input file must only contain integers between 0 and 9")

    # Read in grid dimensions to get n_row and n_col
    try:
        n_row,n_col = grid_dimensions(file_contents)
    except ValueError as e:
        print(e)
        return None
    try :
        file_input_check(file_contents, n_row, n_col)
    except ValueError as e:
        print(e)
        return None
    # Solve the sudoku grid
    grid = copy.deepcopy(file_contents)
    return grid, n_row, n_col

def file_input_main(input_file, output_file, hint_flag, hint_value, explain_flag, profile_flag):
    '''
    This function takes the input

    Parameters
    ----------
    input_file: str
        A string representing the input file
    output_file: str
        A string representing the output file
    hint_flag: bool
        A boolean representing whether the user wants a hint
    hint_value: int
        An integer representing the value of the hint
    explain_flag: bool
        A boolean representing whether the user wants an explanation
    profile_flag: bool
        A boolean representing whether the user wants to profile the code

    Returns
    ----------
    None

    
    
    '''

    input_grid, n_row, n_col =  file_input_extraction(input_file)

    # initialise the sudoku grid
    grid_instance = Sudoku(grid=input_grid, 
                           n_rows = n_row, 
                           n_cols = n_col, 
                           hint_flag = hint_flag, 
                           hint_number =hint_value, 
                           profile_flag = profile_flag, 
                           explain_flag = explain_flag)
    
    # Solve the sudoku grid
    grid_instance.solve_sudoku('recursion')
    grid_instance.solve_sudoku('overall')
    grid_instance.solve_sudoku('wavefront')
    
    if hint_flag:
        grid_instance.hint_class()
        output_grid = grid_instance.hint_grid
    else:
        output_grid = grid_instance.grid


    # write the output to a file
    np.savetxt(output_file, output_grid, delimiter=",", fmt="%d")
    with open(output_file, "a") as file:

        # say that the grid has been solved using wavefront
        file.write(f"\n\nThe solution grid is taken from the wavefront algorithm.")
        if profile_flag:
            # print the times taken by each algorithm to the output file
            file.write(f"\n\nThe following are the times taken by each algorithm to solve the grid (note if 0.0 it is likely due to the small scale and bit errors):")
            file.write(f"\nWavefront: {grid_instance.time_taken_wavefront}")
            file.write(f"\nRecursion: {grid_instance.time_taken_recursion}")
            file.write(f"\nCombination (recursion + quickfill): {grid_instance.time_taken_overall}")

        # If explain is True, print the steps taken to solve the grid into the output file as a list to the side of the grid
        if explain_flag:
            # We cannot call explain() here as it is writing to a file instead of printing to the console
            if hint_flag:
                file.write(f"\n\nAbove is a partially completed grid (it contains {hint_value} hints).")
                file.write(f"\nThe following is a list of where the hints that were inserted.")
                for insertion in grid_instance.hints:
                    if insertion[0] == 8:
                        file.write("\n")
                        file.write(f"Insert an {insertion[0]} in the cell in row {insertion[1]+1} and column {insertion[2]+1}")
                    else:
                        file.write("\n")
                        file.write(f"Insert a {insertion[0]} in the cell in row {insertion[1]+1} and column {insertion[2]+1}")

            else:
                file.write(f"\n\nThe following is a list of where the numbers were inserted to complete the grid.")
                for insertion in grid_instance.filled_in:
                    if insertion[0] == 8:
                        file.write("\n")
                        file.write(f"Insert an {insertion[0]} in the cell in row {insertion[1]+1} and column {insertion[2]+1}")
                    else:
                        file.write("\n")
                        file.write(f"Insert a {insertion[0]} in the cell in row {insertion[1]+1} and column {insertion[2]+1}")



