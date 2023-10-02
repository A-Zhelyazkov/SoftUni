budget = float(input())
season = input()
price = 0
class_car = 0
car_type = 0

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        price = budget * 0.35
        car_type = "Cabrio"
    elif season == "Winter":
        car_type = "Jeep"
        price = budget * 0.65

elif budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        price = budget * 0.45
        car_type = "Cabrio"
    elif season == "Winter":
        car_type = "Jeep"
        price = budget * 0.8

elif budget > 500:
    class_car = "Luxury class"
    car_type = "Jeep"
    price = budget * 0.9

print(class_car)
print(f"{car_type} - {price:.2f}")


