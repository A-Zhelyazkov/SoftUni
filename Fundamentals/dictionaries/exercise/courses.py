courses = {}

while True:
    command = input()

    if command == "end":
        break

    course, name = command.split(" : ")

    if course not in courses:
        courses[course] = []

    courses[course].append(name)

for name in courses:
    print(f"{name}: {len(courses[name])} ")
    for person in courses[name]:
        print(f"-- {person}")