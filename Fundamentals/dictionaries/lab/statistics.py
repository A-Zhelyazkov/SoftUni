products = {}
while True:
    command = input()

    if command == "statistics":
        break

    key, arg2 = command.split(": ")
    value = int(arg2)

    if key not in products:
        products[key] = value
    else:
        products[key] += value

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")

