budget = float(input())
count_stats = int(input())
price_clothes_one = float(input())

decor_price = budget * 0.1
price_clothes = count_stats * price_clothes_one

if count_stats > 150:
    price_clothes = price_clothes * 0.9

needed_cash = decor_price + price_clothes

diff = abs(budget - needed_cash)

if needed_cash > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")