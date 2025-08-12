def show(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
            if (j + 1) % 3 == 0 and j != 8:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0 and i != 8:
            print("-" * 21)

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def check(board, number, row, col):
    for j in range(9):
        if board[row][j] == number:
            return False

    for i in range(9):
        if board[i][col] == number:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == number:
                return False

    return True

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if check(board, num, row, col):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


puzzle = [
    [8, 1, 0, 0, 5, 0, 0, 0, 0],
    [9, 0, 0, 6, 8, 2, 0, 0, 0],
    [0, 7, 5, 0, 0, 0, 0, 8, 0],

    [1, 0, 0, 0, 3, 0, 0, 0, 6],
    [3, 0, 0, 8, 4, 5, 0, 0, 1],
    [2, 0, 0, 0, 6, 0, 0, 3, 4],

    [0, 2, 0, 9, 0, 0, 3, 6, 0],
    [0, 0, 0, 5, 2, 6, 0, 0, 7],
    [0, 0, 0, 0, 1, 0, 0, 5, 2]
]

print("Sudoku board before resolving:\n")
show(puzzle)

if solve(puzzle):
    print("\n Resolved Sudoku board:\n")
    show(puzzle)
else:
    print("Quitting.....Can't solve it")