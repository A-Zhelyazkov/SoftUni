from math import ceil
from math import floor

days_missing = int(input())
food_left = int(input())
food_dog_day_kg = float(input())
food_cat_day_kg = float(input())
food_turtle_day_gr = float(input())


total_dog_food = food_dog_day_kg * days_missing
total_cat_food = food_cat_day_kg * days_missing
total_turtle_food = food_turtle_day_gr * days_missing
total_turtle_food_kg = total_turtle_food / 1000

total_food_needed = total_turtle_food_kg + total_cat_food + total_dog_food

diff = abs(food_left - total_food_needed)
if food_left >= total_food_needed:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")