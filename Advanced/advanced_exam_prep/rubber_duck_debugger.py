from collections import  deque


def select_ducky(time):
    if 0 < time <= 60:
        return "Darth Vader Ducky"
    elif 60 < time <= 120:
        return "Thor Ducky"
    elif 120 < time <= 180:
        return "Big Blue Rubber Ducky"
    elif 180 < time:
        return "Small Yellow Rubber Ducky"


programmers = deque(int(i) for i in input().split())
tasks = deque([int(i) for i in input().split()])
ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}
while programmers and tasks:
    programmer = programmers.popleft()
    task = tasks.pop()

    result = programmer * task

    if result > 240:
        task -= 2
        tasks.append(task)
        programmers.append(programmer)
        continue

    duck = select_ducky(result)
    ducks[duck] += 1

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in ducks.items():
    print(f"{key}: {value}")