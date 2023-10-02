def check_valid_index(a, b):
    if rows > int(a) >= 0 and columns > int(b) >= 0:
        return True
    else:
        return False


rows, columns = [int(i) for i in input().split()]

matrix = [[i for i in input().split()] for _ in range(rows)]

while True:
    command = input()

    if command == "END":
        break

    command_args = command.split()

    if command_args[0] != "swap" or len(command_args) != 5:
        print("Invalid input!")
        continue

    if check_valid_index(command_args[1], command_args[2]) and check_valid_index(command_args[3], command_args[4]):
        pass
    else:
        print("Invalid input!")
        continue
    point_1 = matrix[int(command_args[1])][int(command_args[2])]
    point_2 = matrix[int(command_args[3])][int(command_args[4])]

    matrix[int(command_args[1])][int(command_args[2])] = point_2
    matrix[int(command_args[3])][int(command_args[4])] = point_1

    for i in matrix:
        print(*i)

