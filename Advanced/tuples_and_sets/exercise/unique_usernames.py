n = int(input())

unique_names = set()

for _ in range(n):
    username = input()

    unique_names.add(username)

for i in unique_names:
    print(i)