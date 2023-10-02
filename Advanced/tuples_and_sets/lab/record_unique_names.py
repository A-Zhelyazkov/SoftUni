n = int(input())

unique_names = set()

for _ in range(n):
    name = input()

    unique_names.add(name)

for i in unique_names:
    print(i)