'''
This function is used to provide a hint to the user, if the -flag hint is set to True

'''

# a basic hint function will provide the user with a list of random hints to help them solve the puzzle
def basic_hint(filled_in, hint_number):
    
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
    new_grid: list
        A list of lists representing a sudoku board with the hints added

    '''

    
    '''