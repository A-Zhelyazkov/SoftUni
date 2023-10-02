budget = float(input())
season = input()
destination = ""
type_accommodation = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_accommodation = "Camp"
        price = budget * 0.3
    if season == "winter":
        type_accommodation = "Hotel"
        price = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_accommodation = "Camp"
        price = budget * 0.4
    if season == "winter":
        type_accommodation = "Hotel"
        price = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    type_accommodation = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{type_accommodation} - {price:.2f}")


