# Conway's game of life
# N number of steps

def gol(starting_cells, N):
    # Init
    start_y = [y for x, y in starting_cells]
    start_x = [x for x, y in starting_cells]
    min_y, max_y = min(start_y), max(start_y)
    min_x, max_x = min(start_x), max(start_x)

    board = [[0 for x in range(max_x - min_x + 1)] for j in range(max_y - min_y + 1)]
    for x, y in starting_cells:
        board[y - min_y][x - min_x] = 1
        # 0 = dead, 1 = alive
    display(board)

# Life cycles
    for i in range(N):
        board = update(board)
        display(board)

def display(board):
    width = len(board[0])
    print("=" * width)
    for row in board:
        out = ""
        for col in row:
            if col: out += "*"
            else: out += "."
        print(out)
    print("=" * width)
    print("\n")

def update(board):
    width, height = len(board[0]), len(board)
    cache = []
    for y in range(-1, height + 1):
        for x in range(-1, width + 1):
            # Count the number of neighbors
            s = 0
            if x > 0:
                if y != -1 and y != height: s += board[y][x-1]
                if y > 0: s += board[y-1][x-1]
                if y < height-1: s += board[y+1][x-1]
            if x < width - 1:
                if y != -1 and y != height: s += board[y][x+1]
                if y > 0: s += board[y-1][x+1]
                if y < height-1: s += board[y+1][x+1]
            if y > 0 and x != -1 and x != width: s += board[y-1][x]
            if y < height - 1 and x != -1 and x != width: s += board[y+1][x]

            if y >= 0 and y < height and x >= 0 and x < width and board[y][x]:
                if s < 2 or s > 3:
                    cache.append((x, y))
            else:
                if s == 3: cache.append((x, y))


    left, right, up, down = False, False, False, False
    for x, y in cache:
        if x == -1: left = True
        elif x == width: right = True
        if y == -1: up = True
        elif y == height: down = True

    if down: board.append([0 for i in range(width)])
    if up: board = [[0 for i in range(width)]] + board
    if right: board = [[x for x in board[y]] + [0] for y in range(len(board))]
    if left: board = [[0] + [x for x in board[y]] for y in range(len(board))]

    for (x, y) in cache:
        new_x = x + left
        new_y = y + up
        if board[new_y][new_x]: board[new_y][new_x] = 0
        else: board[new_y][new_x] = 1
    return board


# TESTS
#gol([(0, 0), (1, 0), (2, 0)], 10)
gol([(0, -1), (1, -1), (2, -1), (2, -2), (1, -3)], 100)
