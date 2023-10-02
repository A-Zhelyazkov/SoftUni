items = input().split("|")
budget = float(input())
initial_budget = budget
bought_items = []
increased_items = []
for i in items:
    items_info = i.split("->")
    item = items_info[0]
    price = float(items_info[1])

    if item == "Clothes" and price > 50:
        continue
    if item == "Shoes" and price > 35:
        continue
    if item == "Accessories" and price > 20.50:
        continue
    if price > budget:
        continue

    budget -= price
    bought_items.append(price)

for k in bought_items:
    increased_price = k * 1.4
    increased_items.append(increased_price)
formatted_price = [float("%.02f" % x) for x in increased_items]

profit = sum(formatted_price) - sum(bought_items)
new_budget = budget + sum(formatted_price)
print(*formatted_price, sep=" ")
print(f"Profit: {profit:.2f}")
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
