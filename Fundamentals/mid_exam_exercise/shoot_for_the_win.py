sequence = [int(i) for i in input().split()]
shot_targets = []
while True:
    command = input()

    if command == "End":
        break

    target = int(command)

    if target >= len(sequence) or target in shot_targets:
        continue
    else:
        current_target = sequence[target]
        sequence[target] = -1
        shot_targets.append(target)

    for i in range(len(sequence)):
        if sequence[i] == -1:
            continue
        else:
            if sequence[i] > current_target:
                sequence[i] -= current_target
            else:
                sequence[i] += current_target

final_string = ''
for i in sequence:
    final_string += str(f"{i} ")
print(f"Shot targets: {len(shot_targets)} -> {final_string}")
