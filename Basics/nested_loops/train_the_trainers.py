count_jury = int(input())

operation = input()
total_grades = 0
count_grades = 0
while operation != "Finish":
    current_grade = 0
    for grades in range(count_jury):
        grade = float(input())
        current_grade += grade
        total_grades += grade
        count_grades += 1
    average_current_grade = current_grade / count_jury
    print(f"{operation} - {average_current_grade:.2f}.")

    operation = input()

average_grade = total_grades / count_grades
print(f"Student's final assessment is {average_grade:.2f}.")