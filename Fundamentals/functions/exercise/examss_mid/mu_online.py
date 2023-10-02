rooms = input().split("|")
initial_health = 100
health = initial_health
btc = 0
room_count = 0
is_dead = False
for room in rooms:
    room = room.split()
    type_room = room[0]
    amount = int(room[1])
    room_count += 1

    if type_room == "potion":
        current_hp = health
        health = min(initial_health, health + amount)
        if 100 >= amount + current_hp:
            print(f"You healed for {amount} hp.")
        else:
            print(f"You healed for {initial_health - current_hp} hp.")
        print(f"Current health: {health} hp.")

    elif type_room == "chest":
        btc += amount
        print(f"You found {amount} bitcoins.")

    else:
        health -= amount
        if health <= 0:
            print(f"You died! Killed by {type_room}.")
            print(f"Best room: {room_count}")
            is_dead = True
            break
        else:
            print(f"You slayed {type_room}.")

if not is_dead:
    print("You've made it!")
    print(f"Bitcoins: {btc}")
    print(f"Health: {health}")



