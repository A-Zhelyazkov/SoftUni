days_accommodation = int(input())
room_type = input()
grade = input()
nights = days_accommodation - 1
price = 0

price_rfop = nights * 18
price_apartment = nights * 25
price_president_apartment = nights * 35

if days_accommodation < 10:
    if room_type == "room for one person":
        price = price_rfop
    if room_type == "apartment":
        price = price_apartment * 0.7
    if room_type == "president apartment":
        price = price_president_apartment * 0.9

elif 10 <= days_accommodation <= 15:
    if room_type == "room for one person":
        price = price_rfop
    if room_type == "apartment":
        price = price_apartment * 0.65
    if room_type == "president apartment":
        price = price_president_apartment * 0.85

elif days_accommodation > 15:
    if room_type == "room for one person":
        price = price_rfop
    if room_type == "apartment":
        price = price_apartment * 0.5
    if room_type == "president apartment":
        price = price_president_apartment * 0.8

if grade == "positive":
    price = price * 1.25
elif grade == "negative":
    price = price * 0.9

print(f"{price:.2f}")
