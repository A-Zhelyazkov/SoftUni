name = input()

year_counter = 0
grades_counter = 0
bad_year = 0

while True:
    grade = float(input())
    year_counter += 1

    if grade < 4:
        bad_year += 1
        if bad_year == 2:
            print(f"{name} has been excluded at {year_counter} grade")
            break
        year_counter -= 1
    else:
        grades_counter += grade

    if year_counter == 12:
        avg_grade = grades_counter / 12
        print(f"{name} graduated. Average grade: {avg_grade:.2f}")
        break

