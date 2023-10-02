import os

curr_dir = os.path.dirname(os.path.abspath(__file__))


while True:
    command = input()

    if command == "End":
        break

    command_args = command.split("-")
    action, file_name = command_args[0], command_args[1]
    curr_file = os.path.join(curr_dir, file_name)
    if action == "Create":
        with open(curr_file, "w")as file:
            pass

    elif action == "Add":
        content = command_args[2]
        with open(curr_file, "a") as file:
            file.write(f"{content}\n")

    elif action == "Replace":
        old = command_args[2]
        new = command_args[3]
        try:
            with open(curr_file, "r+") as file:
                text = file.read()
                text = text.replace(old, new)
                file.seek(0)
                file.write(text)

        except FileNotFoundError:
            print(f"An error occurred")

    elif action == "Delete":
        if os.path.isfile(curr_file):
            os.remove(curr_file)
        else:
            print("An error occurred")