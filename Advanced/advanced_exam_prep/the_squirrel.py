def check_val_indices(r, c):
    if 0 <= r < size and 0 <= c < size:
        return True


size = int(input())
commands = input().split(", ")
field = []
squirrel = []
hazelnuts = 0
last_position = 0
iteration = 0
win = False

directions = {
    "up": lambda r, c: [(r - 1), c],
    "down": lambda r, c: [(r + 1), c],
    "left": lambda r, c: [r, (c - 1)],
    "right": lambda r, c: [r, (c + 1)],
}

for row in range(size):
    line = [letter for letter in input()]
    field.append(line)
    if "s" in line:
        squirrel.append(row)
        squirrel.append(line.index("s"))

for command in commands:
    squirrel = directions[command](*squirrel)
    if not check_val_indices(squirrel[0], squirrel[1]):
        print(f"The squirrel is out of the field.")
        break

    if iteration > 0:
        field[last_position[0]][last_position[1]] = "*"

    current_pos = field[squirrel[0]][squirrel[1]]
    last_position = squirrel
    if current_pos == "h":
        hazelnuts += 1
        if hazelnuts == 3:
            win = True
            break
    elif current_pos == "t":
        print(f"Unfortunately, the squirrel stepped on a trap...")
        break

    iteration += 1

if win:
    if hazelnuts == 3:
        print(f"Good job! You have collected all hazelnuts!")
    else:
        print(f"There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")