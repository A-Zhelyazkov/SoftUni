to_do_list = [''] * 10
while True:
    command = input()

    if command == "End":
        break

    command_info = command.split('-')
    importance = int(command_info[0]) - 1
    task = command_info[1]

    to_do_list.pop(importance)
    to_do_list.insert(importance, task)

print([i for i in to_do_list if i != ''])

