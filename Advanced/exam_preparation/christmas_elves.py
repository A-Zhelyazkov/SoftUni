from collections import deque

elves_energy = deque(int(i) for i in input().split())
num_of_material_in_box = deque(int(i) for i in input().split())

total_energy_used = 0
made_toys = 0
count_days = 0

while len(elves_energy) != 0 and len(num_of_material_in_box) != 0:
    elf = elves_energy.popleft()
    box = num_of_material_in_box[-1]

    if elf < 5:
        continue

    count_days += 1
    current_toys = 0

    if count_days % 3 == 0:
        box *= 2
        current_toys += 1

    if elf >= box:
        elf -= box
        total_energy_used += box

        if count_days % 5 != 0:
            elf += 1
            current_toys += 1
        else:
            current_toys = 0

        num_of_material_in_box.pop()
    else:
        elf *= 2
        current_toys = 0

    made_toys += current_toys
    elves_energy.append(elf)

print(f"Toys: {made_toys}")
print(f"Energy: {total_energy_used}")
if elves_energy:
    print(f"Elves left: {', '.join(str(i) for i in elves_energy)}")
if num_of_material_in_box:
    print(f"Boxes left: {', '.join(str(i) for i in num_of_material_in_box)}")