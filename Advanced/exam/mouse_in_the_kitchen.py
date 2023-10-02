def check_wall(direction):
    next_step = directions[command](*mouse)
    if check_indices(next_step, n, m):
        if field[next_step[0]][next_step[1]] == "@":
            return True


def check_indices(position, r, c):
    if 0 <= position[0] < r and 0 <= position[1] < c:
        return True


n, m = [int(i) for i in input().split(",")]

field = []
mouse = 0
last_position = 0
cheeses = 0

for row in range(n):
    line = [i for i in input()]
    field.append(line)
    if "M" in line:
        mouse = [row, line.index("M")]
    for i in line:
        if i == "C":
            cheeses += 1

directions = {
    "up": lambda r, c: [(r - 1), c],
    "down": lambda r, c: [(r + 1), c],
    "left": lambda r, c: [r, (c - 1)],
    "right": lambda r, c: [r, (c + 1)],
}

while True:
    command = input()

    if command == "danger":
        print("Mouse will come back later!")
        break

    if check_wall(command):
        continue

    last_position = mouse
    mouse = directions[command](*mouse)

    if not check_indices(mouse, n, m):
        print("No more cheese for tonight!")
        field[last_position[0]][last_position[1]] = "M"
        break

    position = field[mouse[0]][mouse[1]]

    field[last_position[0]][last_position[1]] = "*"

    if position == "C":
        cheeses -= 1
        if cheeses == 0:
            field[mouse[0]][mouse[1]] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif position == "T":
        print("Mouse is trapped!")
        field[mouse[0]][mouse[1]] = "M"
        break
    elif position == "@":
        continue

for line in field:
    print(''.join(line))



