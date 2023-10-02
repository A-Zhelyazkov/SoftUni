n = int(input())
students = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = grade

    students[name] += grade
    students[name] /= 2

for name, grade in students.items():
    if grade >= 4.5:
        print(f"{name} -> {grade:.2f}")