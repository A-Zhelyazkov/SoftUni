allowed_bad_grades = int(input())

task = input()
counter_bad_grades = 0
counter_problems = 0
counter_grades = 0
flag = False
while task != "Enough":
    problem = task
    grade = int(input())
    counter_problems += 1
    counter_grades += grade

    if grade <= 4:
        counter_bad_grades += 1
        if counter_bad_grades == allowed_bad_grades:
            flag = True
            break
    task = input()

if flag:
    print(f"You need a break, {counter_bad_grades} poor grades.")
else:
    avg_grades = counter_grades / counter_problems
    print(f"Average score: {avg_grades:.2f}")
    print(f"Number of problems: {counter_problems}")
    print(f"Last problem: {problem}")
