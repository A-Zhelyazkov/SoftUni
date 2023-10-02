a = float(input())
b = float(input())
operator = input()
total = 0

if b == 0:
    if operator == "/" or operator == "%":
        print(f"Cannot divide {int(a)} by zero")

elif operator == "-":
    total = a - b
    if total % 2 == 0:
        print(f"{int(a)} - {int(b)} = {int(total)} - even")
    else:
        print(f"{int(a)} - {int(b)} = {int(total)} - odd")

elif operator == "+":
    total = a + b
    if total % 2 == 0:
        print(f"{int(a)} + {int(b)} = {int(total)} - even")
    else:
        print(f"{int(a)} + {int(b)} = {int(total)} - odd")

elif operator == "*":
    total = a * b
    if total % 2 == 0:
        print(f"{int(a)} * {int(b)} = {int(total)} - even")
    else:
        print(f"{int(a)} * {int(b)} = {int(total)} - odd")

elif operator == "/":
    total = a / b
    print(f"{int(a)} / {int(b)} = {total:.2f}")

elif operator == "%":
    total = a % b
    print(f"{int(a)} % {int(b)} = {int(total)}")