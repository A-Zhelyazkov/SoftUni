from math import ceil
students = int(input())
lectures = int(input())
bonus = int(input())
max_num = float('-inf')

for i in range(students):
    attendance = int(input())
    if attendance > max_num:
        max_num = attendance

if lectures:
    total_bonus = ceil((max_num / lectures) * (5 + bonus))
    print(f"Max Bonus: {total_bonus}.")
    print(f"The student has attended {max_num} lectures.")
else:
    print(f"Max Bonus: 0.")
    print(f"The student has attended 0 lectures.")

