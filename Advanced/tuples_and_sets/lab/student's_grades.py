n = int(input())
data = {}
for _ in range(n):
    name, grade = input().split()
    grade = float(grade)

    if name not in data:
        data[name] = []

    data[name].append(grade)


for key, value in data.items():
    average_grade = sum(value) / len(value)
    print(f"{key} -> {' '.join([str(f'{i:.2f}') for i in value])} (avg: {average_grade:.2f})")