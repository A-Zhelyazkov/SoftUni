num_line = input().split()

counter = {}

for i in num_line:
    if i not in counter:
        counter[i] = 0

    counter[i] += 1

for key, value in counter.items():
    key = float(key)
    print(f"{key:.1f} - {value} times")