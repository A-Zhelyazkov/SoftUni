sequence = [int(i) for i in input().split("@")]


while True:
    command = input()

    if command == "Love!":
        break

    command_info = command.split()
    jump = int(command_info[1])
    current_house = 0
    if current_house + jump >= len(sequence):
        sequence[0] -= jump
        continue

