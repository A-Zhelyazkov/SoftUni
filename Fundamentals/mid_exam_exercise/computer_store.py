total_price = 0
price_without_taxes = 0
taxes = 0
while True:
    command = input()

    if command == "special":
        total_price *= 0.9
        break
    if command == "regular":
        break
    if float(command) < 0:
        print("Invalid price!")
        continue

    price_without_taxes += float(command)
    total_price += float(command) * 1.2


taxes = price_without_taxes * 0.2
if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")


