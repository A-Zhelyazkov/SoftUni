people = int(input())
capacity = int(input())

courses_full = int(people / capacity)

if people % capacity == 0:
    print(f"{courses_full}")
else:
    courses_full += 1
    print(f"{courses_full}")