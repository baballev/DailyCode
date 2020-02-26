# Conway's game of life
# N number of steps

def gol(starting_cells, N):
    start_y = [y for x, y in starting_cells]
    start_x = [x for x, y in starting_cells]
    min_y, max_y = min(start_y), max(start_y)
    min_y, max_y = min(start_x), max(start_x)

    board = [[0 for x in range(max_x - min_x)] for j in range(max_y - min_y)]
    for x, y in starting_cells:
        board[y - min_y][x - min_x] = 1
        # 0 = void, 1 = alive, 2 = dead
    display(board)

    for i in range(N):
        update(board)


        display(board)


def display(board):
    for row in board:
        out = ""
        for col in row:
            if col == 0: out += " "
            elif col == 1: out += "*"
            else: out += "."
        print(out)

def update(board, min_y, max_y, min_y, max_y):
    cache = []
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col == 1:
                s = #TODO
                if s < 2 or s 3>:
                    cache.append((x, y))

    # ToDo: Make board bigger/ smaller and be careful to coordinates that change
    for x, y in cache:
        if board[y][x] == 1: board[y][x] = 2
        else: board[y][x] = 1
