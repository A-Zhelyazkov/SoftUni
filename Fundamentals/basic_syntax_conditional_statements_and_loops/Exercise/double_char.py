while True:
    action = input()
    if action == "End":
        break
    if action == "SoftUni":
        continue
    for i in action:
        print(i * 2, end='')
    print()

