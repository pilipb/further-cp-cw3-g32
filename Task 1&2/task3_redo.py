import copy
from modules import possible_values_combined, check_solution
import numpy as np
class NewSudokuGrid():
    def __init__(self, grid, n_rows, n_cols, chosen_move = None):
        self.grid = grid
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.chosen_move = chosen_move
        self.working_grid = copy.deepcopy(grid)
        self.direction = 'down'
        if chosen_move != None:
            self.move_location = chosen_move[0]
            self.move_value = chosen_move[1]
        self.solved = False
    
    def update_grid(self):
        """
        1) Updates the original grid with the chosen move
        2) Updates the working grid with the possible values for each cell
        3) If the length of the possible values list is 1, the cell is updated with the value in both grids
        4) Check if word grid has any lists in it at all, if theyre all integers, check if the solution is correct

    
        """
        if self.chosen_move != None:
        # 1)
            self.grid[self.move_location[0]][self.move_location[1]] = self.move_value
            self.working_grid[self.move_location[0]][self.move_location[1]] = self.move_value
        # 2)
        for i in range(len(self.working_grid)):
            for j in range(len(self.working_grid)):
                if self.working_grid[i][j] == 0:
                    possible_values = possible_values_combined(self.working_grid, self.n_rows, self.n_cols, i, j)
                    self.working_grid[i][j] = possible_values
        # 3)
        for i in range(len(self.working_grid)):
            for j in range(len(self.working_grid)):
                if type(self.working_grid[i][j]) == list:
                    if len(self.working_grid[i][j]) == 1:
                        self.working_grid[i][j] = self.working_grid[i][j][0]
        
        # 4)
        lists = False
        for i in range(len(self.working_grid)):
            for j in range(len(self.working_grid)):
                if type(self.working_grid[i][j]) == list:
                    lists = True
        if lists == False:
            self.solved = check_solution(self.working_grid, self.n_rows, self.n_cols)

        



                
    
    def define_direction(self):
        """
        This goes through the working grid and checks if any lists have length zero,
        if they do, self.direction should be set to 'backtrack' and be returned
        """
        for i in range(len(self.working_grid)):
            for j in range(len(self.working_grid)):
                if type(self.working_grid[i][j]) == list:
                    if len(self.working_grid[i][j]) == 0:
                        self.direction = 'backtrack'
                        return self.direction
        self.direction = 'down'
        return self.direction

    def next_move(self):
        """
        If self.direction is 'down', this function will return the next move
        This is a random move from the cell with the smallest possible values list
        This should be returned in the format of a tuple, with the first element being the location of the cell and the second being the value to be placed in the cell

        """
        if self.direction == 'down':
            # Find the cell with the smallest possible values list
            smallest_possible_values = 9
            smallest_possible_values_location = None
            for i in range(len(self.working_grid)):
                for j in range(len(self.working_grid)):
                    if type(self.working_grid[i][j]) == list:
                        if len(self.working_grid[i][j]) < smallest_possible_values:
                            smallest_possible_values = len(self.working_grid[i][j])
                            smallest_possible_values_location = (i, j)
            random_value = self.working_grid[smallest_possible_values_location[0]][smallest_possible_values_location[1]][0]
            # Return the move
            return (smallest_possible_values_location, random_value)
        
    def remove_move(self, move):
        """
        This function goes through the working grid and removes a highlighted move
        
        """
        # Remove the move from the working grid
        try:
            self.working_grid[move[0][0]][move[0][1]].remove(move[1])
        except AttributeError:
            self.working_grid[move[0][0]][move[0][1]] = []
        # Update the grid
        self.update_grid()
        # Update the direction
        self.define_direction()
        # Return the direction
        return self.direction
            

                    

    
test_grid_1 = [
	[1, 0, 0, 2],
	[0, 0, 1, 0],
	[0, 1, 0, 4],
	[0, 0, 0, 1]]
grid9 = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,3,0,8,5],
         [0,0,1,0,2,0,0,0,0],
         [0,0,0,5,0,7,0,0,0],
         [0,0,4,0,0,0,1,0,0],
         [0,9,0,0,0,0,0,0,0],
         [5,0,0,0,0,0,0,7,3],
         [0,0,2,0,1,0,0,0,0],
         [0,0,0,0,4,0,0,0,8]]
grid6 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]

def wavefront_solver(grid, n_rows, n_cols):
    print('Initial grid:', np.array(grid))
    # Initialise the frontier (list of instances)
    frontier = []
    # Initialise the first instance
    init_instance = NewSudokuGrid(grid, n_rows, n_cols)
    init_instance.update_grid()
    # Check the grid can go down, if it can, add it to the frontier
    init_instance.define_direction()
    if init_instance.direction == 'down':
        frontier.append(init_instance)
    else:
        return 'No solution'
    # Define initial next move
    next_move = init_instance.next_move()
    next_grid = init_instance.grid
    print('Next move:', next_move)
    print('Next grid:', np.array(next_grid))
    # While the grid is not solved
    solved = init_instance.solved
    while solved == False:
        # Create a new instance with the next move
        next_instance = NewSudokuGrid(next_grid, n_rows, n_cols, next_move)
        # Update the grid
        next_instance.update_grid()
        print('Next grid (loop):', np.array(next_instance.grid))
        # Check the direction
        next_instance.define_direction()
        # If the direction is backtrack, pop the last instance from the frontier and remove the move from the instance
        if next_instance.direction == 'backtrack':
            # This is the hard part
            # If the next instance needs to back track, the last instance needs to have its output move removed from the working grid
            # Then the last instance needs to be updated and the direction needs to be rechecked
            # If the direction is now backtrack, the last instance needs to be popped from the frontier, 
            # then the output from the previous instance needs to be removed from its working grid, and so on 
            # until the direction is down
            new_direction = frontier[-1].remove_move(frontier[-1].next_move())
            while new_direction == 'backtrack':
                frontier.pop()
                new_direction = frontier[-1].remove_move(frontier[-1].next_move())
            # Once the direction is down, redefine the next move
            next_move = frontier[-1].next_move()
            next_grid = frontier[-1].grid
            #print(np.array(next_grid))
        # If the direction is down, add the instance to the frontier and update the next move
        else:
            frontier.append(next_instance)
            solved = next_instance.solved
            if solved == True:
                return next_instance.grid 
            else:
                next_move = next_instance.next_move()

if __name__ == "__main__":
    print(wavefront_solver(grid9, 3, 3))
            

        