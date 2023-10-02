budget = float(input())
season = input()
cost = 0
accommodation = 0
country = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        country = "Alaska"
        cost = budget * 0.65
    elif season == "Winter":
        country = "Morocco"
        cost = budget * 0.45

elif budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        country = "Alaska"
        cost = budget * 0.8
    elif season == "Winter":
        country = "Morocco"
        cost = budget * 0.6

elif budget > 3000:
    if season == "Summer":
        country = "Alaska"
    elif season == "Winter":
        country = "Morocco"
    accommodation = "Hotel"
    cost = budget * 0.9

print(f"{country} - {accommodation} - {cost:.2f}")

