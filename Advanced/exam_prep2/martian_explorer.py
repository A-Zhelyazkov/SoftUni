SIZE = 6

matrix = []
spaceship = []
directions = {
    "left": lambda row, col: [row, (col-1) % SIZE],
    "right": lambda row, col: [row, (col+1) % SIZE],
    "up": lambda row, col: [(row - 1) % SIZE, col],
    "down": lambda row, col: [(row + 1) % SIZE, col]

}
for n in range(SIZE):
    current_line = input().split()
    matrix.append(current_line)
    if "E" in current_line:
        spaceship.append(n)
        spaceship.append(current_line.index("E"))

commands = input().split(", ")
found_materials = set()
for command in commands:
    spaceship = directions[command](*spaceship)
    current_pos = matrix[spaceship[0]][spaceship[1]]

    if current_pos == "W":
        print(f"Water deposit found at ({spaceship[0]}, {spaceship[1]})")
        found_materials.add("W")
    elif current_pos == "C":
        print(f"Concrete deposit found at ({spaceship[0]}, {spaceship[1]})")
        found_materials.add("C")
    elif current_pos == "M":
        found_materials.add("M")
        print(f"Metal deposit found at ({spaceship[0]}, {spaceship[1]})")
    elif current_pos == "R":
        print(f"Rover got broken at ({spaceship[0]}, {spaceship[1]})")
        break

if len(found_materials) == 3:
    print("Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")