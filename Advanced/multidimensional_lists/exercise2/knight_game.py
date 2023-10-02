board_size = int(input())

board = [list(input()) for _ in range(board_size)]

possible_moves = (
    (-2, -1),
    (-2, 1),
    (2, 1),
    (2, -1),
    (-1, -2),
    (-1, 2),
    (1, 2),
    (1, -2),
)

removed_knights = 0

