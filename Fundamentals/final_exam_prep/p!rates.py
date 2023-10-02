cities = {}
while True:
    command = input()

    if command == "Sail":
        break

    city, population, gold = command.split("||")

    if city not in cities:
        cities[city] = {'population': int(population), 'gold': int(gold)}
    else:
        cities[city]['population'] += int(population)
        cities[city]['gold'] += int(gold)

while True:
    data = input()

    if data == "End":
        break

    data_args = data.split("=>")
    action = data_args[0]
    city = data_args[1]

    if action == "Plunder":
        people = int(data_args[2])
        gold = int(data_args[3])
        cities[city]['population'] -= people
        cities[city]['gold'] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[city]['population'] <= 0 or cities[city]['gold'] <= 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")

    elif action == "Prosper":
        gold = int(data_args[2])
        if gold >= 0:
            cities[city]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")
            continue

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, values in cities.items():
        print(f"{city} -> Population: {values['population']} citizens, Gold: {values['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
