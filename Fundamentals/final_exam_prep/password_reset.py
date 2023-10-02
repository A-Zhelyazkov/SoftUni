text = input()

while True:
    data = input()

    if data == "Done":
        break

    data_args = data.split()
    command = data_args[0]

    if command == "TakeOdd":
        text = text[1::2]

    elif command == "Cut":
        index = int(data_args[1])
        length = int(data_args[2])
        cut_sub = text[index:index+length:]
        text = text.replace(cut_sub, "", 1)

    elif command == "Substitute":
        substring = data_args[1]
        substitute = data_args[2]

        if substring in text:
            text = text.replace(substring, substitute)
        else:
            print(f"Nothing to replace!")
            continue
    print(text)

print(f"Your password is: {text}")