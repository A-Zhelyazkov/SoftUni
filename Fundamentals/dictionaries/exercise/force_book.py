sides = {}
users_added = []
# not done
while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if "|" in command:
        side, user = command.split(" | ")

        if side not in sides and user not in users_added:
            sides[side] = []

        if user in users_added:
            continue

        sides[side].append(user)
        users_added.append(user)

    elif "->" in command:
        user, side = command.split(" -> ")
        if user in users_added and side in sides:
            for key in sides:
                if key != side:
                    sides[key].remove(user)
            for key in sides:
                if side == key:
                    sides[key].append(user)
        elif side not in sides:
            sides[side] = user
        elif user not in users_added:
            sides[side].append(user)

        print(f"{user} joins the {side} side!")


for side, lists in sides.items():
    if not lists:
        continue
    print(f"Side: {side}, Members: {len(lists)}")
    for i in lists:
        print(f"! {i}")




