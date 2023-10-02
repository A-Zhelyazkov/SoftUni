goal = int(input())
income = 0

while True:
    operation = input()

    if operation == "haircut":
        type_cut = input()
        if type_cut == "mens":
            income += 15
        elif type_cut == "ladies":
            income += 20
        elif type_cut == "kids":
            income += 10
    if operation == "color":
        type_color = input()
        if type_color == "touch up":
            income += 20
        elif type_color == "full color":
            income += 30

    if income >= goal:
        break
    if operation == "closed":
        break

diff = abs(income - goal)
if income >= goal:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {diff}lv. more.")

print(f"Earned money: {income}lv.")

