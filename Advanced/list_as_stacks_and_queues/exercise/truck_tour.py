from collections import deque

stations = deque([[int(i) for i in input().split()] for _ in range(int(input()))])

tank = 0
i = 0
current_rotation = stations.copy()

while current_rotation:
    fuel, distance = current_rotation.popleft()
    tank += fuel

    if tank >= distance:
        tank -= distance
    else:
        tank = 0
        stations.rotate(-1)
        current_rotation = stations.copy()
        i += 1

print(i)


