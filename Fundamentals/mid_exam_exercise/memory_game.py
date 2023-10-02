sequence_of_el = input().split()
moves = 0
while True:
    command = input()
    if len(sequence_of_el) == 0:
        break
    if command == "end":
        break
    moves += 1
    indexes = command.split()
    index1 = int(indexes[0])
    index2 = int(indexes[1])
    if (index1 < 0 or index2 < 0) or (index1 == index2) or (index1 >= len(sequence_of_el) or index2 >= len(sequence_of_el)):
        half_list = len(sequence_of_el) // 2
        sequence_of_el.insert(half_list, f"-{moves}a")
        sequence_of_el.insert(half_list, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
        continue
    pick1 = sequence_of_el[index1]
    pick2 = sequence_of_el[index2]

    if pick1 == pick2:
        print(f"Congrats! You have found matching elements - {sequence_of_el[index2]}!")
        sequence_of_el.remove(pick1)
        sequence_of_el.remove(pick2)
    else:
        print("Try again!")


if sequence_of_el:
    print("Sorry you lose :(")
    print(*sequence_of_el)
else:
    print(f"You have won in {moves} turns!")
