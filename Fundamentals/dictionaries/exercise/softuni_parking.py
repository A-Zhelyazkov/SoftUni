n = int(input())
parking = {}

for _ in range(n):
    command = input().split()
    action = command[0]
    name = command[1]

    if action == "register":
        plate = command[2]
        if name not in parking:
            parking[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[name]}")

    elif action == "unregister":
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            parking.pop(name)
            print(f"{name} unregistered successfully")

for name, plate in parking.items():
    print(f"{name} => {plate}")