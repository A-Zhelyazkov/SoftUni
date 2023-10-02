animals = {}
areas = {}
while True:
    data = input()

    if data == "EndDay":
        break

    data_args = data.split(": ")
    command = data_args[0]

    if command == "Add":
        animal, needed_food, area = data_args[1].split("-")
        if animal not in animals:
            animals[animal] = {'needed_food': int(needed_food), 'area': area}
        else:
            animals[animal]['needed_food'] += int(needed_food)

        if area not in areas:
            areas[area] = []

        if animal not in areas[area]:
            areas[area].append(animal)

    elif command == "Feed":
        animal, food = data_args[1].split("-")
        if animal in animals:
            animals[animal]['needed_food'] -= int(food)
            if animals[animal]['needed_food'] <= 0 and animal in animals:
                area = animals[animal]['area']
                del animals[animal]
                print(f"{animal} was successfully fed")
                areas[area].remove(animal)


print(f"Animals:")
for animal, values in animals.items():
    print(f" {animal} -> {values['needed_food']}g")

print("Areas with hungry animals:")
for key, value in areas.items():
    if value:
        print(f" {key}: {len(value)}")