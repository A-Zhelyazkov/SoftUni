size = int(input())

submarine = 0
field = []
mines = 0
ships = 0
last_position = 0
win = False

for row in range(size):
    line = [i for i in input()]
    field.append(line)

    if "S" in line:
        submarine = [row, line.index("S")]

    for i in line:
        if i == "C":
            ships += 1

directions = {
    "up": lambda r, c: [(r - 1), c],
    "down": lambda r, c: [(r + 1), c],
    "left": lambda r, c: [r, (c - 1)],
    "right": lambda r, c: [r, (c + 1)],
}

while True:
    command = input()
    last_position = submarine
    submarine = directions[command](*submarine)
    position = field[submarine[0]][submarine[1]]

    field[last_position[0]][last_position[1]] = "-"

    if position == "-":
        continue
    elif position == "*":
        mines += 1
    elif position == "C":
        ships -= 1

    if ships == 0:
        field[submarine[0]][submarine[1]] = "S"
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break
    elif mines == 3:
        field[submarine[0]][submarine[1]] = "S"
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine[0]}, {submarine[1]}]!")
        break

for line in field:
    print(''.join(line))