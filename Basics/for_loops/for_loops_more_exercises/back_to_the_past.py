inherited_money = float(input())
year_to_live_until = int(input())

age = 17
expenses = 0
for i in range(1800, year_to_live_until + 1):
    age += 1
    if i % 2 == 0:
        expenses += 12000
    else:
        expenses += 12000 + 50 * age

diff = abs(expenses - inherited_money)
if inherited_money >= expenses:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")

