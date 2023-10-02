chicken_menu = int(input("Chicken menus: "))
fish_menu = int(input("Fish menus: "))
veggie_menu = int(input("Veggie menus: "))

price_chicken = chicken_menu * 10.35
price_fish = fish_menu * 12.40
price_veggie = veggie_menu * 8.15
price_for_menu = price_chicken + price_fish + price_veggie

price_dessert = price_for_menu * 0.2
delivery_price = 2.50

total_bill = price_for_menu + price_dessert + delivery_price

print(total_bill)