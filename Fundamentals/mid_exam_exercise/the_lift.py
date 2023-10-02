total_people = int(input())
state_of_lift = [int(i) for i in input().split()]
new_list = []
people_left = total_people
flag = True
people_on_lift = 0
for i in state_of_lift:
    if i == 4:
        new_list.append(i)
        continue
    for k in range(4):
        if people_left == 0:
            break
        people_left -= 1
        i += 1
        people_on_lift += 1
        if i == 4:
            break
    new_list.append(i)
for i in new_list:
    if i == 4:
        continue
    else:
        flag = False
if people_on_lift == total_people and flag:
    print(*new_list)
elif people_left == 0:
    print("The lift has empty spots!")
    print(*new_list)
elif people_left > 0:
    print(f"There isn't enough space! {people_left} people in a queue!")
    print(*new_list)

