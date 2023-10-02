initial_list = [i.split() for i in input().split("|")]
result = []

for i in range(len(initial_list) -1, -1, -1):
    result.extend(initial_list[i])

print(*result)