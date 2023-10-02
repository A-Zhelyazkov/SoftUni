product = input()
quantity_input = int(input())


def total_price(wanted_product, quantity):
    if wanted_product == "water":
        return 1 * quantity
    elif wanted_product == "coffee":
        return 1.5 * quantity
    elif wanted_product == "coke":
        return 1.4 * quantity
    elif wanted_product == "snacks":
        return 2 * quantity


total = total_price(product, quantity_input)
print(f"{total:.2f}")