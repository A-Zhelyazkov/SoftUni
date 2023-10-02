lost_fights = int(input())
helm_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
cost = 0
count = 0

for i in range(lost_fights):
    count += 1
    if count % 2 == 0:
        cost += helm_price
    if count % 3 == 0:
        cost += sword_price
    if count % 6 == 0:
        cost += shield_price
    if count % 12 == 0:
        cost += armor_price

print(f"Gladiator expenses: {cost:.2f} aureus")