type_flower = input()
count_flowers = int(input())
budget = int(input())
price = 0

if type_flower == "Roses":
    price = count_flowers * 5
    if count_flowers > 80:
        price = price * 0.9
elif type_flower == "Dahlias":
    price = count_flowers * 3.8
    if count_flowers > 90:
        price = price * 0.85
elif type_flower == "Tulips":
    price = count_flowers * 2.8
    if count_flowers > 80:
        price = price * 0.85
elif type_flower == "Narcissus":
    price = count_flowers * 3
    if count_flowers < 120:
        price = price * 1.15
elif type_flower == "Gladiolus":
    price = count_flowers * 2.5
    if count_flowers < 80:
        price = price * 1.2

diff = abs(budget - price)
if budget >= price:
    print(f"Hey, you have a great garden with {count_flowers} {type_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
