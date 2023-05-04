from matplotlib import pyplot as plt


def profile_grids(solved_dict):
    '''
    This function takes in the dictionary of metrics from the profiling method in the class and plots the metrics
    
    Parameters
    ----------
    solved_dict : dict
        A dictionary containing the metrics for each grid
        in the form:
            {grid_name: [(grid_size), (avg_time_recursion, avg_time_wavefront, avg_time_overall), zero_counter, iterations]}
    
    Returns
    ---------
    None (plots the metrics)

    
    '''
    import numpy as np

    # Initialise the figure and plot the times for different methods on the same plot
    # Initialise lists for the average rnu times of each method and the number of zeros in each grid
    num_zeros = []
    recur_times = []
    wave_times = []
    overall_times = []

    
    plt.figure()
    # loop through the dictionary and plot the metrics for each method in a single colour
    for grid in solved_dict:
        # extract the metrics into separate lists
        num_zeros.append(solved_dict[grid][2])
        recur_times.append(solved_dict[grid][1][0])
        wave_times.append(solved_dict[grid][1][1])
        overall_times.append(solved_dict[grid][1][2])

    # Add the labels
    plt.plot(num_zeros,recur_times, 'o', label = 'Recursion', color = 'blue')
    plt.plot(num_zeros, wave_times, 'o', label = 'Wavefront', color = 'orange')
    plt.plot(num_zeros, overall_times, 'o', label = 'Overall', color = 'green')

    # plot lines of best fit
    plt.plot(np.unique(num_zeros), np.poly1d(np.polyfit(num_zeros, recur_times, 1))(np.unique(num_zeros)), label = 'Recursion Line of Best Fit', color = 'blue')
    plt.plot(np.unique(num_zeros), np.poly1d(np.polyfit(num_zeros, wave_times, 1))(np.unique(num_zeros)), label = 'Wavefront Line of Best Fit', color = 'orange')
    plt.plot(np.unique(num_zeros), np.poly1d(np.polyfit(num_zeros, overall_times, 1))(np.unique(num_zeros)), label = 'Overall Line of Best Fit', color = 'green')

    plt.xlabel('Number of Empty Spaces in Grid')
    plt.ylabel('Average Time (s) (log scale)')

    # make the y axis log scale
    plt.yscale('log')

    plt.title('Average Time to Solve Grids')
    plt.legend()
    # show
    plt.show()











