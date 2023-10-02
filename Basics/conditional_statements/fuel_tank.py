import string
fuel = input()
litres_in_the_tank = int(input())
fuel = fuel.lower()

if fuel == "diesel" or  fuel == "gas" or fuel == "gasoline":
    if litres_in_the_tank >= 25:
        print(f"You have enough {fuel}.")
    elif litres_in_the_tank < 25:
        print(f"Fill your tank with {fuel}!")


else:
    print("Invalid fuel!")


