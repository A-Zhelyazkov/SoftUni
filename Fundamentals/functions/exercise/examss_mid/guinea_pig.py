quantity_food = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
guinea_weight = float(input()) * 1000
days = 1
flag = True
while days < 31:
    if quantity_food > 300:
        quantity_food -= 300
    else:
        flag = False
        break

    if days % 2 == 0:
        if quantity_hay > quantity_food * 0.05:
            quantity_hay -= quantity_food * 0.05
        else:
            flag = False
            break

    if days % 3 == 0:
        if quantity_cover > guinea_weight * 1/3:
            quantity_cover -= (1/3 * guinea_weight)
        else:
            flag = False
            break

    days += 1

if flag:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food / 1000:.2f}, Hay: {quantity_hay / 1000:.2f}, Cover: {quantity_cover / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")
