from collections import deque

liters_water = int(input())
people = deque()
while True:
    name = input()

    if name == "Start":
        break

    people.append(name)

while True:
    command = input()

    if command == "End":
        break

    command_args = command.split()

    if command_args[0] == "refill":
        liters_water += int(command_args[1])

    else:
        wanted_liters = int(command_args[0])
        if wanted_liters > liters_water:
            print(f"{people.popleft()} must wait")
        else:
            liters_water -= wanted_liters
            print(f"{people.popleft()} got water")

print(f"{liters_water} liters left")