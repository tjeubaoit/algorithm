#!/bin/python

import sys


n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
    grid_t = str(input().strip())
    grid.append(grid_t)
    
m = [[0 for j in range(n)] for i in range(n)]
for i in range(1, n-1):
    for j in range(1, n-1):
        cell = grid[i][j]
        if m[i][j] != 0: continue
        
        adjacent_cells = [grid[i-1][j], grid[i+1][j], grid[i][j-1], grid[i][j+1]]
        cavity = True
        for c in adjacent_cells:
            if int(c) >= int(cell):
                cavity = False
                break
        if cavity:
            m[i][j] = 1
            m[i+1][j] = -1
            m[i][j+1] = -1
            
for i in range(n):
    r = ''
    for j in range(n):
        r += 'X' if m[i][j] == 1 else grid[i][j]
    print(r)
