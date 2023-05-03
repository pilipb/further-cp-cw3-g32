import numpy as np
def explain(filled_in,hint,profile,time_taken, method, iterations):
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
    print("--------------------")
    if profile:
        print(f"Time taken to solve: {time_taken:.8f} seconds")
        print(f"Method used: {method}")
        if method == "Recursion":
            print(f"Recursive iterations: {iterations}")
        print("--------------------")
    if hint:
        print("Partial solution above is the result of the hints you requested.")
        print("This is where values were inserted:")
    else:
        print("This can be done with the following steps:")
    for instruction in filled_in:
        if instruction[0] == 8:
            print(f"Insert an {instruction[0]} in the cell in row {instruction[1]+1} and column {instruction[2]+1}")
        else:
            print(f"Insert a {instruction[0]} in the cell in row {instruction[1]+1} and column {instruction[2]+1}")
    print("--------------------")
    pass
