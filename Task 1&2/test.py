import random
import numpy as np
import copy
import time
import argparse
import matplotlib.pyplot as plt
#Grids 1-4 are 2x2
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
 
grid7 = [
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 1],
        [3, 6, 9, 0, 8, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 6, 8, 0, 0],
        [0, 0, 0, 1, 3, 0, 0, 0, 9],
        [4, 0, 5, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 6, 0, 0, 7, 0, 0, 0],
        [1, 0, 0, 3, 4, 0, 0, 0, 0]]
 
grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6, 2, 3), (grid7, 3, 3)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''
parser = argparse.ArgumentParser()
parser.add_argument('--explain', action='store_true',
                    help='Print out a set of instructions for solving the Sudoku ')
parser.add_argument('--profile', action='store_true',
                    help='Measures the performance of the solver(s) in terms of time for grids of different size and difficulties')
parser.add_argument('--hint', type=int, help='Returns a grid with N values filled in')
args = parser.parse_args()
 
def check_section(section, n):
 
    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n+1)]):
        return True
    return False
 
def get_squares(grid, n_rows, n_cols):
 
    squares = []
    for i in range(n_cols):
        rows = (i*n_rows, (i+1)*n_rows)
        for j in range(n_rows):
            cols = (j*n_cols, (j+1)*n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square +=line
            squares.append(square)
 
 
    return(squares)
 
def possible_col_values(grid, row_no, column_no):
# form a list of possible values that could fill an empty cell
    possible_values = list(range(1, len(grid)+1))
   
# when code finds an empty cell, remove the values from that column from the list of possible values as the cell cannot be any of those
    if grid[row_no][column_no] == 0:
        for i in range(len(grid)):
            if grid[i][column_no] in possible_values:
                possible_values.remove(grid[i][column_no])
        return possible_values
    else:
        return None
 
 
 
 
def possible_row_values(grid, row_no, column_no):
    possible_values = list(range(1, len(grid)+1))
   
# when code finds an empty cell, remove the values from that row from the list of possible values as the cell cannot be any of those
    if grid[row_no][column_no] == 0:
        for i in range(len(grid)):
            if grid[row_no][i] in possible_values:
                possible_values.remove(grid[row_no][i])
        return possible_values
    else:
        return None
 
 
def possible_square_values(grid, n_rows, n_cols, row_no, column_no):
    possible_values = list(range(1, len(grid)+1))
    square = get_squares(grid, n_rows, n_cols)
# when code finds an empty cell, remove the values from that square from the list of possible values as the cell cannot be any of those
    if grid[row_no][column_no] == 0:
# find square that the empty cell is located in
        find_square = (row_no//n_rows)*n_rows + column_no//n_cols
     
        square_found = square[find_square]
        for i in square_found:
            if i in possible_values:
                possible_values.remove(i)
        return possible_values
    else:
        return None
"""
grid5 = [
         [1, 0, 0, 2],
         [0, 0, 1, 0],
         [0, 1, 0, 4],
         [0, 0, 0, 1]]
         
 
print(possible_square_values(grid5, 2, 2, 0 , 1))
 
 
"""
def final_grid_poss_values(grid, n_rows, n_cols, row_no, column_no):
#this function is to form a list of possible values for the empty cell, based off of the above functions finding the possible values for the given square, column and row
   
#if it comes across a number rather than a zero, return None
    if grid[row_no][column_no] != 0:
        return None
    possible_square = possible_square_values(grid, n_rows, n_cols, row_no, column_no)
    if possible_square == None:
        return None
    possible_column = possible_col_values(grid, row_no, column_no)
    if possible_column == None:
        return None
    possible_row = possible_row_values(grid, row_no, column_no)
    if possible_row == None:
        return None
    if grid[row_no][column_no] != 0:
        return None
    final_possible_values = []
#loop through all possible values for a given cell and find the common values for the cell and store them in the final possible values list    
    for i in possible_row:   
        if i in possible_column:
            if i in possible_square:
                final_possible_values.append(i)
   
    return final_possible_values
       
 
   
 
        
"""
grid5 = [
         [1, 0, 0, 2],
         [0, 0, 1, 0],
         [0, 1, 0, 4],
         [0, 0, 0, 1]]
          
print("Possible values for specfifed location",final_grid_poss_values(grid5, 2, 2, 0, 1))
"""
 
 
 
def listoflist(grid, n_rows, n_cols):
#creating a list of lists of lists which is the list of the possible values within the list of the rows within the list of the actual grid itself
    combo = n_rows*n_cols
   
    new_grid = copy.deepcopy(grid) # keep in mind deep copy
   
    for a in range(combo):
        for b in range(combo):
            if new_grid[a][b] == 0:
                final_possible_values = final_grid_poss_values(grid, n_rows, n_cols, a, b)
                new_grid[a][b] = final_possible_values
    return new_grid
               
             
 
grid5 = [
         [1, 0, 0, 2],
         [0, 0, 1, 0],
         [0, 1, 0, 4],
         [0, 0, 0, 1]]       
 
print('possible values for: USER CHANGE ACCORDINGLY HERE: grid 5:', listoflist(grid5, 2, 2))
 
 
# the function below records the index of the empty space with the lowest possible number of different numbers to fill it
# so that the solver can work iteratively by finding locations in smaller grids with only a single possible value to fill it in the list of lists of lists
# and then eliminating that value from the location's row/column/square to solve the grid more efficiently and faster
# low_col and low_row mark the exact location of the cell with the lowest number of possible solutions
def solving_index(grid,n_rows,n_cols):
    combo = n_rows*n_cols
    #grid_solve = copy.deepcopy(grid)
    grid_sol = listoflist(grid, n_rows, n_cols)
    low_col = 0
    low_row = 0
    lowest = combo
    for a in range(combo):
        for b in range(combo):
            if isinstance(grid_sol[a][b], list):
                if len(grid_sol[a][b]) < lowest:
                    lowest = len(grid_sol[a][b])
                    low_row = a
                    low_col = b
   
    return low_row, low_col, grid_sol[low_row][low_col]
 
#print(solving_index(grid7, 3, 3))
 
def find_empty(grid):
                '''
                This function returns the index (i, j) to the first zero element in a sudoku grid
                If no such element is found, it returns None
                args: grid
                return: A tuple (i,j) where i and j are both integers, or None
                '''
 
                for i in range(len(grid)):
                                row = grid[i]
                                for j in range(len(row)):
                                                if grid[i][j] == 0:
                                                                return (i, j)
 
                return None
 
 
# this solver works so that it can perform on larger grids where the cell with the lowest possible
# number of solutions is not necessarily just one. This wavefront propagation method follows a 'backtracking' method where if
# the empty cell with the lowest possible numbers are two possible options rather than one, it will chose the first one and then
# continue to solve the grid. If this proves wrong, the solver will backtrack to the most recent filled space where the code diverged
# and instead selects the second value and effectively deletes the incorrect code that just ran and then re-runs the code with the second value option etc until the grid is correctly solved.
def wavefront_solver(grid,n_rows,n_cols):
    combo = n_rows*n_cols
    grid_solve = copy.deepcopy(grid)
    visited = []
   
    while find_empty(grid_solve) != None :
        low_row, low_col, pos = solving_index(grid_solve, n_rows, n_cols)
        if len(pos) > 0:
            grid_solve[low_row][low_col] = pos[0]
            visited.append([low_row,low_col,pos])
        else:
            while(len(visited[-1][2]) == 1):
                row = visited[-1][0]
                col = visited[-1][1]
                grid_solve[row][col] = 0
                del visited[-1]
            del visited[-1][2][0]
            row = visited[-1][0]
            col = visited[-1][1]
            grid_solve[row][col] = visited[-1][2][0]
               
                
                
                
                
                
            
    
    
    print(grid_solve)
   
wavefront_solver(grid7,3,3)