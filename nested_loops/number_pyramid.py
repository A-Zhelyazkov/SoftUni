n = int(input())
counter = 0
for i in range(1, n + 1):
    for k in range(i):
        print(i, end=" ")
    print()