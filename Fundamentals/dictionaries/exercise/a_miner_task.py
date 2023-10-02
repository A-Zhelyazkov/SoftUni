resources = {}
counter = 0
while True:
    counter += 1
    command = input()
    if command == "stop":
        break

    if counter % 2 != 0:
        last_material = command
        if command not in resources:
            resources[command] = 0

    else:
        resources[last_material] += int(command)

for key, value in resources.items():
    print(f"{key} -> {value}")

