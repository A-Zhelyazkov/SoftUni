n = int(input())
stack = []
final = []
for i in range(n):
    data = input().split()

    if data[0] == "1":
        stack.append(int(data[1]))

    elif data[0] == "2":
        if stack:
            stack.pop()
        else:
            continue

    elif data[0] == "3":
        if stack:
            print(max(stack))
        else:
            continue

    elif data[0] == "4":
        if stack:
            print(min(stack))
        else:
            continue

for i in range(len(stack)):
    final.append(stack.pop())

print(*final, sep=', ')