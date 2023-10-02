sequence = [int(i) for i in input().split()]

while True:
    command = input()

    if command == "End":
        break

    list_command = command.split()
    index = int(list_command[1])
    action = list_command[0]
    index2 = int(list_command[2])

    if action == "Shoot":
        if 0 <= index < len(sequence):
            sequence[index] -= index2
        if sequence[index] <= 0:
            sequence.pop(index)

    elif action == "Add":
        if 0 <= index < len(sequence):
            sequence.insert(index, index2)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        if index + index2 >= len(sequence) or index - index2 < 0:
            print("Strike missed!")
            continue
        middle = sequence[index]
        for i in range(index + 1, index + index2 + 1):
            sequence.pop(i)
        for k in range(index - 1, index - index2 -1, -1):
            sequence.pop(k)
        sequence.remove(middle)

print(*sequence, sep='|')
