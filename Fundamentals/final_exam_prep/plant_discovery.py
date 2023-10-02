n = int(input())
plants = {}
for _ in range(n):
    data = input()
    plant, rarity = data.split("<->")

    plants[plant] = {'rarity': rarity, 'rating': 0}

while True:
    data = input()
    if data == "Exhibition":
        break

    data_args = data.split(": ")
    command = data_args[0]

    if command == "Rate":
        plant, rate = data_args[1].split(" - ")
        if plant in plants:
            if plants[plant]['rating'] == 0:
                plants[plant]['rating'] += int(rate)
            else:
                plants[plant]['rating'] += int(rate)
                plants[plant]['rating'] /= 2
        else:
            print("error")

    elif command == "Update":
        plant, new_rarity = data_args[1].split(" - ")
        if plant in plants:
            plants[plant]['rarity'] = new_rarity
        else:
            print("error")

    elif command == "Reset":
        plant = data_args[1]
        if plant in plants:
            plants[plant]['rating'] = 0
        else:
            print("error")

print("Plants for the exhibition:")
for plant, values in plants.items():
    print(f"- {plant}; Rarity: {values['rarity']}; Rating: {values['rating']:.2f}")