budget = float(input())
ticket = input()
people_in_group = int(input())
tickets_price = 0

if people_in_group <= 4:
    budget = budget * 0.25
elif people_in_group <= 9:
    budget = budget * 0.4
elif people_in_group <= 24:
    budget = budget * 0.5
elif people_in_group <= 49:
    budget = budget * 0.6
elif people_in_group >= 50:
    budget = budget * 0.75

if ticket == "Normal":
    tickets_price = people_in_group * 249.99
    diff = abs(budget - tickets_price)
    if budget > tickets_price:
        print(f"Yes! You have {diff:.2f} leva left.")
    else:
        print(f"Not enough money! You need {diff:.2f} leva.")

if ticket == "VIP":
    tickets_price = people_in_group * 499.99
    diff = abs(budget - tickets_price)
    if budget > tickets_price:
        print(f"Yes! You have {diff:.2f} leva left.")
    else:
        print(f"Not enough money! You need {diff:.2f} leva.")

