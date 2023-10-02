total_joinery = int(input())
type = input()
delivery_type = input()

price = 0
total_price = 0
if type == "90X130":
    price = 110
    total_price = price * total_joinery
    if 60 >= total_joinery > 30:
        total_price *= 0.95
    elif total_joinery > 60:
        total_price *= 0.92

if type == "100X150":
    price = 140
    total_price = price * total_joinery
    if 80 >= total_joinery > 40:
        total_price *= 0.94
    elif total_joinery > 80:
        total_price *= 0.9

if type == "130X180":
    price = 190
    total_price = price * total_joinery
    if 50 >= total_joinery > 20:
        total_price *= 0.93
    elif total_joinery > 50:
        total_price *= 0.88

if type == "200X300":
    price = 250
    total_price = price * total_joinery
    if 50 >= total_joinery > 25:
        total_price *= 0.91
    elif total_joinery > 50:
        total_price *= 0.86

if delivery_type == "With delivery":
    total_price += 60

if total_joinery > 99:
    total_price *= 0.96

if total_joinery > 10:
    print(f"{total_price:.2f} BGN")
else:
    print("Invalid order")
