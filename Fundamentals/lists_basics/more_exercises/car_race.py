times = [int(i) for i in input().split()]
middle_of_the_list = len(times) // 2
left_racer = times[:middle_of_the_list]
right_racer = times[middle_of_the_list + 1:]
left_racer_time = 0
right_racer_time = 0

for i in range(len(left_racer)):
    if left_racer[i] == 0:
        left_racer_time *= 0.8
    left_racer_time += left_racer[i]
for k in range(len(right_racer) -1, -1, -1):
    if right_racer[k] == 0:
        right_racer_time *= 0.8
    right_racer_time += right_racer[k]


if left_racer_time < right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")
