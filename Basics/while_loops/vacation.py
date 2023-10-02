money_needed = float(input())
current_money = float(input())

total_sum = current_money
days_spending = 0
total_days = 0
flag = False

while total_sum < money_needed:
    operation = input()
    amount = float(input())
    total_days += 1

    if operation == "save":
        total_sum += amount
        days_spending = 0

    elif operation == "spend":
        days_spending += 1
        total_sum -= amount
        if total_sum < 0:
            total_sum = 0
        if days_spending == 5:
            flag = True
            break

if flag:
    print("You can't save the money.")
    print(f"{total_days}")
else:
    print(f"You saved the money for {total_days} days.")




