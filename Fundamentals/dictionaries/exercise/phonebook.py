phonebook = {}
while True:
    command = input()

    if command.isdigit():
        break

    name, phone = command.split("-")

    phonebook[name] = phone

for _ in range(int(command)):
    name = input()

    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
