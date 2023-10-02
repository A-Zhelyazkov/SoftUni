names_seq = input().split(", ")
blacklist_count = 0
lost_count = 0
while True:
    command = input()

    if command == "Report":
        break

    command_args = command.split()
    action, first_arg = command_args[0], command_args[1]

    if action == "Blacklist":
        if first_arg in names_seq:
            print(f"{first_arg} was blacklisted.")
            index = names_seq.index(first_arg)
            names_seq[index] = "Blacklisted"
            blacklist_count += 1
        else:
            print(f"{first_arg} was not found.")

    elif action == "Error":
        index = int(first_arg)
        if 0 <= index < len(names_seq):
            if names_seq[index] != "Blacklisted" and names_seq[index] != "Lost":
                print(f"{names_seq[index]} was lost due to an error.")
                names_seq[index] = "Lost"
                lost_count += 1
        else:
            continue

    elif action == "Change":
        index = int(first_arg)
        new_name = command_args[2]
        if 0 <= index < len(names_seq):
            if names_seq[index] != "Blacklisted" and names_seq[index] != "Lost":
                print(f"{names_seq[index]} changed his username to {new_name}.")
                names_seq[index] = new_name
        else:
            continue

print(f"Blacklisted names: {blacklist_count}")
print(f"Lost names: {lost_count}")
print(*names_seq)

