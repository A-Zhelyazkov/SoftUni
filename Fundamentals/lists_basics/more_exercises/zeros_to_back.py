initial_input = input().split(", ")
initial_input_ints = [int(i) for i in initial_input]

for i in initial_input_ints:
    if i == 0:
        initial_input_ints.remove(i)
        initial_input_ints.append(0)
    else:
        continue

print(initial_input_ints)