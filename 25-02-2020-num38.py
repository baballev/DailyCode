# Given N, find the number of possible arrangements where you put N queens on
# the board without having one threatening another one.
# Let's use Backtracking

def number_of_arrangements(N, board=[]):
    if len(board) == N:
        return 1

    count = 0
    for j in range(N):
        board.append(j)
        if is_valid(board):
            count += number_of_arrangements(N, board)
        board.pop()
    return count

def is_valid(board):
    current_row = len(board) - 1
    current_col = board[-1]
    for k, j in enumerate(board[:-1]):
        if current_col == j or current_col == j + (current_row - k) or current_col == j - (current_row - k):
            return False
    return True
print(number_of_arrangements(8, []))
