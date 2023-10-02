def shop_from_grocery_list(budget, products, *args):
    unable_to_buy = False
    for product, price in args:
        if product not in products:
            continue
        if price > budget:
            unable_to_buy = True
            break
        budget -= price
        products.remove(product)

    if unable_to_buy or products:
        return f"You did not buy all the products. Missing products: {', '.join(str(i) for i in products)}."

    return f"Shopping is successful. Remaining budget: {budget:.2f}."




print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))



