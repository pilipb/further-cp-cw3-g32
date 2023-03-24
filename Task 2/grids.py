# Create a difficult 9x9 sodoku grid where empty cells are represented by 0
grid1 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]

grid2 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 0, 4],
		[3, 4, 2, 1]]

grid3 = [
		[1, 0, 4, 2],
		[4, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid4 = [
		[1, 0, 4, 2],
		[0, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid5 = [
		[1, 0, 0, 2],
		[0, 0, 1, 0],
		[0, 1, 0, 4],
		[0, 0, 0, 1]]

grid6 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]

grid7 = [[6,0,8,0,0,0,0,0,0],
         [2,0,0,8,0,0,4,0,0],
         [0,1,0,0,0,2,5,0,0],
         [0,3,0,0,0,1,9,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,2,0,0,7,0,0,4,0],
         [0,4,0,0,0,9,0,3,0],
         [0,6,3,1,0,0,0,7,0],
         [0,0,0,0,0,8,0,1,0]]
# This one can take slightly longer time to solve if row 9 column 8 is 6
# Must have something to do with the position of the final grid in the solution space

grid8 = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,3,0,8,5],
         [0,0,1,0,2,0,0,0,0],
         [0,0,0,5,0,7,0,0,0],
         [0,0,4,0,0,0,1,0,0],
         [0,9,0,0,0,0,0,0,0],
         [5,0,0,0,0,0,0,7,3],
         [0,0,2,0,1,0,0,0,0],
         [0,0,0,0,4,0,0,0,8]]
# This is the very long one ^^^ if you make the bottom 
# right hand corner 9, it will take a while to solve
# This can be seen from its solution - the first row is [9,8,7,6,5,4,3,2,1] (The far end of the solution space)
# With an 8 in the bottom right hand corner, it takes 167 recursive calls to solve
# With a 9 in the bottom right hand corner, it takes 45267 recursive calls to solve
# This shows that number of missing cells is of little importance to the time taken to solve
# Rather the number of recursive calls is the most important factor which in turn is dependent on the position of the grid in the solution space
grid9 = [[9,0,0,5,0,4,0,1,0],
         [4,0,0,0,0,9,6,0,3],
         [8,1,6,2,7,0,0,0,0],
         [0,0,5,6,8,0,7,0,0],
         [1,0,0,0,3,0,4,5,2],
         [0,9,7,0,0,2,0,0,1],
         [6,3,0,7,0,0,5,9,0],
         [0,0,9,1,4,0,3,0,0],
         [5,2,0,0,0,6,0,8,7]]

grid10 = [[0,3,0,0,9,0,0,0,4],
          [6,0,4,0,0,2,0,0,0],
          [0,0,0,0,6,4,1,7,5],
          [0,0,0,6,0,0,3,0,2],
          [0,0,0,0,0,5,0,9,8],
          [7,8,1,0,0,0,0,0,0],
          [0,5,0,0,4,3,0,0,7],
          [0,0,9,8,0,0,0,0,0],
		  [0,0,0,0,7,1,2,4,0]]

grid11 = [[0,3,0,0,0,0,0,0,6],
		  [0,5,0,0,6,0,7,0,0],
		  [0,0,0,4,0,0,0,0,0],
		  [9,0,0,8,0,0,0,0,0],
		  [2,4,8,0,0,0,0,9,0],	
		  [0,0,0,1,0,0,0,4,0],
		  [0,0,5,6,7,0,9,0,0],
		  [0,0,0,9,0,8,0,0,1],
		  [0,0,9,0,0,0,0,5,2]]

grid12 = [[6,0,0,0,0,5,0,0,0],
		  [0,5,0,0,4,9,0,0,0],
		  [0,0,0,1,0,0,0,0,8],
		  [0,6,5,0,0,4,0,0,0],
		  [0,0,4,0,0,6,1,5,2],
		  [0,0,0,0,0,7,0,0,0],
		  [0,7,0,0,0,0,6,0,0],
		  [0,0,0,0,0,0,0,3,0],
		  [0,2,0,0,0,0,9,0,0]]

grid13 = [[0,0,0,0,0,0,0,0,1],
		  [5,0,0,0,9,0,0,0,6],
		  [0,0,0,4,0,0,3,8,0],
		  [0,0,5,0,0,0,0,0,0],
		  [0,1,0,0,2,0,7,0,0],
		  [2,0,0,0,3,0,0,0,5],
		  [6,9,0,0,0,8,0,0,0],
		  [0,0,0,0,0,0,8,0,0],
		  [0,0,7,0,0,0,0,5,0]]




grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6, 2, 3), 
         (grid7,3,3), (grid8,3,3), (grid9,3,3), (grid10,3,3), (grid11,3,3), (grid12,3,3), (grid13,3,3)]
'''
Something to look into is plotting the performance of the solver against the 
number of zeros in the grid.  This is a good way to see how the solver performs
Its also a good was to see how different mods impact the performance of the solver
Currently, grid8 takes about 30 seconds to solve on my computer
'''
# print the number of zeros in the each grid
"""
for grid in grids:
    zeros = sum([row.count(0) for row in grid[0]])
    print("Number of zeros in grid: ", zeros)
    grid_size = len(grid[0])**2
    print("Number of values in grid: ", grid_size)
    print(grid_size - zeros)
    
"""


    


