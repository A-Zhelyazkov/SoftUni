orders = {}
while True:
    command = input()

    if command == "buy":
        break

    product, price_str, quantity_str = command.split()
    price = float(price_str)
    quantity = int(quantity_str)

    if product not in orders:
        orders[product] = [price, quantity]
    else:
        orders[product][1] += quantity
        orders[product][0] = price

for key, value in orders.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")

