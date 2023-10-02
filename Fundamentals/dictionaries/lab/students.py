students = {}
while True:
    input_line = input()

    if ":" not in input_line:
        break

    name, id, course = input_line.split(":")

    if course not in students:
        students[course] = {id: name}
    else:
        students[course][id] = name


input_line = input_line.replace("_", " ")
final_students = students[input_line]

for key, value in final_students.items():
    print(f"{value} - {key}")
