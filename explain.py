import numpy as np
def explain(filled_in,hint,profile,avg_time_recursion,avg_time_wavefront,avg_time_overall):
    """
    This function takes in a solved grid and returns a series of strings explaining how the grid was solved.
    ----------
    Parameters
    ----------
    filled_in: list of tuples
        A list of tuples containing the values that were inserted into the grid.
        Each tuple is of the form (value, row, column)
    hint: bool
        A boolean value indicating whether the user requested a hint or not.
    profile: bool
        A boolean value indicating whether the user requested a profile or not.
    avg_time_recursion: float
        The average time taken to solve a grid using the recursive method.
    avg_time_wavefront: float   
        The average time taken to solve a grid using the wavefront method.
    avg_time_overall: float
        The average time taken to solve a grid using a combination of quickfill and recursion method.
    ----------
    Returns
    ----------
    explanation: list of strings
        A list of strings explaining how the grid was solved.
    """
    print("--------------------")


    if profile:
        # print the average times for each method
        print(f"Average time taken to solve grid using recursion: {avg_time_recursion} seconds")
        print(f"Average time taken to solve grid using wavefront: {avg_time_wavefront} seconds")
        print(f"Average time taken to solve grid using quickfill and recursion: {avg_time_overall} seconds")
    if hint:
        print("Partial solution above is the result of the hints you requested.")
        print("This is where values were inserted:")
    else:
        print("This is the recursive solution to the grid.")
        print("This can be done with the following steps:")
    for instruction in filled_in:
        if instruction[0] == 8:
            print(f"Insert an {instruction[0]} in the cell in row {instruction[1]+1} and column {instruction[2]+1}")
        else:
            print(f"Insert a {instruction[0]} in the cell in row {instruction[1]+1} and column {instruction[2]+1}")
    print("--------------------")
    pass
