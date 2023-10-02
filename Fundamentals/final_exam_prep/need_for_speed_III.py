cars_num = int(input())
cars = {}
for _ in range(cars_num):
    data = input().split("|")
    car = data[0]
    mileage = int(data[1])
    fuel = int(data[2])

    if car not in cars:
        cars[car] = {"mileage": mileage, "fuel": fuel}
    elif car in cars:
        cars[car]["mileage"] += mileage
        cars[car]["fuel"] += fuel

while True:
    command = input()

    if command == "Stop":
        break

    command_args = command.split(" : ")
    action = command_args[0]
    car = command_args[1]

    if action == "Drive":
        distance = int(command_args[2])
        fuel = int(command_args[3])
        if cars[car]["fuel"] >= fuel:
            cars[car]["fuel"] -= fuel
            cars[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")

        if cars[car]["mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]

    elif action == "Refuel":
        fuel = int(command_args[2])
        if cars[car]["fuel"] + fuel <= 75:
            cars[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")
        else:
            refilled_amount = 75 - cars[car]["fuel"]
            cars[car]["fuel"] = 75
            print(f"{car} refueled with {refilled_amount} liters")

    elif action == "Revert":
        km = int(command_args[2])
        if cars[car]["mileage"] - km >= 10000:
            cars[car]["mileage"] -= km
            print(f"{car} mileage decreased by {km} kilometers")
        else:
            cars[car]["mileage"] = 10000

for car, values in cars.items():
    print(f"{car} -> Mileage: {values['mileage']} kms, Fuel in the tank: {values['fuel']} lt.")