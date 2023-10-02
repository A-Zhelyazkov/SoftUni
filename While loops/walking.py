operation = input()

total_steps = 0
while operation != "Going home":
    steps = int(operation)
    total_steps += steps

    if total_steps >= 10000:
        break
    operation = input()


if operation == "Going home":
    steps_back_home = int(input())
    total_steps += steps_back_home
    diff = abs(total_steps - 10000)
    if total_steps >= 10000:
        print(f"Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
    else:
        print(f"{diff} more steps to reach goal.")
else:
    diff = abs(total_steps - 10000)
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")

