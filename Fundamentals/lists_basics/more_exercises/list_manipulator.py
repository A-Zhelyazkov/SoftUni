initial_seq = [int(i) for i in input().split()]

while True:
    command = input()

    if command == "end":
        break

    command = command.split()
    action = command[0]

    if action == "exchange":
        index = int(command[1])
        if index > len(initial_seq) or index < 0:
            print("Invalid index")
        if index == len(initial_seq):
            continue
        else:
            part1 = initial_seq[:index+1]
            part2 = initial_seq[index+1:]
            initial_seq = part2 + part1

    elif action == "max":
        second_arg = command[1]
        if second_arg == "even":
            current_even = [i for i in initial_seq if i % 2 == 0]
            if current_even:
                max_num = max(current_even)
                print(initial_seq.index(max_num))
            else:
                print("No matches")
        else:
            current_odd = [i for i in initial_seq if i % 2 != 0]
            if current_odd:
                max_num = max(current_odd)
                print(initial_seq.index(max_num))
            else:
                print("No matches")

    elif action == "min":
        second_arg = command[1]
        if second_arg == "even":
            current_even = [i for i in initial_seq if i % 2 == 0]
            if current_even:
                min_even = min(current_even)
                print(initial_seq.index(min_even))
            else:
                print("No matches")
        else:
            current_odd = [i for i in initial_seq if i % 2 != 0]
            if current_odd:
                min_odd = min(current_odd)
                print(initial_seq.index(min_odd))
            else:
                print("No matches")

    elif action == "first":
        count = int(command[1])
        if count > len(initial_seq) or count < 0:
            print("Invalid count")
            continue
        second_arg = command[2]
        if second_arg == "even":
            current_even = [i for i in initial_seq if i % 2 == 0]
            if not current_even:
                print([])
            elif count >= len(current_even):
                print(current_even)
            else:
                printable_list = [current_even[i] for i in range(0, count)]
                print(printable_list)

        if second_arg == "odd":
            current_odd = [i for i in initial_seq if i % 2 != 0]
            if not current_odd:
                print([])
            elif count >= len(current_odd):
                print(current_odd)
            else:
                current_odd = [current_odd[i] for i in range(0, count)]
                print(current_odd)

    elif action == "last":
        count = int(command[1])
        if count > len(initial_seq) or count < 0:
            print("Invalid count")
            continue
        second_arg = command[2]
        if second_arg == "even":
            current_even = [i for i in initial_seq if i % 2 == 0]
            if not current_even:
                print([])
            elif count >= len(current_even):
                print(current_even.reverse())
            else:
                printable_list = [current_even[i] for i in range(-1, len(current_even) - count, -1)]
                print(printable_list)

        if second_arg == "odd":
            current_odd = [i for i in initial_seq if i % 2 != 0]
            if not current_odd:
                print([])
            elif count >= len(current_odd):
                reversed_list = list(reversed(current_odd))
                print(reversed_list)
            else:
                printable_list = [current_odd[i] for i in range(-1, len(current_odd) - count, -1)]
                print(printable_list)

print(initial_seq)