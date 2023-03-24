import numpy as np 
import copy
import time 
from hint import make_hint
from possible_values import possible_values_combined
from modules import solve
def file_input(input_file, output_file, explain, hint, hint_number, profile):
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
    # If explain is True, print the steps taken to solve the grid into the output file as a list to the side of the grid
    if explain:
        # We cannot call explain() here as it is writing to a file instead of printing to the console
        with open(output_file, "a") as file:
            if profile:
                file.write(f"\n\nThis grid was solved in {end-start} seconds, using {iterations} recursive iterations")
            if hint:
                file.write("\n")
                file.write(f"Instructions for the {hint_number} hints")
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
    # Check if grid is a square        
    for row in file_contents:
        if len(row) != len(file_contents):
            raise ValueError("Input file must be a square")
    

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

    
