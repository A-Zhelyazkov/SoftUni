pirate_ship = [int(i) for i in input().split(">")]
war_ship = [int(i) for i in input().split(">")]
max_hp = int(input())

while True:
    command = input()

    if command == "Retire":
        break

    command_args = command.split()
    action = command_args[0]

    if action == "Fire":
        index = int(command_args[1])
        damage = int(command_args[2])
        if 0 <= index < len(war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
        else:
            continue

    elif action == "Defend":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        damage = int(command_args[3])
        if 0 <= start_index <= end_index and 0 <= end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif action == "Repair":
        index = int(command_args[1])
        health = int(command_args[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_hp:
                pirate_ship[index] = max_hp

    elif action == "Status":
        count_sections = 0
        for i in pirate_ship:
            if i < max_hp * 0.2:
                count_sections += 1
        print(f"{count_sections} sections need repair.")

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(war_ship)}")