students = int(input())

fail = 0
below_good = 0
good = 0
excellent = 0
total_sum_grades = 0
for i in range(students):
    grade = float(input())
    total_sum_grades += grade
    if 2 <= grade < 3:
        fail += 1
    elif grade < 4:
        below_good += 1
    elif grade < 5:
        good += 1
    elif grade >= 5:
        excellent += 1

average_score = total_sum_grades / students
average_fail = (fail / students) * 100
average_below_good = (below_good / students) * 100
average_good = (good / students) * 100
average_excellent = (excellent / students) * 100

print(f"Top students: {average_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {average_good:.2f}%")
print(f"Between 3.00 and 3.99: {average_below_good:.2f}%")
print(f"Fail: {average_fail:.2f}%")
print(f"Average: {average_score:.2f}")



