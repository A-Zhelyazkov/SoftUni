text = input()

while True:
    command = input()
    if command == "End":
        break

    command_args = command.split()

    action = command_args[0]

    if action == "Translate":
        char = command_args[1]
        replacement = command_args[2]
        text = text.replace(char, replacement)
        print(text)

    elif action == "Includes":
        substring = command_args[1]
        if substring in text:
            print("True")
        else:
            print(f"False")

    elif action == "Start":
        substring = command_args[1]
        if text.startswith(substring):
            print("True")
        else:
            print(f"False")

    elif action == "Lowercase":
        text = text.lower()
        print(text)

    elif action == "FindIndex":
        char = command_args[1]
        for i in range(len(text) - 1, 0, -1):
            if text[i] == char:
                print(i)
                break

    elif action == "Remove":
        start_index = int(command_args[1])
        count = int(command_args[2])
        text = text[:start_index] + text[start_index+count:]
        print(text)

