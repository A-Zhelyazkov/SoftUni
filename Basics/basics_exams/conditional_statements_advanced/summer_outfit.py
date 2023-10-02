temp = int(input())
part_of_day = input()
outfit = ""
shoes = ""

if part_of_day == "Morning":
    if 10 <= temp <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < temp <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif temp >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif part_of_day == "Afternoon":
    if 10 <= temp <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < temp <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif temp >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
if part_of_day == "Evening":
    if 10 <= temp <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < temp <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif temp >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {temp} degrees, get your {outfit} and {shoes}.")