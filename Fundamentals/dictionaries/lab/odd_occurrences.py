sequence = input().lower().split()
occurrences = {}

for i in sequence:
    if i not in occurrences:
        occurrences[i] = 1
    else:
        occurrences[i] += 1

for key, value in occurrences.items():
    if value % 2 == 0:
        continue
    print(key, end=" ")