n = int(input())

reservations = set()

for _ in range(n):
    res_code = input()
    reservations.add(res_code)


while True:
    guest = input()

    if guest == "END":
        break

    if guest in reservations:
        reservations.remove(guest)


reservations = list(reservations)
reservations.sort()

print(len(reservations))
for i in reservations:
    print(i)