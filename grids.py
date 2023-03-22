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
         [0,0,0,0,0,8,0,6,0]]

grid8 = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,3,0,8,5],
         [0,0,1,0,2,0,0,0,0],
         [0,0,0,5,0,7,0,0,0],
         [0,0,4,0,0,0,1,0,0],
         [0,9,0,0,0,0,0,0,0],
         [5,0,0,0,0,0,0,7,3],
         [0,0,2,0,1,0,0,0,0],
         [0,0,0,0,4,0,0,0,9]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6, 2, 3), (grid7,3,3), (grid8,3,3)]

# Something to look into is plotting the performance of the solver against the 
# number of zeros in the grid.  This is a good way to see how the solver performs
# Its also a good was to see how different mods impact the performance of the solver
# Currently, grid8 takes about 30 seconds to solve on my computer


zero_count = 0
for row in grid7:
    zero_count += row.count(0)
print(zero_count)
