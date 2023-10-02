board = []

white_pos = []
black_pos = []
for row in range(8):
    board.append(input().split())

print(*board, sep='\n')
