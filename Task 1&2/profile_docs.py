from Sudoku import Sudoku
import matplotlib
from matplotlib import pyplot as plt
import cProfile as cp
import pstats
from pstats import SortKey


def profile_methods(grids, plot = True):

    '''
    This method will profile the quick_solve, recursion and propagation methods on a set of input grids and visualise the results

    Parameters:
    ---------------
    grids: list of objects
        A list of grid objects to be profiled (each grid can be a sudoku object that stores the n_rows and n_cols attributes as well as the grid itself)

    Returns:
    ---------------
    stats: dict
        A dictionary containing the statistics for each method in form:
        stats = {
            'quick_solve': [list of times],
            'recursion': [list of times],
            'propagation': [list of times],
            'grid_sizes': [list of grid sizes]
        }

    ** if plot is set to true, the method will also plot the results of the profiling **

    '''



    # initialise the stats dictionary
    stats = {}

    # initialise the lists to store the results
    quick_solve_times = []
    recursion_times = []
    propagation_times = []
    grid_sizes = []

    pr = cp.Profile()

    # loop through the grids and profile each method
    for grid in grids:
        # extract the grid and the dimensions from the object
        grid = grid[0]
        n_rows = grid[1]
        n_cols = grid[2]

        # store the size of the grid
        n = n_rows * n_cols
        grid_sizes.append(n)


        # re-initialise the solver
        solver = Sudoku(grid, n_rows, n_cols, hint_flag = False, hint_number = 0, profile_flag = False, explain_flag = False)

        # profile the quick_solve method
        pr.enable()
        solver.quick_solve()
        pr.disable()
        stats_quick = pr.getstats()
        quick_time = stats_quick.total_tt

        # profile the recursion method
        pr.enable()
        solver.recursion_solve()
        pr.disable()
        stats_rec = pr.getstats()
        rec_time = stats_rec.total_tt

        # profile the propagation method
        pr.enable()
        solver.wavefront_solve()
        pr.disable()
        stats_prop = pr.getstats()
        prop_time = stats_prop.total_tt

        # append the times to the lists
        quick_solve_times.append(quick_time)
        recursion_times.append(rec_time)
        propagation_times.append(prop_time)

    # add the lists to the stats dictionary
    stats['quick_solve'] = quick_solve_times
    stats['recursion'] = recursion_times
    stats['propagation'] = propagation_times
    stats['grid_sizes'] = grid_sizes



    # plot the results if plot is set to true
    if plot:
        # plot the times against the grid sizes on the same plot
        plt.plot(grid_sizes, quick_solve_times, label = 'quick_solve')
        plt.plot(grid_sizes, recursion_times, label = 'recursion')
        plt.plot(grid_sizes, propagation_times, label = 'propagation')
        plt.xlabel('Grid size')
        plt.ylabel('Time taken (s)')
        plt.title('Time taken for each method against grid size')
        plt.legend()
        plt.show()

    # return the stats dictionary
    return stats







def profile_grids(solved_dict):
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
                if dimensions == (3,3):
                    iterations.append(solved_dict[key][3])
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




###### RUN THE CODE ######


if __name__ == '__main__':


    from grids import grids

    # each grid in list is form (grid, n_rows, n_cols)
    profile_methods(grids, plot = True)



