phones_seq = input().split(", ")

while True:
    command = input()

    if command == "End":
        break

    command_args = command.split(" - ")
    action, phone = command_args[0], command_args[1]

    if action == "Add":
        if phone not in phones_seq:
            phones_seq.append(phone)
        else:
            continue

    elif action == "Remove":
        if phone in phones_seq:
            phones_seq.remove(phone)
        else:
            continue

    elif action == "Bonus phone":
        phone = phone.split(":")
        old_phone = phone[0]
        new_phone = phone[1]
        if old_phone in phones_seq:
            index_old = phones_seq.index(old_phone)
            phones_seq.insert(index_old + 1, new_phone)
        else:
            continue

    elif action == "Last":
        if phone in phones_seq:
            phones_seq.remove(phone)
            phones_seq.append(phone)

        else:
            continue

print(', '.join(phones_seq))