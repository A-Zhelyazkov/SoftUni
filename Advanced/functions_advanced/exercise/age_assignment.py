def age_assignment(*args, **kwargs):
    names = []
    result = ''
    for key, value in kwargs.items():
        for name in args:
            if key == name[0]:
                names.append([name, value])
    sorted_result = sorted(names, key=lambda x: x[0])
    for items in sorted_result:
        result += f"{items[0]} is {items[1]} years old.\n"

    return result

print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36,
A=22, B=61))