import numpy as np
def explain(grid_number,solved_grid,filled_in,hint):
    """
    This function takes in a solved grid and returns a series of strings explaining how the grid was solved.
    ----------
    Parameters
    ----------
    grid: list of lists
        A list of lists representing the grid.
    ----------
    Returns
    ----------
    explanation: list of strings
        A list of strings explaining how the grid was solved.
    """
    if hint:
        print(f"Here is a hint for grid {grid_number}:")
    else:
        print(f"Solved grid {grid_number}: ",np.array(solved_grid))
        print("This can be done with the following steps:")
    for instruction in filled_in:
        if instruction[0] == 8:
            print(f"Insert an {instruction[0]} in the cell in row {instruction[1]+1} and column {instruction[2]+1}")
        else:
            print(f"Insert a {instruction[0]} in the cell in row {instruction[1]+1} and column {instruction[2]+1}")
    print("--------------------")
    pass
