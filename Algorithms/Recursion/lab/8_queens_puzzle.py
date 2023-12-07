def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def can_place_queen(row, col, rows, cols, l_diag, r_diag):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in l_diag:
        return False
    if (row + col) in r_diag:
        return False
    return True


def set_queen(row, col, board, rows, cols, l_diag, r_diag):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    l_diag.add(row-col)
    r_diag.add(col+row)


def remove_queen(row, col, board, rows, cols, l_diag, r_diag):
    board[row][col] = '-'

    rows.remove(row)
    cols.remove(col)
    l_diag.remove(row-col)
    r_diag.remove(col+row)


def find_all_variations(board, row, rows, cols, l_diag, r_diag):
    if row == 8:
        print_board(board)

    for col in range(8):
        if can_place_queen(row, col, rows, cols, l_diag, r_diag):
            set_queen(row, col, board, rows, cols, l_diag, r_diag)
            find_all_variations(board, row+1, rows, cols, l_diag, r_diag)
            remove_queen(row, col, board, rows, cols, l_diag, r_diag)
n = 8

board = []

for _ in range(n):
    board.append(['-'] * n)

find_all_variations(board, 0, set(), set(), set(), set())