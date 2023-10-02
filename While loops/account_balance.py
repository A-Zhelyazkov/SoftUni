total_money = 0

operation = input()

while operation != "NoMoreMoney":
    money = float(operation)
    if money < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {money:.2f}")
    total_money += money

    operation = input()

print(f"Total: {total_money:.2f}")