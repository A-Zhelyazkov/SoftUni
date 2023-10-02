array = [int(i) for i in input().split()]

while True:
    command = input()

    if command == "end":
        break

    command_list = command.split()
    action = command_list[0]

    if action == "swap":
        index1 = int(command_list[1])
        index2 = int(command_list[2])
        array[index1], array[index2] = array[index2], array[index1]
    elif action == "multiply":
        index1 = int(command_list[1])
        index2 = int(command_list[2])
        result_multi = array[index1] * array[index2]
        array[index1] = result_multi
    elif action == "decrease":
        for i in range(len(array)):
            array[i] -= 1

print(*array, sep=', ')