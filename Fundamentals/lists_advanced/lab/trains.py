train_length = int(input())
train = [0] * train_length

while True:
    command = input()

    if command == "End":
        break

    command_info = command.split()
    action = command_info[0]

    if action == "add":
        people = int(command_info[1])
        train[-1] += people

    elif action == "insert":
        index = int(command_info[1])
        people = int(command_info[2])
        train[index] += people

    elif action == "leave":
        index = int(command_info[1])
        people = int(command_info[2])
        train[index] -= people

print(train)
