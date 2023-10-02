from collections import deque

names = deque(input().split())
n = int(input()) - 1

while len(names) > 1:
    names.rotate(-n)
    lost = names.popleft()
    print(f"Removed {lost}")

print(f"Last is {names.popleft()}")