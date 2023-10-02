def check_valid_indices(row, col):
    if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix) - 1:
        return True
    else:
        return False


rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(i) for i in input().split()])

while True:
    command = input()

    if command == "END":
        break

    command = command.split()
    action = command[0]
    row, col, value = int(command[1]), int(command[2]), int(command[3])

    if not check_valid_indices(row, col):
        print("Invalid coordinates")
        continue

    if action == "Add":
        matrix[row][col] += value

    elif action == "Subtract":
        matrix[row][col] -= value

for i in matrix:
    print(*i)