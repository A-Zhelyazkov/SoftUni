chrysanths = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
price = 0

price_summer_chrys = 2
price_summer_rose = 4.1
price_summer_tulip = 2.5
price_winter_chrys = 3.75
price_winter_rose = 4.5
price_winter_tulip = 4.15

if season == "Spring" or season == "Summer":
    price = (chrysanths * price_summer_chrys) + (roses * price_summer_rose) + (tulips * price_summer_tulip)

elif season == "Autumn" or season == "Winter":
    price = (chrysanths * price_winter_chrys) + (roses * price_winter_rose) + (tulips * price_winter_tulip)

if holiday == "Y":
    price = price * 1.15

if season == "Spring" and tulips > 7:
    price = price * 0.95
if season == "Winter" and roses >= 10:
    price = price * 0.9
if chrysanths + roses + tulips > 20:
    price = price * 0.8

print(f"{price + 2:.2f}")


