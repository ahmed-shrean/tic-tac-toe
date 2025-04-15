import sys
import infinity
def evaluate(board):
    return -1  # not written yet

def is_terminal(board):
    return not any(" " in item for row in board for item in row)

def unsigned_places(board):
    places = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                places.append((row, col))
    return places

def minmax(board, depth, maximizing_player):
    if depth == 0:
        return evaluate(board)

    if maximizing_player:
        max_value = -infinity
        for row, col in unsigned_places(board):
            board[row][col] = "x"
            value = minmax(board, depth - 1, False)
            board[row][col] = " "
            max_value = max(max_value, value)
        return max_value
    else:
        min_value = infinity
        for row, col in unsigned_places(board):
            board[row][col] = "o"
            value = minmax(board, depth - 1, True)
            board[row][col] = " "
            min_value = min(min_value, value)
        return min_value
