key = input()

while True:
    command = input()

    if command == "Generate":
        break

    command_args = command.split(">>>")
    action = command_args[0]

    if action == "Contains":
        substring = command_args[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif action == "Flip":
        action2 = command_args[1]
        start_index = int(command_args[2])
        end_index = int(command_args[3])
        if action2 == "Upper":
            substring = key[start_index:end_index]
            key = key[:start_index] + substring.upper() + key[end_index:]
            print(key)
        else:
            substring = key[start_index:end_index]
            key = key[:start_index] + substring.lower() + key[end_index:]
            print(key)

    elif action == "Slice":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        key = key[0:start_index] + key[end_index:]
        print(key)

print(f"Your activation key is: {key}")