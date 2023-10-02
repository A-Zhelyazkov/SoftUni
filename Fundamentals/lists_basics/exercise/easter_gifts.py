gifts = input().split()
final_list = []
while True:
    command = input()
    command_info = command.split()
    action = command_info[0]
    gift = command_info[1]
    if command == "No Money":
        break

    if action == "OutOfStock":
        for i in range(len(gifts)):
            if gift == gifts[i]:
                gifts[i] = "None"
    elif action == "Required":
        index = int(command_info[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift
    elif action == "JustInCase":
        gifts.pop()
        gifts.append(gift)

for el in gifts:
    if el == "None":
        continue
    else:
        final_list.append(el)
print(' '.join(final_list))
