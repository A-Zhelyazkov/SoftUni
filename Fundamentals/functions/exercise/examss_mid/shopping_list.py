groceries = input().split("!")

while True:
    command = input()

    if command == "Go Shopping!":
        break

    command_info = command.split()
    action = command_info[0]
    item = command_info[1]

    if action == "Urgent":
        if item in groceries:
            continue
        else:
            groceries.insert(0, item)

    if action == "Unnecessary":
        if item not in groceries:
            continue
        else:
            groceries.remove(item)

    if action == "Correct":
        new_item = command_info[2]
        if item not in groceries:
            continue
        else:
            idx = 0
            for i in range(len(groceries)):
                if groceries[i] == item:
                    idx = i
            groceries[idx] = new_item

    if action == "Rearrange":
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
        else:
            continue

print(*groceries, sep=', ')


