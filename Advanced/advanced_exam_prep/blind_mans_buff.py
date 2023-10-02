def check_val_indices(row, col):
    if 0 <= row < n and 0 <= col < m:
        return True


n, m = [int(i) for i in input().split()]

field = []
player_position = 0
moves = 0
players_touched = 0
last_position = 0
to_remove = 0
win = False
for i in range(n):
    line = input().split()
    field.append(line)
    if "B" in line:
        player_position = [i, line.index("B")]

directions = {
    "up": lambda row, col: [(row - 1), col],
    "down": lambda row, col: [(row + 1), col],
    "left": lambda row, col: [row, (col - 1)],
    "right": lambda row, col: [row, (col + 1)],
}
while True:
    command = input()

    if command == "Finish":
        break

    last_position = player_position
    player_position = directions[command](*player_position)

    if not check_val_indices(player_position[0], player_position[1]) or\
            field[player_position[0]][player_position[1]] == "O":
        player_position = last_position
        continue

    curr_position = field[player_position[0]][player_position[1]]
    moves += 1
    if to_remove:
        field[to_remove[0]][to_remove[1]] = "-"

    if curr_position == "P":
        players_touched += 1
        to_remove = player_position
        if players_touched == 3:
            win = True
            break

print(f"Game over!")
print(f"Touched opponents: {players_touched} Moves made: {moves}")