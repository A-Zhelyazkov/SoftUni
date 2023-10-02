from collections import deque
clients = deque()
while True:
    name = input()

    if name == "End":
        break

    elif name == "Paid":
        while clients:
            print(clients.popleft())
        continue

    clients.append(name)

print(f"{len(clients)} people remaining.")