import matplotlib.pyplot as plt

def profile(solved_dict):
    """
    This function takes a dictionary of solved grids metrics and plots them. 
    [INSERT MORE PLOTTING DETAIL HERE]
    ----------
    Parameters
    ----------
    solved_dict: dict
        A dictionary of solved grids metrics
    ----------
    Returns
    ----------
    None
    """
    for dimensions in [(2,2), (3,2), (3,3)]: # Loop through the dimensions of the grids
        timings = []
        empty_cells = []
        iterations = []
        for key in solved_dict:
            if solved_dict[key][0] == dimensions:
                timings.append(solved_dict[key][1])
                empty_cells.append(solved_dict[key][2])
                iterations.append(solved_dict[key][3])
        print(timings)
        print(empty_cells)
        print(iterations)
        # Plot the time against the number of empty cells for the 3x3 grids
        # Make it a scatter plot with the empty cells on the x-axis and the time on the y-axis
        plt.scatter(empty_cells, timings)
        plt.xlabel("Number of empty cells")
        plt.ylabel("Time taken to solve (s)")
        plt.title(f"Time taken to solve {dimensions[0]}x{dimensions[1]} grids")
        plt.show()
        # Plot the time against the number of recursive iterations for the 3x3 grids
        # Make it a scatter plot with the number of recursive iterations on the x-axis and the time on the y-axis
        if dimensions == (3,3):
            plt.scatter(iterations, timings)
            plt.xlabel("Number of recursive iterations")
            plt.ylabel("Time taken to solve (s)")
            plt.title(f"Time taken to solve {dimensions[0]}x{dimensions[1]} grids")
            plt.show()





 