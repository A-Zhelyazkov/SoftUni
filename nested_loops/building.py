floors = int(input())
ap_per_floor = int(input())

for a in range(floors, 0, -1):
    for b in range(ap_per_floor):
        if a == floors:
            print(f"L{a}{b}", end=' ')
        elif a % 2 == 0:
            print(f"O{a}{b}", end=' ')
        elif a % 2 != 0:
            print(f"A{a}{b}", end=' ')
    print()