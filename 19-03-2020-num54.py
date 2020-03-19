# Implement an efficient sudoku solver
# School case usage of backtracking!

def check(grid, x, y, k):
    t = grid[(y//3)*3][(x//3)*3:(x//3 + 1)*3] + grid[(y//3)*3+1][(x//3)*3:(x//3 + 1)*3] + grid[(y//3)*3 + 2][(x//3)*3:(x//3 +1)*3]
    return ((k not in grid[y]) and (k not in [grid[l][x] for l in range(9)]) and (k not in t)) 

def solver(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == None:
                for k in range(9):
                    if check(grid, j, i, k+1):
                        grid[i][j] = k + 1
                        result = solver(grid)
                        #print(result) 
                        if result != None: 
                            return result # Propagate the solution to the first call if a solution is found
                 # If no number works for this case, propagate (backtracking) the fact that this solution won't work to previous recursive call and prune the entire subtree
                grid[i][j] = None
                return None
    return grid # case for when the solver reach the end of the grid i.e he found a solution!



test1 = [[None for _ in range(9)] for _ in range(9)]
test1[0][1] = 3
test1[1][1] = 2
test1[1][3] = 9
test1[1][5] = 6
test1[1][6] = 3
test1[2][1] = 6
test1[2][3] = 4
test1[2][5] = 2
test1[2][7] = 9
test1[3][0] = 1
test1[3][4] = 9
test1[3][6] = 4
test1[4][2] = 8
test1[4][3] = 1
test1[4][5] = 3
test1[4][6] = 5
test1[5][2] = 5
test1[5][4] = 7
test1[5][8] = 3
test1[6][1] = 5
test1[6][3] = 3
test1[6][5] = 1
test1[6][7] = 6
test1[7][2] = 4
test1[7][3] = 6
test1[7][5] = 7
test1[7][7] = 3
test1[8][7] = 8
print(test1)

print(solver(test1))

