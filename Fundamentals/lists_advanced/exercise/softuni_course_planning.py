seq = input().split(", ")

while True:
    command = input()

    if command == "course start":
        break

    command_args = command.split(':')
    action = command_args[0]
    lesson_title = command_args[1]

    if action == "Add":
        if lesson_title not in seq:
            seq.append(lesson_title)

    elif action == "Insert":
        index = int(command_args[2])
        if lesson_title not in seq:
            seq.insert(index, lesson_title)

    elif action == "Remove":
        if lesson_title in seq:
            seq.remove(lesson_title)

    elif action == "Swap":
        lesson_title2 = command_args[2]
        index_1 = seq.index(lesson_title)
        index_2 = seq.index(lesson_title2)
        seq[index_1], seq[index_2] = seq[index_2], seq[index_1]

    elif action == "Exercise":
        if lesson_title in seq:
            index_lesson = seq.index(lesson_title) + 1
            seq.insert(index_lesson, f"{lesson_title}-Exercise")
        else:
            seq.append(lesson_title)
            seq.append(f"{lesson_title}-Exercise")

print(seq)

# not rdy