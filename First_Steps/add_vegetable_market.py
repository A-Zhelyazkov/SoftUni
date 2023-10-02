price_vege = float(input())
price_fruit = float(input())
vege_kg = int(input())
fruit_kg = int(input())

total_vege = price_vege * vege_kg
total_fruit = price_fruit * fruit_kg
total_price = total_fruit + total_vege
total_price_eur = total_price / 1.94

print(f'{total_price_eur:.2f}')