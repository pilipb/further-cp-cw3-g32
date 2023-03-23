'''
These functions are used to provide a hint to the user, if the -flag hint is set to True,
the number of hints the user has requested will be provided.

'''
# imports
import copy


def make_hint(grid, filled_in, hint_number):
    
    '''
    This function is used to provide a hint to the user, if the -flag hint is set to True
    This will output the number of hints the user has requested, with the corresponding locations.

    Parameters
    ----------

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
        print("\nYou have requested more hints than there are squares filled in, so you will be given all the hints available:")
        hint_number = len(filled_in)

    for n in range(hint_number):
        
        grid[filled_in[n][1]][filled_in[n][2]] = filled_in[n][0]

    return grid

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
        
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != ans[row][col]:
                filled_in.append([ans[row][col], row, col])

    return filled_in





    
    