price_luggage_over_20kg = float(input())
luggage_kg = float(input())
days_until_trip = int(input())
count_luggages = int(input())

price_luggage = 0
if luggage_kg < 10:
    price_luggage = price_luggage_over_20kg * 0.2
elif luggage_kg <= 20:
    price_luggage = price_luggage_over_20kg * 0.5
elif luggage_kg > 20:
    price_luggage = price_luggage_over_20kg

if days_until_trip > 30:
    price_luggage *= 1.1
elif days_until_trip >= 7:
    price_luggage *= 1.15
elif days_until_trip < 7:
    price_luggage *= 1.4

total_price = price_luggage * count_luggages

print(f"The total price of bags is: {total_price:.2f} lv. ")
