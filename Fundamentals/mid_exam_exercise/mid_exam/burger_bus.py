cities = int(input())
total_profit = 0

for i in range(1, cities + 1):
    name_of_city = input()
    owners_income = float(input())
    owners_expenses = float(input())

    if i % 5 == 0:
        owners_income *= 0.9

    elif i % 3 == 0:
        owners_expenses *= 1.5

    city_profit = owners_income - owners_expenses
    total_profit += city_profit
    print(f"In {name_of_city} Burger Bus earned {city_profit:.2f} leva.")


print(f"Burger Bus total profit: {total_profit:.2f} leva.")