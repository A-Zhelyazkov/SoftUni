fuel = input()
fuel_litre = float(input())
club_card = input()

if fuel == "Gasoline":
    fuel_price = fuel_litre * 2.22
    if club_card == "Yes":
        fuel_price = fuel_price - (fuel_litre * 0.18)

elif fuel == "Diesel":
    fuel_price = fuel_litre * 2.33
    if club_card == "Yes":
        fuel_price = fuel_price - (fuel_litre * 0.12)

elif fuel == "Gas":
    fuel_price = fuel_litre * 0.93
    if club_card == "Yes":
        fuel_price = fuel_price - (fuel_litre * 0.08)

if 20 <= fuel_litre <= 25:
    fuel_price = fuel_price * 0.92
elif fuel_litre > 25:
    fuel_price = fuel_price * 0.9

print(f"{fuel_price:.2f} lv.")




