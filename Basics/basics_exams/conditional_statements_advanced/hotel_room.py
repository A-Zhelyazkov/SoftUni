month = input()
nights = int(input())
price_apartment = 0
price_studio = 0

if month == "May" or month == "October":
    price_studio = nights * 50
    price_apartment = nights * 65
    if 14 >= nights > 7:
        price_studio *= 0.95
    elif nights > 14:
        price_studio *= 0.7
elif month == "June" or month == "September":
    price_studio = nights * 75.2
    price_apartment = nights * 68.7
    if nights > 14:
        price_studio *= 0.8
elif month == "July" or month == "August":
    price_studio = nights * 76
    price_apartment = nights * 77

if nights > 14:
    price_apartment *= 0.9

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")