initial_energy = int(input())
wins = 0
left_energy = True
while True:
    command = input()

    if command == "End of battle":
        break
    if wins % 3 == 0:
        initial_energy += wins

    energy_used = int(command)
    if energy_used > initial_energy:
        left_energy = False
        break
    wins += 1
    initial_energy -= energy_used

if left_energy:
    print(f"Won battles: {wins}. Energy left: {initial_energy}")
else:
    print(f"Not enough energy! Game ends with {wins} won battles and {initial_energy} energy")

