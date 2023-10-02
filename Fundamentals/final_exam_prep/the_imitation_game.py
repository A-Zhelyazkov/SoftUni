message = input()

while True:
    command = input()

    if command == "Decode":
        break

    command_args = command.split("|")
    action = command_args[0]
    arg1 = command_args[1]

    if action == "Move":
        num_of_letters = int(arg1)
        letters_to_be_moved = message[0:num_of_letters]
        message = message[num_of_letters:] + letters_to_be_moved

    elif action == "Insert":
        index = int(arg1)
        value = command_args[2]
        first_part = message[:index]
        message = first_part + value + message[index:]

    elif action == "ChangeAll":
        substring = arg1
        value = command_args[2]
        message = message.replace(substring, value)

print(f"The decrypted message is: {message}")



