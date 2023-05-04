import random


def make_hint(grid, filled_in, hint_number):
    
    '''
    This function is used to provide a hint to the user, if the -flag hint is set to True
    This will output the number of hints the user has requested, with the corresponding locations.

    Parameters
    ----------

    grid: list
        A list of lists representing a sudoku board (original)
    filled_in: list
        A list of the squares that have been filled in and their locations [value, row, column]
    hint_number: int
        The number of hints the user has requested

    Returns
    ----------
    hint_grid: list
        A list of lists representing a sudoku board with the hints added


    '''

    # check if the number of hints requested is greater than the number of squares filled in
    if hint_number > len(filled_in):
        hint_number = len(filled_in)
        print(f"\nYou have requested more hints than there are squares filled in, so you will be given all the hints available ({hint_number})")
        
    # Randomly arrange the list of filled in squares so hints don't fill in sequentially
    random.shuffle(filled_in)
    hints = []
    # fill in the appropriate number of squares with the corresponding values
    for n in range(hint_number):
        # Add the hint to the grid
        grid[filled_in[n][1]][filled_in[n][2]] = filled_in[n][0]
        # Add the hint to the list of hints
        hints.append([filled_in[n][0], filled_in[n][1], filled_in[n][2]])
    return grid, hints, hint_number

def find_filled(grid, ans):

    '''
    This function is used to find the squares that have been filled in and their locations by comparison
    of the original board and the solved board.

    Parameters
    ----------
    grid: list
        A list of lists representing a sudoku board (original)
    ans: list
        A list of lists representing a sudoku board (solved)

    Returns
    ----------
    filled_in: list
        A list of the squares that have been filled in and their locations [value, row, column]

    '''
    filled_in = []
        
    # loop through the grid and compare the values to the solved grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            
            # if the values are different, the square has been filled in
            if grid[row][col] != ans[row][col]:
                filled_in.append([ans[row][col], row, col])
    # This doesnt work for a sodoku board with no squares filled in
    return filled_in





    
    